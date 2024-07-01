---
layout: post
title:  "react hook useState"
summary: "화면에서 값이 변하는 것들을 담아두고 관리할 때"
author: yoo94
date: '2024-02-01 18:35:23 +0530'
category: react
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: /blog/react-hook-useState/
---
###### 언제 사용?  : 화면에서 값이 변하는 것들을 담아두고 관리할 때

- 부연 설명을 하자면, onChange , onClick 등 뭔가 값이 변하고 그 값을 저장해서 사용해야 할 때 사용한다.
```jsx
import React,{useState} from 'react';

const [state,setState] = useState("");

const saveInput = (value) => {
	setState(value)
}

//만약에 input에 넣은 값을 저장하고 사용해야한다면
<input onChange={(e)=>{saveInput(e.target.value)}}/>



```

1. 첫번째 인자는 상태의 값으로 화면에 출력되는 것이고,
2. 두번째 인자 첫번째 인자를 변화시키는 상태변화 함수로 사용하게 된다.
3. useState(이안에 들어갈 값은) 초기값이라고 보면 된다.


먼저 counter.js를 만들어준다.
```jsx
const Counter = ()=>{
  return (
    <div>
      <h2>0</h2>
      <button>+</button>
      <button>-</button>
    </div>
  )
}
export default Counter;
```

1. 여기서 바껴야하는 부분은 h2의 0이다.
2. 그렇다면 h2의 상태를 바꾸면 되는것이다.

```jsx
import React,{useState} from 'react';
```
위의 리액트 모듈은 useState를 import 해준다음

```jsx
import React,{useState} from 'react';

const Counter = ()=>{
  const [count,setcount] = useState(0);
  return (
    <div>
      <h2>{count}</h2>
      <button>+</button>
      <button>-</button>
    </div>
  )
}
export default Counter;
```
const [count,setcount] = useState(0);
이렇게 적어준다. 이것도 state의 문법이라고 볼 수 있다.
useState를 사용할때는
1. 첫번째 인자는 상태의 값으로 화면에 출력되는 것이고,
2. 두번째 인자 첫번째 인자를 변화시키는 상태변화 함수로 사용하게 된다.
3. useState(이안에 들어갈 값은) 초기값이라고 보면 된다.

