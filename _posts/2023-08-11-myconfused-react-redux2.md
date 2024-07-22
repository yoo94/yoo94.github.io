---
layout: post
title:  "react redux 사용방법"
summary: ""
author: yoo94
date: '2023-08-11 13:35:23 +0530'
category: ['react','myconfused']
tags: react,redux
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: /blog/react-redux2/
---

1. 프로젝트 설정
   먼저, 리액트와 리덕스를 설치. 새로운 리액트 프로젝트를 생성하고 리덕스를 설치.
코드 복사
```shell
npx create-react-app redux-counter
cd redux-counter
npm install redux react-redux
```

2. 리덕스 설정
   src/store.js 파일 생성
   리덕스 스토어를 설정하기 위해 src 폴더에 store.js 파일을 생성.
```javascript
// src/store.js
import { createStore } from 'redux';

// 초기 상태 설정
const initialState = {
count: 0,
};

// 리듀서 함수 정의
const counterReducer = (state = initialState, action) => {
switch (action.type) {
case 'INCREMENT':
return { ...state, count: state.count + 1 };
case 'DECREMENT':
return { ...state, count: state.count - 1 };
default:
return state;
}
};

// 스토어 생성
const store = createStore(counterReducer);

export default store;
```

3. 리액트에 리덕스 연결
   src/index.js 파일 수정
   리덕스 스토어를 리액트 애플리케이션에 연결합니다.

```javascript

// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './store';
import App from './App';

ReactDOM.render(
<Provider store={store}>
<App />
</Provider>,
document.getElementById('root')
);

````
4. 리덕스 상태 사용
   src/App.js 파일 수정
   리덕스 상태를 사용하여 카운터 애플리케이션을 구현합니다.

```javascript
// src/App.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

const App = () => {
const count = useSelector((state) => state.count);
const dispatch = useDispatch();

return (
<div>
<h1>Counter: {count}</h1>
<button onClick={() => dispatch({ type: 'INCREMENT' })}>Increment</button>
<button onClick={() => dispatch({ type: 'DECREMENT' })}>Decrement</button>
</div>
);
};

export default App;
```
