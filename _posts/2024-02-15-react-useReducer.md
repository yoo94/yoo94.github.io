---
layout: post
title:  "react hook useReducer"
summary: "같은 state를 변화 시키는데, 여러 함수가 여기저기 선언되어 있을 때 묶음으로 만들기 위해 사용"
author: yoo94
date: '2024-02-15 12:35:23 +0530'
category: react
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-hook-useReducer/
---
<img src="/blog/postImg/Pasted image 20240506161949.png" alt="Pasted image 20240506161949.png" style="max-width:100%;">
<img src="/blog/postImg/Pasted image 20240506162047.png" alt="Pasted image 20240506162047.png" style="max-width:100%;">
<img src="/blog/postImg/Pasted image 20240506162035.png" alt="Pasted image 20240506162035.png" style="max-width:100%;">

###### 언제 사용?  : 같은 state를 변화 시키는데, 여러 함수가 여기저기 선언되어 있을 때 묶음으로 만들기 위해 사용
<img src="/blog/postImg/Pasted image 20240204234130.png" alt="Pasted image 20240204234130.png" style="max-width:100%;">
이런 식으로, 상태를 변화 시켜야 하는 것들이 있으면  한 곳에 다 때려 박는 로직은 좋은 로직 이 아니다.
<img src="/blog/postImg/Pasted image 20240204234233.png" alt="Pasted image 20240204234233.png" style="max-width:100%;">
이런 식으로 따로 빼서 useReducer안에 담아서 사용하면 더 좋다.

비 구조 할당으로 사용하며, 설명하면,

```jsx

// 변환기 역할, 상태를 실제로 변환하는 함수 컴포넌트 안에서 할 필요없이 밖에서 가능함
function reducer(state,action){
	if(action.type === 'INCREASE'){
		return state + action.data
	}
}
//첫번째 인자 count는 - state이다.
//두번째 인자 dispatch - 상태를 변화시키는 액션을 발생시키는 함
const [state,dispatch] = useReducer(reducer,1)
// reducer - 상태 변화가 있어야 한다는 사실을 알리는 발송함수
//useReducer() 이 안에는 반드시 reducer가 반드시 필요하다. 두번째 인자를 처리해주는 함수이다.
// 그리고 1 은 count 인자의 초기값이다.

const onClickFunc =()=>{
	// 인자로 상태가 어떻게 변화되길 원하는지에 대한 액션 객
	dispatch({
		type : 'INCREASE',
		data: 1,
	})
}

```

1. 버튼을 누르면 dispatch가 실행된다. 이때 전달된 객체를 action 객체라고 하고 action 객체는 state와 함께 reducer 로 전달된다.
2.  reducer에서 첫 번째로는 상태가 바뀌어야 할 state의 최신 값을 받게 되고, 두 번째로는 전달된 action 객체를 받게 된다.
3.  reducer에서는 받은 값들로 state를 변경하여 반환한다.
