---
layout: post title:  "next Parallel Routes "
summary: "next 병렬 라우팅"
author: yoo94 date: '2024-09-05 13:35:23 +0530' category: ['nextJs','react']
tags: react,nextJs
permalink: blog/next-Parallel-Routes/
---

## Parallel Routes?
병렬 라우트로 하나의 페이지 안에 여러 페이지를 한꺼번에 렌더링해주는것을 말한다.
여러 page.tsx를 하나의  화면에 병렬 렌더링 해준다.

사이드바 같은거 해주면 좋을거같다.

#### parallel/@sidebar/page.tsx
이런식으로 @ 이걸 붙여주면, 그안에 있는 page.tsx는 parallel/layout.tsx 라는 부모 컴 포넌트의 레이아웃에 자동으로 props로 전달이된다.

<img src="/blog/postImg/next-parallel.png" alt="next-parallel.png" style="max-width:100%;">

sidebar라는 이름으로 전달 될 것이다.

참고로 @파일은 갯수 제한이 없다.


