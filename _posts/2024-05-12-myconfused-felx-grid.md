---
layout: post
title:  "felx와 grid의 차이? "
summary: "단방향과 양방향"
author: yoo94
date: '2024-05-12 19:35:23 +0530'
category: myconfused
tags: myconfused, felx, grid
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: /blog/felx-grid/
---

### flex랑 Grid의 차이점은?

- Flex는 1차원적인 1방향 레이아웃, 가로면 가로 세로면 세로로 레이아웃 구성이 가능
- Grid는 2차원적인 2방향 레이아웃이다. 가로 세로 동시에 가능

즉, 1차원 정렬이면 flex 2차원 정렬이면 grid를 사용하면 된다.


### flex 가로 세로
```html
<div style="display:flex;">
  <div style="background-color: rgb(226, 110, 43);">a</div>
  <div style="background-color: rgb(198, 231, 154);">a</div>
  <div style="background-color: rgb(238, 136, 136);">a</div>
  <div style="background-color: rgb(161, 184, 228);">a</div>
</div>

<div style="display:flex; flex-direction: column;">
   <div style="background-color: rgb(226, 110, 43);">a</div>
   <div style="background-color: rgb(198, 231, 154);">a</div>
   <div style="background-color: rgb(238, 136, 136);">a</div>
   <div style="background-color: rgb(161, 184, 228);">a</div>
</div>
```
<div style="display:flex;">
  <div style="background-color: rgb(226, 110, 43);">a</div>
  <div style="background-color: rgb(198, 231, 154);">a</div>
  <div style="background-color: rgb(238, 136, 136);">a</div>
  <div style="background-color: rgb(161, 184, 228);">a</div>
</div>
--------------------------------------
<div style="display:flex; flex-direction: column;">
  <div style="background-color: rgb(226, 110, 43);">a</div>
  <div style="background-color: rgb(198, 231, 154);">a</div>
  <div style="background-color: rgb(238, 136, 136);">a</div>
  <div style="background-color: rgb(161, 184, 228);">a</div>
</div>

### grid
```html
<div style="display:grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;">
  <div style="background-color: rgb(226, 110, 43);">a</div>
  <div style="background-color: rgb(198, 231, 154);">a</div>
  <div style="background-color: rgb(238, 136, 136);">a</div>
  <div style="background-color: rgb(161, 184, 228);">a</div>
</div>

```
<div style="display:grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr;">
  <div style="background-color: rgb(226, 110, 43);">a</div>
  <div style="background-color: rgb(198, 231, 154);">a</div>
  <div style="background-color: rgb(238, 136, 136);">a</div>
  <div style="background-color: rgb(161, 184, 228);">a</div>
</div>


