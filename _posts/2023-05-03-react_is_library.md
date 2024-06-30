---
layout: post
title:  "React는 라이브러리"
summary: "프레임워크가 아니다!"
author: yoo94
date: '2023-05-03 12:35:23 +0530'
category: react
tags: react
keywords: react
thumbnail: /assets/postImg/Pasted image 20240205195107.png
permalink: /blog/react_is_library/
---
### **1. React 는 프레임워크일까? 라이브러리일까?**

그 답은 React 공식 홈페이지에서 얻을 수 있었다.
https://ko.legacy.reactjs.org/

Render 과정의 라이프사이클을 예시로 했을 때, 순서는 다음과 같습니다.

1) componentWillMount()

2) render()

3) componentDidMount()

React는 위와 같이 프로그램 흐름의 기본적인 틀은 정해져 있다.

하지만 앱 실행시 render() 함수는 입력이 필수이지고  componentDidMount() 함수는 자동으로 생성되지만 개발자가 명시적으로 입력해 줄 필요는 없다.

하지만 개발자가 API를 호출하거나 다른 작업을 수행하기를 원할 때, componentDidMount()를 통해 프로그램을 추가적인 동작을 정의할 수 있습니다.

이처럼 프로그램 흐름에 작업을 추가하거나 그렇게 하지 않음으로서 프로그램의 흐름을 바꾸는 것이 가능하기 때문에 React가 라이브러리인 것 같다.