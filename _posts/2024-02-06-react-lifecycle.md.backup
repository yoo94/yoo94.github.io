---
layout: post
title: "react 컴포넌트 라이프사이클"
summary: "컴포넌트 라이프사이클"
author: yoo94
date: "2024-02-06 11:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-component-lifecycle/
---

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240506123745.png" alt="Pasted image 20240506123745.png" style="max-width:auto;; height:auto;">
</div>

1. 마운트 : 컴포넌트가 처음으로 렌더링된 순간 / 컴포넌트가 DOM에 삽입되는 과정
2. 업데이트 : 컴포넌트가 리렌더링 된 순간 / 컴포넌트의 props 또는 state가 변경될 때
3. 언마운트 : 화면에서 사라진 순간 / 컴포넌트가 DOM에서 제거되는 과정

```text
1. 마운팅
   - constructor()
   - getDerivedStateFromProps()
   - render()
   - componentDidMount()

2. 업데이트
   - getDerivedStateFromProps()
   - shouldComponentUpdate()
   - render()
   - getSnapshotBeforeUpdate()
   - componentDidUpdate()

3. 언마운팅
   - componentWillUnmount()

함수형 컴포넌트 라이프사이클 (useEffect)

1. 마운팅 및 업데이트
   - useEffect(() => { ... }, [])
   - useEffect(() => { ... })
   - useEffect(() => { ... }, [dependencies])

2. 언마운팅
   - useEffect(() => { return () => { ... } }, [])
```
