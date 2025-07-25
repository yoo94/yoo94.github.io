---
layout: post
title: "react hook useRef"
summary: "DOM에 있는 선택 요소에 참조를 걸어 놔서, 바로 접근 할 수 있게 한다."
author: yoo94
date: "2024-02-03 11:35:23 +0530"
category: ["react", "reactHook"]
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-hook-useRef/
---

##### 리렌더링과 무관한 값을 보관하고 싶을때

- 리렌더링이 발생하면 내부변수는 초기화가 된다. 이때 useState를 사용하면 값의 상태를 유지 할 수 있지만 반드시 리렌더링이 발생하게된다.
- 그러나 타이머id나 dom요소 참조와 같은 상황에서는 값의 보관 또는 변경이 필요하지만, 변경이 리렌더링을 유발할 필요가 없다.
- 이럴때 값은 보관하되 리렌더링을 유발하지 않도록 할 수 있다.

####### 언제 사용? : DOM에 있는 선택 요소에 참조를 걸어 놔서, 바로 접근 할 수 있게 한다.
<img src="/blog/postImg/Pasted image 20240505232013.png" alt="Pasted image 20240505232013.png" style="max-width:100%;">

<img src="/blog/postImg/Pasted image 20240505232034.png" alt="Pasted image 20240505232034.png" style="max-width:100%;">

```jsx
import { useRef } from "react";

const selectInput = useRef();

<input ref={selectInput} onchange />;
```

이런 식으로 해 놓고,

```
const inputVal = selectInput.current.value;
```

이런 식으로 사용함

##### validation

<img src="/blog/postImg/Pasted image 20240119134225.png" alt="Pasted image 20240119134225.png" style="max-width:100%;">

옛날 방식으로는 이런식으로 alert창을 띄운다. 그치만 요새 방식은 이런식으로 하지 않는다고 한다.
요새는 포커싱을 주면서 어떤 부분이 안써져있는지 알려준다. 그럴때 어떤 선택자가 포커싱 되어야하는지 알려주는것이 useRef 라는 것이다.

이렇게 import 해주고
<img src="/blog/postImg/Pasted image 20240119134451.png" alt="Pasted image 20240119134451.png" style="max-width:100%;">
사진과 같이 선언하면 저 변수에 ,

###### MutableRefObject

이라는 객체가 저장된다. 이 객체는 DOM요소에 접근하는 기능을 해준다.
<img src="/blog/postImg/Pasted image 20240119134613.png" alt="Pasted image 20240119134613.png" style="max-width:100%;">

이런식으로 input 태그에 ref={선언한 변수}
를 해주면 저 변수를 통해 input 태그에 접근한다.
content 도 마찬가지로
<img src="/blog/postImg/Pasted image 20240123133430.png" alt="Pasted image 20240123133430.png" style="max-width:100%;">

만들어준다.
