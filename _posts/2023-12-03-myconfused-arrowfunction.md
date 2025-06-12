---
layout: post
title:  "js arrow vs function()"
summary: ""
author: yoo94
date: '2023-12-03 15:35:23 +0530'
category: ['myconfused','javaScript']
tags: myconfused, arrow
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/arrow-func/
---

#### 일반 함수 (Function Declaration)

전통적인 방식의 함수 선언.
this 키워드가 함수가 호출된 객체를 가리킴.


```javascript
function sayHello(name) {
return `Hello, ${name}!`;
}

console.log(sayHello('Alice')); // Hello, Alice!
```

#### 화살표 함수 (Arrow Function)

더 간결한 문법.
this 키워드가 상위 스코프(lexical scope)를 가리킴.

```javascript
const sayHello = (name) => `Hello, ${name}!`;

console.log(sayHello('Bob')); // Hello, Bob!
```

#### 주요 차이점
##### 문법의 간결함:
- 일반 함수는 function 키워드를 사용하고, 화살표 함수는 =>를 사용
- 화살표 함수는 중괄호 {}와 return 키워드 생략이 가능

##### this 바인딩:

- 일반 함수는 호출된 객체에 따라 this가 동적으로 바인딩.
- 화살표 함수는 this가 정의된 위치의 상위 스코프를 따르므로, this가 변하지 않음.

```javascript
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

