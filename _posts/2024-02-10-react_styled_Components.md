---
layout: post
title:  "styled Components"
summary: "`styled-components`라는 NPM 패키지명을 가지고 있다"
author: yoo94
date: '2024-02-10 14:35:23 +0530'
category: react
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react_styled_Components/
---

#### 패키지 설치

Styled Components는 `styled-components`라는 NPM 패키지명을 가지고 있다. 따라서 React 프로젝트에 다음과 같이 `npm` 커맨드로 간단히 설치할 수 있다.

```bash
$ npm i styled-components
```

설치 후에 `package.json`에 `styled-components`가 추가된 것을 확인할 수 있다.

```json
  "dependencies": {
    "react": "18.0.0",
    "react-dom": "18.0.0",
    "styled-components": "5.3.5"
  },
```

#### 기본 문법

먼저 위에서 설치한 `styled-components` 패키지에서 `styled` 함수를 임포트한다. `styled`는 Styled Components의 근간이 되는 가장 중요한 녀석인데. HTML 엘리먼트나 React 컴포넌트에 원하는 스타일을 적용하기 위해서 사용된다.

기본 문법은 HTML 엘리먼트나 React 컴포넌트 중 어떤 것을 스타일링 하느냐에 따라 살짝 다르다.

- HTML 엘리먼트를 스타일링 할 때는 모든 알려진 HTML 태그에 대해서 이미 속성이 정의되어 있기 때문에 해당 태그명의 속성에 접근한다.

```javascript
import styled from "styled-components";

styled.button`
  // <button> HTML 엘리먼트에 대한 스타일 정의
`;
```

- React 컴포넌트를 스타일링 할 때는 해당 컴포넌트를 임포트 후 인자로 해당 컴포넌트를 넘기면 된다.

```javascript
import styled from "styled-components";
import Button from "./Button";

styled(Button)`
  // <Button> React 컴포넌트에 스타일 정의
`;
```

두가지 문법 모두 ES6의 Tagged Template Literals을 사용해서 스타일을 정의한다. 그리고 `styled` 함수는 결국 해당 스타일이 적용된 HTML 엘리먼트나 React 컴포넌트를 리턴한다.

예를 들어, 다음과 같이 Styled Components로 작성된 JavaScript 코드는

```javascript
import styled from "styled-components";

styled.button`
  font-size: 1rem;
`;
```

아래 CSS 코드가 적용된 `<button>` HTML 엘리먼트를 만들어낸다고 생각하면 쉽다.

```css
button {
  font-size: 1rem;
}
```

```javascript
import React from "react";
import styled from "styled-components";

const StyledButton = styled.button`
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 1rem;
  line-height: 1.5;
  border: 1px solid lightgray;
  color: gray;
  background: white;
`;

function Button({ children }) {
  return <StyledButton>{children}</StyledButton>;
}
```


##### 가변 스타일링

```javascript
import React from "react";
import styled from "styled-components";

const StyledButton = styled.button`
  padding: 6px 12px;
  border-radius: 8px;
  font-size: 1rem;
  line-height: 1.5;
  border: 1px solid lightgray;

  color: ${(props) => props.color || "gray"};
  background: ${(props) => props.background || "white"};
`;

function Button({ children, color, background }) {
  return (
    <StyledButton color={color} background={background} Î>
      {children}
    </StyledButton>
  );
}
```
