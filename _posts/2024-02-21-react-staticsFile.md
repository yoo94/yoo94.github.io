---
layout: post
title: "react 정적파일 설정"
summary: "이미지, 폰트"
author: yoo94
date: "2024-02-21 13:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-staticFiles/
---

#### 이미지 넣기

```jsx
import './App.css';

import { Route,Routes,Link,useNavigate } from 'react-router-dom';

//js에서 이미지를 불러올수있는 함수를 만들어 모듈화 해줌 import함
import { getEmotionImage } from './util/get-emotion-image';
...
 return (
  <>
  //img태그에 src에 함수를 호출해
   <div>
    <div style="display: flex; justify-content: center;">
  <img  src={getEmotionImage(1)}/ style="width:auto; height:auto;">
</div>
    <div style="display: flex; justify-content: center;">
  <img  src={getEmotionImage(2)}/ style="width:auto; height:auto;">
</div>
    <div style="display: flex; justify-content: center;">
  <img  src={getEmotionImage(3)}/ style="width:auto; height:auto;">
</div>
    <div style="display: flex; justify-content: center;">
  <img  src={getEmotionImage(4)}/ style="width:auto; height:auto;">
</div>
    <div style="display: flex; justify-content: center;">
  <img  src={getEmotionImage(5)}/ style="width:auto; height:auto;">
</div>
   </div>
...
<Routes>
    <Route path="/" element={<Home />} />
    <Route path="/new" element={<New />} />
    <Route path="/diary/:id" element={<Diary />} />
    <Route path="*" element={<NotFound />} />
   </Routes>
  </>
 )
}


export default App
```

```jsx
//이미지들을 경로에 맞춰서 잘 설정해 주고
import emotion1 from "./../assets/emotion1.png";

import emotion2 from "./../assets/emotion2.png";

import emotion3 from "./../assets/emotion3.png";

import emotion4 from "./../assets/emotion4.png";

import emotion5 from "./../assets/emotion5.png";

//함수를 호출하면 이미지를 불러올수있게 함수를 설정해준다.
export function getEmotionImage(emotionId) {
  switch (emotionId) {
    case 1:
      return emotion1;
    case 2:
      return emotion2;
    case 3:
      return emotion3;
    case 4:
      return emotion4;
    case 5:
      return emotion5;
    default:
      return null;
  }
}
```

#### 폰트

```css
@font-face {
  font-family: "NanumPenScript";
  src: url("/NanumPenScript-Regular.ttf");
}
body * {
  font-family: "NanumPenScript";
}
```
