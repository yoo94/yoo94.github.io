---
layout: post
title: "js arrow vs function()"
summary: ""
author: yoo94
date: "2023-12-03 15:35:23 +0530"
category: Frontend1
tags:
- JavaScript
- 함수비교
- 화살표함수
- this바인딩
- 함수선언
- ES6
- 프론트엔드
- 객체지향
- 함수형프로그래밍
keywords: JavaScript, 화살표 함수, 일반 함수, function vs arrow, this 바인딩, lexical scope, 함수 선언 방식, ES6 문법, 객체 메서드, 함수 호출 컨텍스트, 함수형 프로그래밍, 코드 간결성
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/arrow-func/
---

#### 일반 함수 (Function Declaration)

전통적인 방식의 함수 선언.
this 키워드가 함수가 호출된 객체를 가리킴.


```js
function sayHello(name) {
  return `Hello, ${name}!`;
}

console.log(sayHello("Alice")); // Hello, Alice!
```

#### 화살표 함수 (Arrow Function)

더 간결한 문법.
this 키워드가 상위 스코프(lexical scope)를 가리킴.

```js
const sayHello = (name) => `Hello, ${name}!`;

console.log(sayHello("Bob")); // Hello, Bob!
```

#### 주요 차이점
##### 문법의 간결함:
- 일반 함수는 function 키워드를 사용하고, 화살표 함수는 =>를 사용
- 화살표 함수는 중괄호 {}와 return 키워드 생략이 가능

##### this 바인딩:

- 일반 함수는 호출된 객체에 따라 this가 동적으로 바인딩.
- 화살표 함수는 this가 정의된 위치의 상위 스코프를 따르므로, this가 변하지 않음.

```js
const person = {
        name: 'Carol',
        regularFunction: function() {
        console.log(this.name); // this는 person 객체를 가리킴
    },
    arrowFunction: () => {
        console.log(this.name); // this는 상위 스코프를 가리킴, 여기서는 전역 객체
    }
};

person.regularFunction(); // Carol
person.arrowFunction();   // undefined (전역 객체에 name이 없기 때문)
```
이렇게 일반 함수와 화살표 함수는 문법의 간결함과 this 바인딩 방식에서 차이가 있어요

