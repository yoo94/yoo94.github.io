---
layout: post
title: "react의 redux!"
summary: "리덕스"
author: yoo94
date: '2024-08-03 16:32:23 +0530'
category: ['inner-Circle']
tags:
  - react
  - redux
thumbnail: 
permalink: blog/react-redux/
---
# Redux란? 
Redux는 애플리케이션의 상태를 중앙에서 관리하는 JavaScript 라이브러리

기본 개념
스토어 (Store): 애플리케이션의 전체 상태를 저장하는 객체.
액션 (Action): 상태 변화를 일으키는 사건을 나타내는 객체입. 액션은 반드시 type 속성을 가져한다.
리듀서 (Reducer): 액션을 처리하여 새로운 상태를 반환하는 함수.
디스패치 (Dispatch): 액션을 스토어에 보내는 함수.
미들웨어 (Middleware): 액션이 리듀서에 도달하기 전에 가로채어 추가 작업을 수행하는 함수.

```bash
npm install redux
```

## (1) 액션 생성자 (Action Creator)
액션을 생성
```javascript
// actions.js
export const increment = () => ({
  type: 'INCREMENT'
});

export const decrement = () => ({
  type: 'DECREMENT'
});
```
## (2) 리듀서 (Reducer)
액션을 처리하여 새로운 상태를 반환하는 함수
```javascript
// reducers.js
const initialState = { count: 0 };

const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { count: state.count + 1 };
    case 'DECREMENT':
      return { count: state.count - 1 };
    default:
      return state;
  }
};

export default counterReducer;
```

(3) 스토어 생성 (Store Creation)
스토어를 생성하고 리듀서를 연결.

```javascript
// store.js
import { createStore } from 'redux';
import counterReducer from './reducers';

const store = createStore(counterReducer);

export default store;
```
###(4) 디스패치 액션 (Dispatch Actions)
스토어에 액션을 디스패치하여 상태를 변경
```javascript
// index.js
import store from './store';
import { increment, decrement } from './actions';

// 상태 변경 구독 (옵션)
store.subscribe(() => console.log(store.getState()));

// 액션 디스패치
store.dispatch(increment()); // count: 1
store.dispatch(increment()); // count: 2
store.dispatch(decrement()); // count: 1
```
## react 에서의 redux
###(1) Provider로 애플리케이션 감싸기
Provider 컴포넌트를 사용하여 Redux 스토어를 React 컴포넌트 트리에 제공
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import App from './App';
import store from './store';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```
###(2) React 컴포넌트에서 상태와 액션 사용
useSelector와 useDispatch 훅을 사용하여 Redux 상태와 액션을 사용.

```javascript
// Counter.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './actions';

const Counter = () => {
const count = useSelector((state) => state.count);
const dispatch = useDispatch();

return (
<div>
<p>Count: {count}</p>
<button onClick={() => dispatch(increment())}>Increment</button>
<button onClick={() => dispatch(decrement())}>Decrement</button>
</div>
);
};

export default Counter;
```
