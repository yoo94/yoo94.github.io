---
layout: post
title: "react router"
summary: "대다수의 리액트앱이 사용중"
author: yoo94
date: "2024-04-08 18:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-router/
---

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240507184422.png" alt="Pasted image 20240507184422.png" style="max-width:100%;; height:70%;">
</div>

```shell
npm i react-router-dom
```

리액트 라우터를 먼저 다운 받아주고

## main.jsx

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
// BrowserRouter를 import를 해준다.
import { BrowserRouter } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  //App 컴포넌트를 감싸준다.
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

## App.jsx

```jsx
import "./App.css";
// Routes와 Route를 import해준다.
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import New from "./pages/New";
import Diary from "./pages/Diary";
import NotFound from "./pages/NotFound";

// 페이지들
// 1. "/" 모든 일기를 조회하는 home 페이지
// 2. "/new" : 새로운 일기를 작성하는 new 페이지
// 3. "/diary" : 일기를 상세히 조회하는 diary 페이지
function App() {
  return (
    <>
      //Routes 밖에 있는 태그는 모든 화면에 렌더링이 된다.
      <div>header</div>
      //Routes로 감싸고 가야할 페이지를 Route에 넣어준다. //Route에는 원하는
      경로 path와 렌더링할 컴포넌트를 element에 넣어준다.
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/new" element={<New />} />
        <Route path="/diary" element={<Diary />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}

export default App;
```
