---
layout: post
title:  "JSX with css"
summary: "JSX css"
author: yoo94
date: '2024-01-12 15:35:23 +0530'
category: react
tags: react
thumbnail: /blog/postImg/Pasted image 20240505144527.png
permalink: blog/react-jsx-css/
---

jsx 에서는 css 를 입힐때는 카멜케이스로 입력해야한다.
1. 요소에 직접 스타일 속성 입히기
```jsx
const Main = ()=>{
  const user = {
    name: "유재석",
    isLogin: false,
  };

  if(user.isLogin){
    return <div style={{backgroundColor:"red"}}>로그아웃</div>
  }else{
    return <div style={{backgroundColor:"blue"}}>로그인</div>   
  }
}


export default Main
```

2. css파일을 만들어서 하기
<img src="/blog/postImg/Pasted image 20240505150240.png" alt="Pasted image 20240505150240.png" style="max-width:100%;">
이렇게 따로 뺀다음
<img src="/blog/postImg/Pasted image 20240505150347.png" alt="Pasted image 20240505150347.png" style="max-width:100%;">
이렇게 넣는다.
