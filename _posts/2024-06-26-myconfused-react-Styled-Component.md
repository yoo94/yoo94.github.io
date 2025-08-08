---
layout: post
title:  "react Styled Component"
summary: "Styled Component를 사용하는 이유"
author: yoo94
date: "2024-06-26 11:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/Styled-Component/
---
### 사용하는 이유
CSS-in-JS: 스타일을 컴포넌트 내에서 정의하여, 스타일과 컴포넌트를 하나의 단위로 관리할 수 있다.
동적 스타일링: React props를 사용하여 동적으로 스타일을 변경할 수 있다.
범위 제한: 각 컴포넌트에 고유한 클래스명을 자동으로 생성하여 CSS 범위를 제한. 이를 통해 스타일 충돌을 방지할 수 있다.
유지 보수성: 스타일과 로직을 같은 파일에 작성하여 유지 보수가 용이.

먼저 styled-components 패키지를 설치해야 한다.

```
npm install styled-components
```

#### 기본 사용법
```js
import React from 'react';
import styled from 'styled-components';

const Container = styled.div`
  width: 100%;
  padding: 20px;
  background-color: lightblue;
`;

const Title = styled.h1`
  color: darkblue;
  text-align: center;
`;

const App = () => (
  <Container>
    <Title>Hello, World!</Title>
  </Container>
);

export default App;
```
#### 동적 사용법
```js

import React from 'react';
import styled from 'styled-components';

const Button = styled.button`
  background-color: ${props => props.primary ? 'blue' : 'gray'};
  color: white;
  font-size: 16px;
  margin: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: ${props => props.primary ? 'darkblue' : 'darkgray'};
  }
`;

const App = () => (
  <div>
    <Button primary>Primary Button</Button>
    <Button>Default Button</Button>
  </div>
);

export default App;
```
#### props로 전달하여 스타일링

```js
import React from 'react';
import styled from 'styled-components';

const Card = styled.div`
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
`;

const Title = styled.h2`
  color: ${props => props.color || 'black'};
`;

const App = () => (
  <div>
    <Card>
      <Title color="blue">Card Title 1</Title>
      <p>This is a card with a blue title.</p>
    </Card>
    <Card>
      <Title color="green">Card Title 2</Title>
      <p>This is a card with a green title.</p>
    </Card>
  </div>
);

export default App;

```
#### scss 사용

```js
import React from 'react';
import styled from 'styled-components';

// 변수 정의
const primaryColor = 'blue';
const secondaryColor = 'gray';

const Button = styled.button`
  background-color: ${primaryColor};
  color: white;
  font-size: 16px;
  margin: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: ${secondaryColor};
  }
`;

const App = () => (
  <div>
    <Button>Styled Button</Button>
  </div>
);

export default App;

```
