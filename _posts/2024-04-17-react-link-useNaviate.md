---
layout: post
title:  "react hook link / useNaviate"
summary: "이동!!!!"
author: yoo94
date: '2024-04-17 13:35:23 +0530'
category: react
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: /blog/react-link-useNaviate/
---
Link: a태그 대신 링크를 하고 싶을 때
useNavigate : 이벤트가 발생 하면서 이동 하고 싶을때

## Link

a태그 대신 클라이언트 사이드 렌더링 방식을 사용 할 때 사용, a태그 사용하면 서버 사이드 렌더링 됨

```jsx
import './App.css';
//Link를 import 해주고
import { Route,Routes,Link } from 'react-router-dom';
import Home from './pages/Home';
import New from './pages/New';
import Diary from './pages/Diary';
import NotFound from './pages/NotFound';


function App() {
 return (
  <>
  //아래처럼 Link태그에 렌더링하고싶은 페이지를 작성해 놓고 클릭하면 Routes 위에서 아래로 path를 확인하면서 to에 해당하는 컴포넌트를 렌더링 한다.
   <div>
    <Link to={"/"}>Home</Link>
    <Link to={"/new"}>New</Link>
    <Link to={"/diary"}>Diary</Link>
   </div>
   <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/new" element={<New />} />
    <Route path="/diary" element={<Diary />} />
    <Route path="*" element={<NotFound />} />
   </Routes>
  </>
 )
}

export default App

```

## useNavigate

링크가 아닌 함수 호출이나 이벤트가 발생 했을 때 원하는 페이지를 렌더링 하고 싶을때
```jsx
import './App.css';
//useNavigate선언
import { Route,Routes,Link,useNavigate } from 'react-router-dom';
import Home from './pages/Home';
import New from './pages/New';
import Diary from './pages/Diary';
import NotFound from './pages/NotFound';

function App() {
 //useNavigate객체를 nav에 넣어줌
 const nav = useNavigate();
 // 버튼 킬릭시 nav객체에 가고싶은 path를 넣어주면 Routes를 읽어가며 일치하는 path를 확인 후 컴포넌트를 뿌려줌
 const onClickButton=()=>{
  nav("/new")
 };
 return (
  <>
   <button onClick={onClickButton}>New</button>
   <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/new" element={<New />} />
    <Route path="/diary" element={<Diary />} />
    <Route path="*" element={<NotFound />} />
   </Routes>
  </>
 )
}

export default App
```
