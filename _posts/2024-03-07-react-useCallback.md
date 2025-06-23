---
layout: post
title:  "react hook useCallback "
summary: "최적화:불필요한 함수 재생성 방지"
author: yoo94
date: '2024-03-07 04:35:23 +0530'
category: ['react','reactHook']
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-hook-useCallback/
---
### 함수 자체를 메모리에 저장하여, 의존성 배열의 값이 변경될때만 함수를 다시 생성한다.
### 특히 자식 컴포넌트에 props로 함수를 전달할 때 불필요한 리렌더링을 방지하는데 유용하다. 

* useMemo는 값을 저장 이건 함수를 저장

###### 언제 사용?  : Memoization된 콜백을 반환할때

즉
```jsx
const onCreate = useCallback(
    () =>{
      setData((data)=>[newItem , ...data])
    },[a,b]
  )
```
```jsx
const add = useCallback(() => x + y, [x, y]);
```

이렇게 되어있으면
1. 첫 번째 인자로 있는 함수를 callback 함수로 인지하여 그대로 반환한다.
2. 두 번째 인자로 있는 값들이 변하지 않으면 저 함수를 그대로 반환한다는 것이다.

#### 함수 메모이제이션

앞서 말한 useCallback 사용법을 정리하자면 아래와 같다. 첫번째 인자로 넘긴 함수를, 두번째 인자로 넘긴 의존성 배열내의 값이 변경되기 전까지 저장하고 재사용할 수 있게 해준다.

```js
const memoizedFunction = useCallback(함수, 배열);
```

만약 useCallback을 사용하지 않는다면, 아래와 같은 함수는 컴포넌트가 렌더링 될 때마다 새롭게 생성된다.

```jsx
const sum = () => x + y;
```
하지만, useCallback을 사용하면 컴포넌트가 다시 렌더링 되더라도, 해당 함수가 의존하고 있는 값들이 바뀌지 않는다면 함수를 새로 생성하지 않고 기존 함수를 계속 반환한다.

```jsx
const add = useCallback(() => x + y, [x, y]);
```

```jsx
import './App.css'
import Header from './components/Header'
import Editor from './components/Editor'
import List from './components/List'
import { useRef,useReducer,useCallback} from 'react'

function reducer (state, action) {
  switch(action.type){
    case 'CREATE':
      return [action.data, ...state];
    case 'UPDATE':
      return state.map((item)=>{
          return item.id === action.targetId? {...item,isDone : !item.isDone}:item
        });
    case 'DELETE':
      return state.filter((item)=>{
        return item.id !== action.targetId
      });
    default: return state;
  }
}

function App() {
  const [todos,dispatch] = useReducer(reducer,[]);
  const idRef = useRef(0);

  // const onCreate=(content)=>{
  //   dispatch({
  //     type:"CREATE",
  //     data : {
  //         id:idRef.current++,
  //         isDone:false,
  //         content: content,
  //         date: new Date().getTime(),
  //     },
  //   })
  // }
// 이 함수들은 리렌더링 되도 이제 다시 선언 되지않고 그전에 있던 함수로 대체되나.
  const onCreate=useCallback((content)=>{
    dispatch({
      type:"CREATE",
      data : {
          id:idRef.current++,
          isDone:false,
          content: content,
          date: new Date().getTime(),
      },
    })
  },[])

  const onUpdate = useCallback((targetId)=>{
    dispatch({
      type:"UPDATE",
      targetId:targetId
    })
  },[])

  const onDelete = useCallback((targetId)=>{
    dispatch({
      type:"DELETE",
      targetId:targetId
    })
  },[])

  return (
    <div className='App'>
      <Header />
      <Editor onCreate={onCreate}/>
      <List todos={todos} onUpdate={onUpdate} onDelete={onDelete}/>
    </div>
  )
}
export default App;
```


#### 함수 동등성

자바스크립트에서 함수는 객체로 취급이 되기때문에, 함수를 동일하게 만들어도 메모리 주소가 다르면 다른 함수로 간주한다. 바로 메모리 주소에 의한 참조 비교가 일어나기 때문인데, 콘솔창에서 아래와 같이 동일한 코드의 함수를 작성하시고 `===` 연산자로 비교를 해보면 `false`가 반환된다.

```jsx
 const add1 = () => x + y;
undefined
 const add2 = () => x + y;
undefined
 add1 === add2
false
```

만약 특정 함수를 다른 함수의 인자로 넘기거나, 자식 컴포넌트의 props로 넘길 때 함수의 참조가 달라서 예상하지 못한 성능 문제가 생길 수 있다.
이 경우, useCallback을 이용해 함수를 특정 조건이 변경되지 않는 이상 재생성하지 못하게 제한하여 함수 동등성을 보장할 수 있다. (만약 리액트가 함수가 동등하지 않다고 판단한다면 상황에 따라 성능이 악화되거나, 무한루프에 빠지는 등의 문제를 겪을 수 있다.)

```jsx
import React, { useState, useEffect } from "react";

function Profile({ id }) {
  const [data, setData] = useState(null);

  const fetchData = useCallback(
    () =>
      fetch(`https://test-api.com/data/${id}`)
        .then((response) => response.json())
        .then(({ data }) => data),
    [id]
  );

  useEffect(() => {
    fetchData().then((data) => setData(data));
  }, [fetchData]);

  // ...
}
```

- 이렇게 useCallback 훅을 사용하면, 컴포넌트가 다시 렌더링 되더라도 `fetchData` 함수의 참조값을 동일하게 유지시킨다.
- 따라서, useEffect에 의존성 배열 값에 있는 `fetchData` 함수는 id 값이 변경되지 않는 한, 재호출되지 않는다.
