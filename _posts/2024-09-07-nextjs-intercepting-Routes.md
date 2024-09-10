---
layout: post 
title:  "next intercepting"
summary: "next intercepting 라우팅"
author: yoo94 date: '2024-09-07 13:35:23 +0530' category: ['nextJs','react']
tags: react,nextJs
permalink: blog/next-intercepting-Routes/
---

## intercepting route
next에서는 인터셉팅이라는 라우팅 기법을 자동으로 제공한다.
사용자가 초기접속 요청이 아닌 csr로 접속하게 되었을때 ( link,push 등)으로 접속 했을때 
그럴때만 인터셉팅이 발동하고 그 조건은 고정적이다.

예를들어 인스타 피드에서 내가 상세페이지를 눌러서 내 화면에 상세페이지를 띄운뒤 뒤로가기를 눌렀을때 다시 원래 보던 피드 화면으로 
돌아가게 된다는 것이다. 

### ()book/[id] | (.)book/[id]
이렇게 해놓으면 book/[id] 경로를 가로 채라라는것이다.(.) 이거의 의미는 동일한 경로라는 뜻이다 (../) 이런식으로 어느 경로에있는
어떤 페이지 경로를 가로채라 라는 뜻이다.

즉 book/[id]로 갈때 csr로 접속하게 되면 (.)book/[id] 이쪽의 page.tsx로 가게 된다.



