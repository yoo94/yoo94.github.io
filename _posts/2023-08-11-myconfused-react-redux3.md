---
layout: post
title:  "react redux configureStore 사용방법"
summary: ""
author: yoo94
date: '2023-08-11 16:35:23 +0530'
category: Frontend
tags: react,redux
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-redux3/
---

configureStore는 Redux 스토어를 생성하는 함수로, 
Redux의 기본 createStore 함수보다 간편하게 스토어를 설정할 수 있도록 도와준다.

Redux Toolkit에서는 configureStore 함수를 사용하여 미들웨어 설정,
Redux DevTools Extension 연결 등의 작업을 자동으로 처리할 수 있다.
#### 기본 구조
```js
import { configureStore } from "@reduxjs/toolkit";

const store = configureStore({
  reducer: rootReducer, // rootReducer를 포함한 리듀서 객체
  middleware: [
    /* 미들웨어 배열 */
  ],
  devTools: true, // Redux DevTools Extension을 사용할지 여부
});
```
###### reducer:
configureStore 함수의 인자로 넣어주어야 하는 속성으로, 모든 리듀서를 합친 rootReducer를 전달한다.

###### middleware:
미들웨어를 배열 형태로 전달하는 속성으로, Redux 미들웨어를 커스터마이징할 수 있습니다.
기본적으로 Redux Toolkit은 redux-thunk와 immutable-state-invariant 미들웨어를 자동으로 포함시킨다.

###### devTools:
개발 환경에서 Redux DevTools Extension을 사용할지 여부를 설정하는 속성입니다. 기본값은 true로 설정되어 있다.
