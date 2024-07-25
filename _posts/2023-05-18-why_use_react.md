---
layout: post
title:  "React 왜!! react"
summary: "왜 리액트를 쓸까"
author: yoo94
date: '2023-05-18 15:35:23 +0530'
category: react
tags: react
keywords: react, nodeJs
thumbnail: https://blog.kakaocdn.net/dn/CXCxi/btszJHkBdaR/gzidgB00mb931TLMKkS3QK/img.png
permalink: blog/why_react/
---

## 산탄총 수술 할 필요없다.
### React는 Component 기반의 UI 라이브러리이기 때문에
- 보통의 웹사이트들은 헤더들과 같이 모든 화면에 공통적으로 적용되어야하는 소스가 분명히 존재한다. 리액트는 재사용될 요소들을 컨포넌트로 만들어서 사용 할 수 있다.

## 선언형 프로그래밍이다.
### 절차를 하나하나 다 나열 할 필요없기 때문이다.
- 목적을 바로 할 수 있다.
- 반대말은 명령형 프로그래밍이 있는데 대표적으로 Jquery 가있다.

## 버츄얼 DOM
### 브라우저의 부하를 줄일 수 있다.
- 브라우저는 DOM을 우리에게 보여주기 위해 많은 일을 하게 된다. DOM을 변경할 떄마다 복잡한 연산을 중복으로 실행하게 된다.
- 그래서 가상의 DOM을 만들어서 가상 DOM에다가 업데이트를 하는 것이다. 그 후에 최종 업데이트된 가상DOM 을 실제 DOM에다가 엎는것 그것이 버츄얼 DOM 기술이다.
- 리액트만의 기능은 아니지만, 리액트를 사용하면 편하게 사용할 수 있다.
