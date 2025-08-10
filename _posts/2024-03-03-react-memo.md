---
layout: post
title: "react React.memo"
summary: "component 불필요한 렌더링 방지"
author: yoo94
date: "2024-03-03 07:35:23 +0530"
category: Frontend2
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/React.memo/
---

###### 언제 사용? : 부모 컴포넌트가 렌더링되어도 자식 컴포넌트에 전달된 props값이 변경되지 않았다면 자식 컴포넌트를 리렌더링 하지 않는다.

![이미지](/blog/postImg/Pasted image 20240204164428.png)
![이미지](/blog/postImg/Pasted image 20240204164443.png)
![이미지](/blog/postImg/Pasted image 20240204164453.png)

```jsx
const MyComponent = React.memo(function MyComponent(props) {
  /* props를 사용하여 렌더링 */
});
```

`React.memo`는 [고차 컴포넌트(Higher Order Component)](https://ko.legacy.reactjs.org/docs/higher-order-components.html)입니다.

##### 결론적으로 이전 props와 같은 props를 주면 리랜딩 하지 않겠다는 말이다.

#### 원래라면 text가 바뀌든 count가 바뀌든 간에 둘다 리랜더링 해서 디버깅을 찍으면 text가 바뀌어도 count에서도 멈춘다. 하지만 React.memo로 감싸면 text가 바뀔 때는 text만 디버깅이 찍힌다.

```jsx
import React , { useState , useEffect} from "react"


const TextView = React.memo(({text})=>{
  useEffect(()=>{})
  return <div>{text}</div>
})

const CountView = React.memo(({count})=>{
  useEffect(()=>{})
  return <div>{count}</div>
});



const OptimizeTest = () =>{
  const [count, setCount] = useState(1);
  const [text, setText] = useState("1");

  return(
    <div style={{padding:50}}>
      <div>
        <h2> count </h2>
        <CountView count={count}/>
        <button onClick={()=> setCount(count+1)}> + </button>
      </div>
      <div>
        <h2> text </h2>
        <TextView text={text}/>
        <input value={text}onChange=e)=>setText(e.target.value)}/>
      </div>
    </div>
  )
};


export default OptimizeTest;
```

###### 저기서 만약 count +1 이 아니라 count 만 있으면 값이 안 바뀌니까 useEffect가 호출 안된다.

예를 들어 header나 footer컴포넌트는 굳이 다시 렌더링 될 필요가 없다.

```jsx
import "./Header.css";
import { memo } from "react";

const Header = () => {
  return (
    <div className="Header">
      <h3>오늘은 😊❤️</h3>
      <h1>{new Date().toDateString()}</h1>
    </div>
  );
};
export default memo(Header);
```

위에 소스처럼 header가 props를 받는다면 그 props가 변경 되지않는한, 다시 렌더링 하지 않는다.
![이미지](/blog/postImg/Pasted image 20240506174909.png)

위 이미지도 마찬가지로 리스트의 아이템컴포넌트인데 하나의 아이템이 변경돼도 다 렌더링 되었기 때문에 이렇게 해 놓으면 해당 아이템만 렌더링 된다.라고 생각 할 수 있지만
그런데 위에처럼 하면 객체를 받게 되는 컴포넌트는 아무리 같은 객체를 받게 되더라도, js에서는 주소가 다르기 때문에 다른 객체로 인식한다. 그래서 렌더링을 다시 하게 된다.
그것이 아래의 개체의 memo이다.

## 객체의 memo

js 는 기본적으로 객체를 비교할 때 얕은 비교를 한다.
객체의 주소를 비교해서 다르다고 판단하는 것이다.
![이미지](/blog/postImg/Pasted image 20240204221451.png)

우리가 바라는 건 아래의 비교이다.
이것이 깊은 비교이다.
![이미지](/blog/postImg/Pasted image 20240204221524.png)

객체는 다르게 비교해야한다.
이때 도움을 줄만한것이

### 첫번째로는

![이미지](/blog/postImg/Pasted image 20240506175600.png)

이렇게 memo에 콜백을 주는 것이고,

두번쨰로는 아래와 같이

### 사용하면 좋은 경우 👍

1. **같은 props로 렌더링이 자주 일어나는 컴포넌트**  
   컴포넌트가 자주 변경되지 않는 정적인 컴포넌트일 때 `React.memo()`를 사용하면 좋다. 이러한 컴포넌트는 동일한 props를 받아 동일한 결과를 렌더링하기 때문에, 재렌더링을 피할 수 있다.
2. **컴포넌트 트리의 상위에 위치해 있거나 자식 컴포넌트가 많은 경우**  
   해당 컴포넌트가 렌더링될 때마다 전체 하위 컴포넌트 트리 / 자식 컴포넌트들이 리렌더링되는 것을 방지할 수 있다.

### 사용하지 않는게 좋은 경우 👎

1. **props가 자주 변경되는 컴포넌트**  
   컴포넌트가 자주 변경되는 동적인 컴포넌트인 경우, `React.memo()`를 사용하면 성능이 저하될 수 있다. 이러한 컴포넌트는 매번 새로운 인스턴스를 생성하고, `render()` 메소드를 호출해야 하므로 `React.memo()`의 메모이제이션 기능을 활용하기도 어렵다.
2. **앱의 크기가 작은 경우**  
   앱의 규모가 작은 경우에도 `React.memo()` 사용은 불필요하다.
