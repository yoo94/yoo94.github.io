---
layout: post
title:  "React 모듈과 네스팅"
summary: "모듈과 네스팅"
author: yoo94
date: '2023-05-02 14:38:23 +0530'
category: react
tags: react
keywords: react, module, nesting
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/module_nesting/
---
#### Module

- 모듈은 파일을 분리해서 필요 시점에 필요한 것만 사용하려고 만든것이다.

- 그래서 되도록이면 작아야한다.

- import / export 형태로 사용한다.

- export 대상은 변수, 함수, class, object 이다.

#### 네스팅

- checkbox 같은 컴포넌트는 여러군데에서 쓰니까 독립된 컴포넌트로 정의하고 여기저기서 쓴다.

필요한 컴포넌트에 React JSX콘텐츠를 포함하는 개념이 네스팅이다.

```js
//----- Checkbox.js
import './App.css';
function Checkbox() {
	return (
    	<div>
            <input type="checkbox" id="checkId" /> 
			<label html For="checkId">0</label>
		</div>
        )
	}
//----- App.js 
function App() { 
	return (
		<div className="App">
			<header>
				<h1>체크체크</h1>
			</header>
			<Checkbox/>
		</div>
	)
}
export default App
```

위에 같이 체크박스를 컴포넌트에 포함시켜서 <Checkbox /> 로 불러오는 것이다.

이처럼 재사용성이 높으면 컴포넌트로 분리하여 사용하는것을 고려해야한다.
