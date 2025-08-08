---
layout: post
title: "float? "
summary: "동적 크기?"
author: yoo94
date: "2024-05-26 15:35:23 +0530"
category: Frontend1
tags: myconfused, float
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/float/
---

## float는 언제쓰지??

float는 CSS에서 요소를 왼쪽 또는 오른쪽으로 정렬하여 텍스트나 다른 요소들이 그 주위를 감싸도록 하는 속성이다.
원래는 이미지와 텍스트를 함께 배치하기 위해 사용되었으나, 레이아웃을 만들 때에도 자주 사용된다.

```html
<div class="container">
  <div
    class="box"
    style="float: left; width: 150px; height: 100px; background-color: lightblue;"
  >
    Left Float
  </div>
  <div
    class="box"
    style="float: right; width: 150px; height: 100px; background-color: lightcoral;"
  >
    Right Float
  </div>
  <div class="content" style="background-color: lightgray; height: 200px;">
    This is some content that flows around the floated elements.
  </div>
</div>
```

<div class="container">
  <div class="box" style="float: left; width: 150px; height: 100px; background-color: lightblue;">Left Float</div>
  <div class="box" style="float: right; width: 150px; height: 100px; background-color: lightcoral;">Right Float</div>
  <div class="content" style="background-color: lightgray; height: 200px;">This is some content that flows around the floated elements.</div>
</div>

```html

```
