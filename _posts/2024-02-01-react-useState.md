---
layout: post
title: "react hook useState"
summary: "화면에서 값이 변하는 것들을 담아두고 관리할 때"
author: yoo94
date: "2024-02-01 18:35:23 +0530"
category: Frontend2
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-hook-useState/
---

##### 클래스 컴포넌트에서 함수형 컴포넌트로의 전황

- 한수형 컨포넌트란 props를 전달받아 JSX로 구성된 virtual DOM element를 반환하는 함수이다.
- 이는 React에서 UI를 선언적으로 표현하는 간결하고 효율적인 방법이다.
- class와 this 그리고 render()를 대신 함수만으로 작성하는 함수형 컴포넌트는 훨씬 단순하고 명확한 코드를 작성할수 있다.
- 초기에는 내부상태를 관리 할 수 없었다. 컴포넌트가 오로지 props를 기반으로 UI를 렌더링하는 무상태 컴포넌트로 작동하게 만들었다.
- 이걸 해결하기위해 나온것이 Hooks이다.
- 이 hook로 인해서 동적인 상태관리가 가능해 졌다.

#### useState

##### 구현 원리

- 클로저의 특성을 활용한다.

```jsx
import React, { useState } from "react";

const Component = () => {
  const [value, setValue] = useState(0);
  setValue(1);
};
export default Component;
```

- useState를 선언한 setValue를 호출하게 되면 value의 값을 바꾸는게 아니라, Component함수를 다시 실행 시킨다. 그래야 새로운 virtual DOM을 반환해서
- 화면이 업데이트 되기 때문이다.
- 그렇다면 setValue를 호출할때는 초기값이 0 인데 어떻게 1로 바꿀수 있을까?
- 컴포넌트 함수가 실행되면, 별도의 저장소가 생성되고 useState가 호출되는 순서대로 값을 기억하고 있는다.
- 그리고 setValue등을 통해 전달된 값으로 저장소의 값을 변경하고 컴포넌트 함수를 재 실행시켜서 저장소에서 최신값을 가지고와 상태가 유지된다.

###### 즉 함수컨포넌트가 실행되면 초기값을 저장소에 보관하고, 상태변경함수를 호출하면 저장소에 값을 바꾼 뒤 함수컴포넌트가 재실행하는 방식으로 상태를 유지한다.

##### 제약조건

- useState 저장소는 호출된 순서대로 기억을 한다. 그래서 조건문이나 반복문 안에서는 선언하면 안된다.
- 불변성을 가지고 있기 때문에 value를 직접적으로 수정해봤자 소용없다. 클로저이기때문에 setValue를 통해서만 바꿔야한다.
- 객체나 배열이 값이라면 불면성을 유지하기위해 spread문법으로만 변경하는것이 좋다.
- {...prevSate, newProperty:value} / [...prevSate, newItem]

##### 프로세스큐와 관계

- 연속해서 요청해도 처리는 마지막 한번에 처리한다.

###### 언제 사용? : 화면에서 값이 변하는 것들을 담아두고 관리할 때

- 부연 설명을 하자면, onChange , onClick 등 뭔가 값이 변하고 그 값을 저장해서 사용해야 할 때 사용한다.

```jsx
import React, { useState } from "react";

const [state, setState] = useState("");

const saveInput = (value) => {
  setState(value);
};

//만약에 input에 넣은 값을 저장하고 사용해야한다면
<input
  onChange={(e) => {
    saveInput(e.target.value);
  }}
/>;
```

1. 첫번째 인자는 상태의 값으로 화면에 출력되는 것이고,
2. 두번째 인자 첫번째 인자를 변화시키는 상태변화 함수로 사용하게 된다.
3. useState(이안에 들어갈 값은) 초기값이라고 보면 된다.

먼저 counter.js를 만들어준다.

```jsx
const Counter = () => {
  return (
    <div>
      <h2>0</h2>
      <button>+</button>
      <button>-</button>
    </div>
  );
};
export default Counter;
```

1. 여기서 바껴야하는 부분은 h2의 0이다.
2. 그렇다면 h2의 상태를 바꾸면 되는것이다.

```jsx
import React, { useState } from "react";
```

위의 리액트 모듈은 useState를 import 해준다음

```jsx
import React, { useState } from "react";

const Counter = () => {
  const [count, setcount] = useState(0);
  return (
    <div>
      <h2>{count}</h2>
      <button>+</button>
      <button>-</button>
    </div>
  );
};
export default Counter;
```

const [count,setcount] = useState(0);
이렇게 적어준다. 이것도 state의 문법이라고 볼 수 있다.
useState를 사용할때는

1. 첫번째 인자는 상태의 값으로 화면에 출력되는 것이고,
2. 두번째 인자 첫번째 인자를 변화시키는 상태변화 함수로 사용하게 된다.
3. useState(이안에 들어갈 값은) 초기값이라고 보면 된다.
