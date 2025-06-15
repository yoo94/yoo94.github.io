---
layout: post
title: "react recoil이란? 사용방법은?"
summary: "컴포넌트간 데이터 공유를 위해 만들어진 bottom-up 상태관리"
author: yoo94
date: "2024-08-20 13:35:23 +0530"
category: ["react", "myconfused", "reactStatetool"]
tags: react,recoil
thumbnail:
permalink: blog/react-recoil/
---

## 컴포넌트간 데이터 공유를 위해 만들어진 bottom-up 상태관리

### 작고 react 스러운 데이터 흐름 그래프 기반 상태관리도구

- react 내장 상태 관리의 한계 : 내장 상태 관리란=context를 말한다.
- 간소화된 api : boilerplate-free API 를 제공한다.
- 호환성과 유연성

### 핵심 개념 Atoms : useState를 전역변수화 하자

1. Atoms : useState의 글로벌 버전, 외부에서 정의하여 앱 전체에서 공유되는 상태 단위이다. 업데이트 시 해당 atom을 구독하는 모든
   컴포넌트가 새로운 값을 반영하여 리렌더링 된다.
2.
3. Selectors : redux의 selecor와 유사, 기존 atom 값들로 부터 파생된 값을 선언하며, 원본 atom값이 변경 될때마다 자동으로 반응하여
   업데이트된다. 변환과 파생데이터 관리를 가능하게함

```shell
npm install recoil
```

#### cdn도 제공한다.

```text
<script src="https://cdn.jsdelivr.net/npm/recoil@0.0.11/umd/recoil.production.js"></script>
```

#### ESLint

```json
{
  "plugins": ["react-hooks"],
  "rules": {
    "react-hooks/rules-of-hooks": "error",
    "react-hooks/exhaustive-deps": [
      "warn",
      {
        "additionalHooks": "useRecoilCallback"
      }
    ]
  }
}
```

### RecoilRoot

recoil 상태를 사용하는 컴포넌트는 부모 트리 어딘가에 나타나는 RecoilRoot 가 필요하다

```javascript
import React from "react";
import {
  RecoilRoot,
  atom,
  selector,
  useRecoilState,
  useRecoilValue,
} from "recoil";

function App() {
  return (
    <RecoilRoot>
      <CharacterCounter />
    </RecoilRoot>
  );
}
```

### atom 함수를 사용해 생성한다.

Atoms는 어떤 컴포넌트에서나 읽고 쓸 수 있다. atom의 값을 읽는 컴포넌트들은 암묵적으로 atom을 구독한다. 그래서 atom에 어떤 변화가
있으면 그 atom을 구독하는 모든 컴포넌트가 재 렌더링 되는 결과가 발생할 것이다.

```javascript
const textState = atom({
  key: "textState", // unique ID (with respect to other atoms/selectors)
  default: "", // default value (aka initial value)
});
```

컴포넌트가 atom을 읽고 쓰게 하기 위해서는 useRecoilState()를 아래와 같이 사용하면 된다

```javascript
function CharacterCounter() {
  return (
    <div>
      <TextInput />
      <CharacterCount />
    </div>
  );
}

function TextInput() {
  const [text, setText] = useRecoilState(textState);

  const onChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div>
      <input type="text" value={text} onChange={onChange} />
      <br />
      Echo: {text}
    </div>
  );
}
```

### Selector

아톰들을 결합해서 새로운 값을 만들어내는것을 말한다. usememo와 비슷한거같다

```javascript
const charCountState = selector({
  key: "charCountState", // unique ID (with respect to other atoms/selectors)
  get: ({ get }) => {
    const text = get(textState);

    return text.length;
  },
});
```

useRecoilValue() 훅을 사용

```javascript
function CharacterCount() {
  const count = useRecoilValue(charCountState);

  return <>Character Count: {count}</>;
}
```
