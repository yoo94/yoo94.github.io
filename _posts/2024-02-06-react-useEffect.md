---
layout: post
title:  "react hook useEffect"
summary: "모든 또는 특정 state 가 변할 때 마다 , 무엇인가 실행하고 싶으면 사용"
author: yoo94
date: '2024-02-06 15:35:23 +0530'
category: ['react','reactHook']
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-hook-useEffect/
---
## 부수효과, 의존성 배열과 정리함수!

<img src="/blog/postImg/Pasted image 20240506123932.png" alt="Pasted image 20240506123932.png" style="max-width:100%;">

<img src="/blog/postImg/Pasted image 20240506124009.png" alt="Pasted image 20240506124009.png" style="max-width:100%;">

### 필요성
- useState에서는 우리가 내부상태를 변경시키면 컴포넌트함수를 실행시켜 리랜더링 시킨다.
모든 코드를 다시 다 실행시키기 때문에 원치않는 동작을 유도할 수 있어서 나오게 되었다.
- 브라우저의 크기에 따라 반응해야하는 코드를 작성해야 할때, eventListener를 쓰게 되면 리렌더링 할때마다 중첩되기 때문에 서버를 죽이는 상황이 발생한다.

###### 언제 사용?  : 의존성에 넣은 상태가 변할 때 마다 , 무엇인가 실행하고 싶으면 사용
- mount update unmount 때마다 각각 실행할 것들을 할 수 있다.
## useEffect
```jsx
import REact, { useEffect } from "react";

useEffect(()=>{

},[])
```
기본적으로 리액트로 임포트 해줘야하고
1. 첫 번째 인자로는 Callback 함수
2. 두 번째 인자로는 의존성 배열
   을 받게 된다.
3. return은 unmount시에 발생한다.
#### 두 번째 인자에 있는 값이 변화하면 콜백 함수가 실행되는 것이다.
##### 즉 배열 안에 값이 변하는 인자를 넣게 되면 변할 때 마다 callback 함수가 실행된다는 얘기이다!

## Mount
```jsx
useEffect(()=>{
	console.log('mount')
},[])
```
이렇게 빈 배열을 넣으면 mount가 한번 찍히게 된다.
*즉 컴포넌트가 처음 렌더링 될 때, 한번만 실행된다.*

---
## Update
```jsx
useEffect(()=>{
   console.log("update")
})
```
이렇게 두 번째 인자를 안 주게 되면, 해당 컴포넌트에 모든 state 가 변할 때 마다 , callback함수가 실행된다.
*즉 컴포넌트가 렌더링,리렌더링 될 때마다 실행된다.*

#### 만약에, 처음 렌더링을 제외하고 실행하고 싶으면 useRef를 사용한다.
아래 소스처럼 ref를 만들고, 처음 실행 될 때, true로 만들고 retrun을 해버리면 처음 렌더링은 return된다.
```jsx
const isMount = useRef(false);
 useEffect(()=>{
  if(!isMount.current){
    isMount.current = true;
    return
  }
  console.log('update')
 })
```

```jsx
useEffect(()=>{
   console.log("text update")
},[text])

```
이렇게 두 번째 인자에 text라는 state로 선언한 인자를 주게 되면 text의 값이 바뀔 때마다 callback 을 실행한다.
*즉 text state가 상태가 변경 될 때마다 실행된다.*


---
## unmount
```jsx
useEffect(()=>{
    console.log('mount')
	return ()=>{
		console.log('unmount')
	};
},[])
```
이렇게 return 문을 넣으면 컴포넌트가 unmount 될 때 실행하게 된다.

만약 두 번 찍히게 된다면
1. **해당 컴포넌트가 페이지내에서 2번 이상 사용되는 경우**

2. **상위 트리에서 언마운트 혹은 리마운트가 발생하는 경우**
    - 이런 경우는 보통 상위 컴포넌트에서 key가 변경되거나 할 때 발생한다고 하며 해결하기 위해서는 문제가 되는 상위 컴포넌트를 찾기 위해 컴포넌트를 하나씩 거슬러 올라가며 `useEffect`를 통해 테스트해봐야 합니다.

3. **Strict mode를 사용했을 경우**
   위 세개를 의심해볼 필요가 있다.

useState같은 것들은 비동기로 실행되기 때문에, 동기식으로 하고 싶을때 useEffect를 사용하면 된다.
