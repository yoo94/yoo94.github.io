---
layout: post
title:  "next server-action "
summary: "next의 강력한 기능"
author: yoo94
date: '2024-09-04 13:35:23 +0530'
category: ['nextJs','react']
tags: react,nextJs
thumbnail: 
permalink: blog/next-server-action/
---

## 서버 액션이란?
브라우저에서 호출할 수 있는 서버에서 실행되는 비동기 함수!
즉 별도의 api를 만들 필요없이, 간단한 함수로 서버 함수를 호출 할 수 있다.

```tsx
export default function Page() {
    const saveName = async (formData: FormData) => {
        "use server";
        
        const name = formData.get("name");
        await sql `INSERT INTO Names (name) VALUES (${name})`;
    };

    return (
        <form action={saveName}>
            <input name="name" placeholder="이름을 알려주세요..." />
            <button type="submit">제출</button>
        </form>
    );
}

```
위에처럼 form 이벤트가 발생할때 서버에서 실행되는것처럼 저렇게 sql을 보낼수도있고
백엔드의 함수를 실행 할 수도 있다.
