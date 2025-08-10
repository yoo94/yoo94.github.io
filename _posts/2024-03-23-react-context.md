---
layout: post
title: "react useContext"
summary: "프롭스 드릴링 방지 -> 전역으로"
author: yoo94
date: "2024-03-23 08:35:23 +0530"
category: Frontend2
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-context/
---

### 전역으로 데이터를 관리하고 싶을떄

- 컴포넌트는 ui 단위이며 재사용을 위해 외부에서 데이터를 전달 받기위해서는 Props를 사용하는데,
- 너무 많아지면 가독성이 떨어지게 된다.

![이미지](/blog/postImg/Pasted image 20240506180849.png)
![이미지](/blog/postImg/Pasted image 20240506180941.png)
![이미지](/blog/postImg/Pasted image 20240506180959.png)
![이미지](/blog/postImg/Pasted image 20240506181019.png)
![이미지](/blog/postImg/Pasted image 20240506181039.png)

## 사용하기

createContext는 보통 컴포넌트 밖에서 한다.

렌더링할때마다 새로운 컨텍스트를 다시 만들 필요가 없기 때문이다.

![이미지](/blog/postImg/Pasted image 20240506181813.png)

## 분리하기

![이미지](/blog/postImg/Pasted image 20240506182819.png)
![이미지](/blog/postImg/Pasted image 20240506182926.png)

# 부모

```jsx
//먼저 사용하려면 context로 값을 내려줄 부모 컴포넌트에서 이렇게 선언해준다.
import { createContext } from 'react'

//부모 컴포넌트에 context 객체를 선언해준다.
export const Context1 = createContext();
export const Context2 = createContext();

//보내줄 context객체를 jsx로 감싸주면 하위 컴포넌트들은 감싼 context 객체를 사용 할 수 있다. context도 객체이기 때문에 바로 넣지는 못하고 Context1.Provider에 value에 넣어준다.
return (
  <div className='App'>
   <Header />
   <Context1.Provider value={data1}>
    <Context2.Provider value={{dataitm1,dataitm2,dataitm3}}}>
     <Editor />
     <List />
    </Context2.Provider>
   </Context1.Provider>
  </div>

 )
```

# 자식

```jsx
//useContext를 선언해준다.
import { useContext } from "react";

//data1 처럼 바로 값을 보내준거면 아래와같이 할당
const data1 = useContext(context1);
//data2처럼 객체로 할당 했으면 객체구조할당을 사용하여 할당해준다.
const { dataitm1, dataitm2, dataitm3 } = useContext(context2);
```
