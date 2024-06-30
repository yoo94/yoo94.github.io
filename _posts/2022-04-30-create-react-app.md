---
layout: post
title:  "create-react-app 및 설명"
summary: "react 프로젝트 만들기"
author: yoo94
date: '2023-05-01 14:35:23 +0530'
category: react
tags: react
thumbnail: /assets/postImg/posts/Pasted image 20240114133527.png
permalink: /blog/what_is_react/
---
먼저 npx 를 설치해야한다.
설치되어있지 않은 패키지를 한번만 설치하고 싶을때 쓰는거라고 생각하면 된다.

```
npm install -g npx
```

```
npx create-react-app reactexam1
```

```
npm start
```
로 시작하면 localhost:3000로 리액트가 시작된다.

---
## 리액트 시작 index.js

리액트든, 스프링이든 어떤 웹사이트의 시작은 대부분
index.js
이다.


![[Pasted image 20240114133527.png]]

이렇게 index.js를 보면 APP 컨포넌트를 root라는 dom의 id에 렌더 한다는 의미의 소스를 볼 수 있다.

APP 컨포넌트는 App.js에 있고, *root* 는 src가 아닌 public에 ![[Pasted image 20240114133734.png]]
index.html을 보면 들어있는것을 알 수 있다.

## SPA
리액트는 spa 즉 single page app 이기 때문에 하나의 페이지에서 dom 을 렌더링하면서 바꿔주고 있다.


## node_modules
react-app으로 프로젝트를 설치하게 되면, 기본적으로node_modules에는 굉장히 많은 모듈들이 설치되게 된다.
![[Pasted image 20240114134144.png]]
이러한 모듈들을 전부 git같은 형상관리소에 올리게되면 굉장히 비효율적은 형상관리가 된다.
***그러나 node.js 패키지는 저러한 모듈들이 없어도 상관없다. 왜냐하면 어떠한 모듈일 필요한지는 package.json 과 package-lock.json에 다 명시가 되어있기 때문이다.***

만약에 node_modules가 없다.
```
npm i
```
라는 명령어를 날리면 자동으로 다운받게 된다.

---
###### logo192.png , logo512.png. mainfest.json
이 세개의 파일은 나중에 모바일 환경에서 보게되었을때 관련된 파일들이다.

###### robots.txt
구글같은 웹사이트에서 데이터 수집 시, 어떤건 수집하고 이건 하지말아라 하는 것을 나타내는것이다.

###### App.jest.js
테스트 용도 없어도됨
