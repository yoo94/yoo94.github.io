---
layout: post
title:  "react vue 차이는 무엇인가?"
summary: "react-vue"
author: yoo94
date: '2024-02-21 13:35:23 +0530'
category: ['myconfused','react']
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: /blog/react-vue/
---
#### react와 vue의 차이점에 있어 가장 대표적인 것은, 먼저 react는 UI 라이브러리이며 Vue는 프레임워크라는 것이다.

### 리액트
라이브러리는 참고가 용이하고, 라이브러리의 일부분만 가져와서 사용하는 게 편리하다. 
하지만 리액트는 UI 라이브러리이기 때문에 리액트 자체만으로는 전역 상태 관리, 라우팅, 빌드 시스템 등을 지원하지 않는다. 
그렇기 때문에 리액트는 별도의 라이브러리를 통해 Redux, Recoil, React-router-dom 등의 미들웨어를 사용해야 한다. 

### 뷰
뷰는 자바스크립트 프레임워크이다. 
부분적인 사용이 불가능하고 프레임워크 안으로 들어가서 프레임 워크가 지원해주는 문법에 따라 작성해주어야 한다. 
그렇기 때문에 라이브러리와 달리 더 많은 기능을 디폴트로 제공해준다.

## 차이
1. 코드 형태의 차이
- 리액트는 JSX(JavaScript XML) 형태로 코드를 작성하여 JavaScript 문법을 응용하기 때문에 JavaScript만으로 UI 로직과 DOM을 구현

- 뷰는 HTML, JS, CSS 코드 영역을 분리해서 작성한다. ".vue " 파일을 만들 때에도 패턴이 존재한다. 
". vue"에서 <template>에 HTML 작성 영역, <script> 안에는 JS, <style> 안에 CSS를 작성한다.

- 리액트는 뷰에 비해 자유롭게 자바스크립트를 통해 코드를 구현할 수 있다.
하지만 뷰는 뷰에서 제공해주는 방법을 반드시 사용해야 한다. 뷰는 정해진 방법만 사용하기 때문에 자유도가 낮지만
그만큼 코드 작성에 있어서 용이하기 때문에 리액트보다 접근성이 더 좋지 않을까란 생각이 든다.

2. 컴포넌트 분리와 재사용

- 리액트의 가장 큰 장점 중 한가지는 컴포넌트의 생성 및 재사용이라고 생각한다. 파일별로 컴포넌트를 분리할 수 있으며, 새로운 함수형 컴포넌트를 생산하고, props 형태로 전달하거나 또는 다른 곳에서 재사용하는 것이 매우 용이하다.
하지만 뷰는 새로운 컴포넌트를 만들어 분리하기 위해서 새로운 파일을 하나 더 만들고, 그에 따라 하나의 파일에 해당하는 template, script, style 모두 작성해주어야 한다.
뿐만 아니라 props를 전달하는 과정에서도 해당 컴포넌트를 사용하는 모든 파일을 오가며 작성해주어야 한다.

