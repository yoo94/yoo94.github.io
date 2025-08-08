---
layout: post
title: "Redux의 middleware 미들웨어!"
summary: "미들웨어"
author: yoo94
date: '2024-08-06 20:32:23 +0530'
category: Frontend2
tags:
  - react
  - redux
  - zustand
  - middleware
  - 미들웨어
thumbnail: 
permalink: blog/react-middleware/
---
## 미들 웨어란? 
운영 체제와 응용 소프트웨어의 중간에서 조정과 중개의 역할을 수행하는 소프트웨어 이다.

## react에서의 미들웨어

상태 관리 라이브러리에서 "미들웨어"는 상태 업데이트 과정에 추가적인 기능을 삽입하는 역할을 한다.

### 액션(요청) ---------> 미들웨어 처리 ----------> 상태없데이트

쉽게 이해하면 미들웨어는 상태 업데이트 전후에 추가 작업을 하는 훅이라고 볼 수 있다.

### 리덕스에서 제공하는 미들 웨어

Redux Thunk: 비동기 액션을 쉽게 처리하기 위한 미들웨어.

Redux Logger: 액션과 상태를 로깅하여 디버깅을 돕는 미들웨어.

Redux Saga: 복잡한 비동기 로직을 제너레이터 함수로 관리하는 미들웨어.

Redux Promise: 프로미스를 반환하는 액션을 처리하는 미들웨어.

## 1. Redux Thunk
비동기 액션을 처리하는 가장 기본적인 방법. API 호출과 같은 간단한 비동기 작업에 적합.

```js
// actions.js
export const fetchData = () => {
    return async (dispatch) => {
        dispatch({ type: 'FETCH_DATA_REQUEST' });
        try {
            const response = await fetch('/api/data');
            const data = await response.json();
            dispatch({ type: 'FETCH_DATA_SUCCESS', payload: data });
        } catch (error) {
            dispatch({ type: 'FETCH_DATA_FAILURE', error });
        }
    };
};

// store.js
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(thunk));
```
## 2. Redux Logger
Redux Logger는 디버깅을 위해 액션과 상태 변화를 로그로 기록하는 미들웨어

```js
// store.js
import { createStore, applyMiddleware } from 'redux';
import logger from 'redux-logger';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(logger));

```
## 3. Redux Saga
edux Saga는 복잡한 비동기 로직을 제너레이터 함수를 통해 관리하는 데 유용, 흐름 제어와 같은 고급 비동기 작업

```js
// sagas.js
import { call, put, takeEvery } from 'redux-saga/effects';

function* fetchData() {
    try {
        const response = yield call(fetch, '/api/data');
        const data = yield response.json();
        yield put({ type: 'FETCH_DATA_SUCCESS', payload: data });
    } catch (error) {
        yield put({ type: 'FETCH_DATA_FAILURE', error });
    }
}

function* watchFetchData() {
    yield takeEvery('FETCH_DATA_REQUEST', fetchData);
}

// store.js
import { createStore, applyMiddleware } from 'redux';
import createSagaMiddleware from 'redux-saga';
import rootReducer from './reducers';
import rootSaga from './sagas';

const sagaMiddleware = createSagaMiddleware();
const store = createStore(rootReducer, applyMiddleware(sagaMiddleware));

sagaMiddleware.run(rootSaga);
```
## 4. Redux Promise
Redux Promise는 프로미스를 반환하는 액션을 자동으로 처리하는 미들웨어
단순한 비동기 액션을 더 쉽게 처리

```js
// actions.js
// actions.js
export const fetchData = () => {
    return {
        type: 'FETCH_DATA',
        payload: fetch('/api/data').then(response => response.json())
    };
};

// reducers.js
const dataReducer = (state = {}, action) => {
    switch (action.type) {
        case 'FETCH_DATA_PENDING':
            return { ...state, loading: true };
        case 'FETCH_DATA_FULFILLED':
            return { ...state, loading: false, data: action.payload };
        case 'FETCH_DATA_REJECTED':
            return { ...state, loading: false, error: action.payload };
        default:
            return state;
    }
};

// store.js
import { createStore, applyMiddleware } from 'redux';
import promiseMiddleware from 'redux-promise';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(promiseMiddleware));
```
