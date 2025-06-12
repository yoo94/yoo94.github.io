---
layout: post
title:  "react context 와 props"
summary: ""
author: yoo94
date: '2023-08-06 11:35:23 +0530'
category: ['react','myconfused']
tags: react,context,props
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-context-props/
---

##### context 란
- 리액트 애플리케이션에서 전역적으로 데이터를 공유하고 관리하는 방법을 제공한다. (간편한 전역 상태 관리 가능)
-  상위 -> 하위 컴포넌트로 데이터 전달 시 속성(props)을 전달하지 않고도 컴포넌트 간 데이터를 공유할 수 있도록 해줌

###### 언제 context를 사용할까?
Context를 사용하면, 중간 계층에 위치하는 엘리먼트에 props를 넘겨주는 작업을 피할 수 있다.
프롭스 드링링을 줄일 수 있다는 말이다.

```jsx
//먼저 사용하려면 context로 값을 내려줄 부모 컴포넌트에서 이렇게 선언해준다.
import { createContext } from 'react'

//부모 컴포넌트에 context 객체를 선언해준다.
export const Context1 = createContext();
export const Context2 = createContext();

//보내줄 context객체를 jsx로 감싸주면 하위 컴포넌트들은 감싼 context 객체를 사용 할 수 있다. context도 객체이기 때문에 바로 넣지는 못하고 Context1.Provider에 value에 넣어준다.
return (
  <div className='App'>
   <Header />
   <Context1.Provider value={data1}>
    <Context2.Provider value={{dataitm1,dataitm2,dataitm3}}}>
     <Editor />
     <List />
    </Context2.Provider>
   </Context1.Provider>
  </div>
 )
```

##### 자식
```jsx

//useContext를 선언해준다.
import { useContext } from 'react'

//data1 처럼 바로 값을 보내준거면 아래와같이 할당
const data1 = useContext(context1);
//data2처럼 객체로 할당 했으면 객체구조할당을 사용하여 할당해준다.
const {dataitm1,dataitm2,dataitm3} = useContext(context2);
```


##### Context <-> Props 차이점

##### Props
전달 방식: 부모 컴포넌트에서 자식 컴포넌트로 명시적으로 전달.
사용 범위: 컴포넌트 간 데이터 전달에 사용.
설정 및 사용: 전달할 때마다 props를 지정해야 함.
###### 장점:
명시적이고 직관적.
컴포넌트 간의 데이터 흐름이 명확.
###### 단점:
깊게 중첩된 컴포넌트에서 Props Drilling 문제가 발생(중간 컴포넌트들이 필요하지 않은 데이터를 전달해야 하는 경우).


##### Context
전달 방식: Context Provider를 통해 트리 전체에 전역적으로 전달.
사용 범위: 전역적이거나 많은 컴포넌트에서 공유해야 하는 데이터에 사용.
설정 및 사용: Provider에서 한 번 설정하면, Consumer나 useContext 훅을 통해 어디서나 접근 가능.

###### 장점:
Props Drilling 문제 해결.
전역 상태 관리에 용이.

###### 단점:
전역 데이터 사용이므로, 관리가 어렵고 남용 시 코드 복잡도가 증가할 수 있음.
데이터의 출처가 불분명해질 수 있음(명시성이 떨어짐).

###### 요약
Props: 컴포넌트 간 명시적으로 데이터를 전달할 때 사용.
Context: 많은 컴포넌트에서 공통적으로 접근해야 하는 데이터를 전역적으로 관리할 때 사용.
