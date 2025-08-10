---
layout: post
title: "next navigate와 pre-fetching"
summary: "화면을 이동하고 불러오는법"
author: yoo94
date: "2024-08-23 13:35:23 +0530"
category: Frontend2
tags: react,nextJs
thumbnail:
permalink: blog/nextJs-navigate-pre-fetching/
---

## Link

원래는 a태그를 사용하는데 이 태그는 서버로부터 요청하는 방식으로 프로세스가 잡혀있다.
그래서 Link라는 컴포넌트를 사용하여 csr을 구현한다.

- Viewport 안에 있는 모든 <Link /> 태그는 Static Generation을 사용하는 페이지에서 prefetching 됨.

- 서버에서 렌더링 된 경로에 대한 데이터는 <Link />를 클릭했을 경우에만 가져옴.

```tsx
import Link from "next/link";

function Home() {
  return (
    <ul>
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/about">About Us</Link>
      </li>
      <li>
        <Link href="/blog/hello-world">Blog Post</Link>
      </li>
    </ul>
  );
}

export default Home;
```

---

## programmatic navigation - useRouter

- 이 말은 사용자가 링크를 클릭했을때만 이동하는게 아니라

- 특정 함수나 이벤트가 발생했을때 조건이 만족했을때 이동하는 방식이다.

```tsx
import Link from "next/link";
const router = useRouter();
const gogoButton = () => {
  router.push("/gogo");
};
<Button onClick={gogoButton}> 이동 </Button>;
```

- router.push: 새로운 경로로 이동. (히스토리 쌓임)
- router.replace: 현재 URL 대체.
- router.back: 뒤로 가기.
- router.reload: 새로고침.

---

## pre-fetching

현재 사용자가 보고있는 페이지를 미리 불러오는것을 말한다.

```tsx
import Link from 'next/link';

<Link href={'/'}>  이동 </Link>
<Link href={'/a'}>  이동 </Link>
<Link href={'/b'}>  이동 </Link>
```

이런식으로 있으면 이동 가능성이 있는 페이지를 서버에 요청해서 미리 불러와 있는 기능이다.

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/nextprocess.png" alt="nextprocess" style="max-width:auto;; height:auto;">
</div>

#### 추가적으로 서버에 리소스를 요청할 이유가 있나?

위에서 전달된 번들링된 js는 모든 파일에대한 js파일이 아니라 해당 페이지와 관련된 번들 파일만 제공한것이다.
만약에 전부다 주게되면 전달도 느려지고 브라우저와 js를 연결하는 hydraion 과정도 오래걸려서 Time to Interactive(TTI)가
늦어지게 되는 상황이 발생한다.

그렇게 되면 이것이 csr이 아니지 않나? 맞다 위 방법만으로는 그렇게 된다. 그래서 나온것이
pre-fetching이다.
링크나 버튼같은 이동 가능성이 있는 모든 페이지에 대한 것들을 미리 위에 js번들파일을 줄때 불러오는 것이다.

#### 결론적으로 페이지에 초기 접속 시 , hydration을 이용하면서 그 이후 페이지는 pre fetching을 이용한 방법이다.

##### npm run dev 로 즉, 개발모드로 진행할때는 프리팻칭은 동작하지 않는다.

##### 프로덕션 모드로 실행하자

```shell
npm run build
npm run start
```

### programmatic navigation은 prefetching 안된다. 그래서 하고싶으면

```tsx
import Link from "next/link";
const router = useRouter();
const gogoButton = () => {
  router.push("/gogo");
};
useEffect(() => {
  router.prefetch("/test");
}, []);

<Button onClick={gogoButton}> 이동 </Button>;
```

이제 이 화면이 마운트 되고나서 곧바로 useEffect가 실행될것이고 test페이지에 대한 프리패칭이 실행된다.

### link에서 프리패칭 하기 싫으면 밑에처럼 하면된다.

```tsx
<Link href={"/"} prefetch={false}>
  {" "}
  이동{" "}
</Link>
```
