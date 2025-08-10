---
layout: post
title: "react event handling"
summary: "이벤트핸들러"
author: yoo94
date: "2024-01-17 18:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-event-handling/
---

##### 1. 태그안에 바로 정의

```jsx
const Button = ({ text, color, children }) => {
  return (
    <button
      onClick={() => {
        console.log(text);
      }}
      style={{ color: color }}
    >
      {text} - {color.toUpperCase()}
      {children}
    </button>
  );
};

Button.defaultProps = { color: "black" };
export default Button;
```

위에처럼 태그 안에 바로 정의 해도 되고
아래처럼 이벤트 로직이 길면 빼서해도 된다.

##### 2. 함수로 빼서 정의

```jsx
const Button = ({ text, color, children }) => {
  const onClickButton = () => {
    console.log(text);
  };

  return (
    <button onClick={onClickButton} style={{ color: color }}>
      {text} - {color.toUpperCase()}
      {children}
    </button>
  );
};

Button.defaultProps = { color: "black" };
export default Button;
```

함수 이름만 전달해야지 ()이거 붙여서 하면 안된다.

---

##### 이벤트 객체

리액트에서는 모든 이벤트핸들러 함수에 이벤트 객체라는 것을 제공한다.

```jsx
const onClickButton = (e) => {
  console.log(e);
};
```

위에처럼 e라는 매개변수를 받아서 출력해보면
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240505215910.png" alt="Pasted image 20240505215910.png" style="max-width:auto;; height:auto;">
</div>
이런식으로 이벤트 객체가 반환되어있다.

이것이 바로 합성 이벤트 객체이다.
브라우저가 너무 많아서 동작이 조금씩 다 다르다.
크롬,엣지,파이어 폭스 등등. 이벤트 객체들도 브라우저 마다 조금씩 다르기 때문에 브라우저 별로 스펙이달라서 발생하는 문제를

###### cross browsing lssue 라고 한다.

여러 브라우저들의 규격을 통합해서 만들어 놓은 것이

##### 합성이벤트라고 하는 것이다.
