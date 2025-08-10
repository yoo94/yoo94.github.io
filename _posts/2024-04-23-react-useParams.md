---
layout: post
title: "react hook useParams, useSearchParams"
summary: "동적 경로"
author: yoo94
date: "2024-04-23 13:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-useParams-useSearchParams/
---

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240507193110.png" alt="Pasted image 20240507193110.png" style="max-width:100%;; height:70%;">
</div>

동적 경로란 페이지가 렌더링 될 때, 동적으로 바뀌고있는 url을 말한다.
이것도 두가징 방법이 있다.

## 1. URL Parameter

위 이미지 같이 /뒤에 아이템의 id를 명시하는 것이다.
이때는

```jsx
import "./App.css";
import { Route, Routes, Link } from "react-router-dom";
import Home from "./pages/Home";
import New from "./pages/New";
import Diary from "./pages/Diary";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <>
      <div>
        <Link to={"/"}>Home</Link>
        <Link to={"/new"}>New</Link>
        <Link to={"/diary"}>Diary</Link>
      </div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/new" element={<New />} />
        //이렇게 reactRoute에 path에다가 /:이동할값이름 을 설정해 준 뒤
        <Route path="/diary/:id" element={<Diary />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}

export default App;
```

```jsx
// useParams를 import해준 다음
import { useParams } from "react-router-dom";

//useParams 객체를 변수에 담아 준 뒤, params.받을값이름으로 사용해 준다.
const Diary = () => {
  const params = useParams();
  return <div>{params.id}번 페이지 입니다.</div>;
};

export default Diary;
```

## Query string

쿼리 스트링을 사용 할 때는 우리가 흔히 아는 get방식이다.
url뒤에 /?변수명=값 의 식으로 전달하게 되는데
이거는 route에 뭔가를 해 줄 필요도 없다.

```jsx
//useSearchParams를 호출한 다음
import { useSearchParams } from "react-router-dom";

const Home = () => {
  //아래처럼 배열에 넣어준뒤 그냥 params.get(변수명)
  //을 해주면 된다.
  const [params, setParams] = useSearchParams();
  console.log(params.get("value"));
  return <div>Home</div>;
};

export default Home;
```
