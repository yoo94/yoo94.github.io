---
layout: post
title:  "nodejs 시작부터 모듈 사용까지"
summary: "nodejs 시작부터 모듈 사용까지"
author: yoo94
date: '2023-05-03 16:35:23 +0530'
category: Backend_infra
tags: nodejs
keywords: nodejs
thumbnail: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTogwU6U5z0Zf2lUxTE72JAKxVd52klwPe-Q&s
permalink: blog/nodejs_init/
---
#### 시작
nodejs.org/ko/
에서 lts버전을 설치 한다.

```powershell
node -v
```
위의 명령어로 설치 확인

```powershell
 npm -v
```
npm은 노드js를 설치하면 자동으로 같이 설치되는 노드 패키지 매니저이다.

예를 들어서 index.js 를 실행하고 싶다면
터미널에서
```powershell
node index.js
```
를 사용하면 실행이 된다.

---
#### 작동
calc.js
```js
const add =(a,b)=> a+b;
const sub=(a,b)=> a-b;

module.exports ={
	moduleName:"calc module",
	add: add,
	sub: sub,
}
```
이런 식으로 export로 내보낼 모듈을 설정하고 나서

index.js
```js
const calc = require("./calc");

calc.add(1,3);
cal.sub(3,5);
```
이런 식으로 하면 calc에 있는 모듈들을 사용할 수 있다.

---

##### 모듈사용
https://www.npmjs.com/
이 사이트에 들어가면 모듈들에 대한 설명을 볼 수 있다.

원하는 모듈을 검색하여 사용 하면 되는데
예를 들어 ramdomcolor라는 모듈을 사용해 보자

![이미지](/blog/postImg/Pasted image 20240111192408.png)

이렇게 install 하는 방법을 명령어로 나와있다.

![이미지](/blog/postImg/Pasted image 20240111192544.png)

설치하게 되면 이렇게
##### package.json에 dependencies
라는 필드가 생기고 설치한 패키지이름과 버전이 써져있다.
여기 버전에 "^0.6.2" 처럼 ^이게 붙어있으면 패키지의 버전이 아니라 이 모듈은 0.6.2 이상의 버전만 설치가 된다라고 명시해 놓은 것이다.

##### package-lock.json
여기에 정확하게 어떤 버전으로 설치 되어있는지 명시되어있다.
##### node_modules
실제 모듈과 관련된 파일을 보관하는


```js
var randomColor = require('randomcolor');
var color = randomColor();
```

위에 처럼 사용하면 되는데, 여기서 require에 경로를 정확하게 명시 안해도 알아서 node_modules에서 찾아서 바라보게 한다.


