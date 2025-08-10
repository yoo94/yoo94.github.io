---
layout: post
title: "next server-action "
summary: "next의 강력한 기능"
author: yoo94
date: "2024-09-04 13:35:23 +0530"
category: Frontend2
tags: react,nextJs
permalink: blog/next-server-action/
---

## 서버 액션이란?

브라우저에서 호출할 수 있는 서버에서 실행되는 비동기 함수!
즉 별도의 api를 만들 필요없이, 간단한 함수로 서버 함수를 호출 할 수 있다.

```tsx
export default function Page() {
  const saveNameAction = async (formData: FormData) => {
    "use server";

    const name = formData.get("name");
    await sql`INSERT INTO Names (name) VALUES (${name})`;
  };

  return (
    <form action={saveNameAction}>
      <input name="name" placeholder="이름을 알려주세요..." />
      <button type="submit">제출</button>
    </form>
  );
}
```

위에처럼 form 이벤트가 발생할때 서버에서 실행되는것처럼 저렇게 sql을 보낼수도있고 백엔드의 함수를 실행 할 수도 있다.

### 백엔드로부터 api 명세를 받게되면 그 api를 호출하는 것들을 작성하면 된다.

```tsx
//actions/create-contentAction.tsx 와 같이 따로 빼서 하는게 가독성이 좋다.
"use server";

async function saveContentAction(formData: FormData) {
  const content = formData.get("content")?.toString();
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_SERVER_URL}/review`,
      {
        method: "POST",
        body: JSON.stringify({ content }),
      }
    );
  } catch (e) {}
}
```

#### 자동 rerendering하기 revalidatePath

```tsx
//actions/create-contentAction.tsx 와 같이 따로 빼서 하는게 가독성이 좋다.
"use server";

async function saveContentAction(formData: FormData) {
  const content = formData.get("content")?.toString();
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_SERVER_URL}/review`,
      {
        method: "POST",
        body: JSON.stringify({ content }),
      }
    );
    //1. 특정 주소의 해당하는 페이지만 재검증
    revalidatePath(`/book/${bookId}`);

    //2. 특정 경로의 모든 페이지 재검증
    revalidatePath(`/book/[id]`, "page");

    //3. 특정 레이아웃을 갖는 모든 페이지 재검증 - searchbar 레이아웃을 갖는 모든 페이지를 재검증한다.
    revalidatePath(`/(with-searchbar)`, "layout");

    //4. 모든 데이터 재검증 - 모든 페이지를 재검증
    revalidatePath(`/`, "layout");

    //5. 태그 기준, 데이터 캐시 재검증 아래 소스 참고
    revalidatePath("tag");
  } catch (e) {}
}
```

revalidatePath이걸 호출하게 되면 이 안에 전달된 인수경로에대한 페이지컴포넌트를 다시 검증하여 재렌더링 해준다. 즉 page.tsx에 있는 모든 컴포넌트와 서버액션을 다시 호출한다는 얘기다.

##### 대신 revalidatePath이건 서버단에서만 실행 가능하다. 즉 server컴포넌트에서만 가능하다는 얘기

##### revalidatePath이게 실행되면 캐싱된 데이터들은 어떻게 하든 다 무표화되기 때문에 fetch같은것들은 다시 생성이 된다.

##### 게다가 풀 라우터 캐시까지 다 초기화 시키고, 다시 업데이트 치진 않는다.. 이건 큰 문제이다. 그래서 새로고침을 다시 해줘야한다.

![next-server-action0904.png](/blog/postImg/next-server-action0904.png)

이미지와 같이 각종 fetch 데이터들은 다시 set 되지만 풀라우트 캐시는 안되기때문에 재접속시에 풀라우트 캐시를 set 해주게된다. 재접속하게 되었을때 무조건 최신의 데이터를 보장하기위해 이렇게 동작한다고한다.

```tsx
//actions/create-contentAction.tsx 와 같이 따로 빼서 하는게 가독성이 좋다.
"use server";

async function saveContentAction(formData: FormData) {
  const content = formData.get("content")?.toString();
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_SERVER_URL}/review`,
      {
        method: "POST",
        body: JSON.stringify({ content }),
      }
    );

    //5. 태그 기준, 데이터 캐시 재검증 - 이렇게 태그를 붙여준다음
    revalidatePath(`${bookid}`);
  } catch (e) {}
}

// 다른 컴포넌트에서 같은 태그를 next 객체에 넣어주면 revalidatePath이루어질때마다 저 태그를 가진것들이 다시 재검증된다.
async function getList() {
  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_SERVER_URL}/getList`,
      { next: { tags: [`${bookid}`] } }
    );
  } catch (e) {}
}
```

이렇게 되면 태그값을 가지고있는 데이터 캐시만 초기화해주기때문에 훨씬 더 경제적으로 할 수 있다.
