---
layout: post
title:  "React 개발에서 Node.js"
summary: "nodeJs"
author: yoo94
date: '2023-05-02 14:35:23 +0530'
category: react
tags: react
keywords: react, nodeJs
thumbnail: https://blog.kakaocdn.net/dn/CXCxi/btszJHkBdaR/gzidgB00mb931TLMKkS3QK/img.png
permalink: /blog/react_with_nodejs/
---
React를 사용하기 위해서는 React , nodejs , 툴로는 vscode가 필요하다.

React니까 당연히 React이고 .. 툴은 vsCode가 아니라 인텔리제이도 사용가능하긴한데...

**nodeJs는 왜일까??? 알아보자** 

![](https://blog.kakaocdn.net/dn/CXCxi/btszJHkBdaR/gzidgB00mb931TLMKkS3QK/img.png)

nodejs는 웹서버역할을 대신 해주는 자바스크립트 런타임이다.( 런타임은 프로그래밍 언어가 구동되는 환경이다. - 프로그램이 동작하는 장소라고 생각하면 되겠다.  브라우저도 런타임이다.)

React는 웹 UI를 구성하기 위한 프론트엔드 자바스크립트 프레임워크이다.

JS는 웹사이트를 동적으로 사용하기 위해 웹브라우저에 내장된 js 엔진에 의해 동작한다. React 또한 웹 브라우저 환경에서 동작하면 된다.

React를 적용하고 싶은 DOM이란을 가져와서 render 함수를 실행시키면 그 DOM에 React 컴포넌트를 추가할 수 있다. 그렇게 되었을때 React에서 필수는 아니지만 많이들 JSX를 사용하게 된다. JSX는 JS의 새로운 표현 방법으로 React의 장점중에 하나라고 할 수 있다. 

 (그러나 순수 자바스크립트 문법이 아니기 때문에 웹 브라우저가 이해할 수 없다. 웹 브라우저가 이해할 수 있게 하기 위해선 JSX 코드를 React.createElement와 같은 함수로 변환해 줘야 한다.)

JSX에 관한 내용은 아래 링크에서 알아보도록 하자 (공식문서만 봐도 충분하고, 나머진 코드를 사용하여 익숙해져야할듯 싶다.)

JSX 소개 – React

A JavaScript library for building user interfaces

ko.legacy.reactjs.org](https://ko.legacy.reactjs.org/docs/introducing-jsx.html)

아무튼 JSX를 React에서 사용가능하게 코드를 변환해 줘야 하는데 이때 많이들 바벨이라는 것을 사용한다. 

바벨은 코드변환 라이브러리로 ES6 -> ES5로 변환해주기도하는 아주 효자손같이 편리한 도구이다.


#### **여기서 이제 node JS를 사용해야하는 이유가 나온다.**

#### **바벨은 JS컴파일러이고 NPM으로 설치 할 수 있기 때문이다.**


npm은 Node Package Manager로 node.js에서 사용하는 모듈을 패키지화해 모아둔 저장소이자 관리소이다. CLI를 통해 편하게 설치 할 수 있다. package.json 파일 내에 프로젝트 내에서 자주 사용하는 커맨드를 작성해 두고 npm CLI를 통해 쉽게 실행시킬 수도 있다. (곧 react에서 배운다)

아무튼 React 같은 웹 프레임워크를 사용하는 데 nodejs? 필수가아니다.

그치만 프로젝트가 커지고, 모듈도 정리안돼고, 암튼 불편하다. 그래서 node js가 필요한 것이다.