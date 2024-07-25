---
layout: post
title:  "constructor 생성자 함수에서의 매커니즘"
summary: "차이"
author: yoo94
date: '2024-07-17 17:35:23 +0530'
category: ['myconfused','javaScript']
tags: javaScript
keywords: javaScript,constructor
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/javascript-constructor/
---

기본적인 생성자 함수의 동작
```javascript
function MyClass(name) {
// this 객체는 자동으로 생성됩니다
this.name = name;
// return this; // 명시적으로 작성하지 않아도 암묵적으로 반환됩니다
}

const instance = new MyClass('Alice');
console.log(instance.name); // Alice
```
명시적으로 다른 객체를 반환하는 경우
객체를 반환하는 경우
만약 생성자 함수에서 명시적으로 객체를 반환하면, 그 객체가 반환된다.

```javascript
function MyClass(name) {
this.name = name;
return {}; // 명시적으로 빈 객체를 반환
}

const instance = new MyClass('Alice');
console.log(instance); // {}
console.log(instance.name); // undefined
```
원시 값을 반환하는 경우
생성자 함수가 원시 값을 반환하면, 해당 반환 값은 무시되고 this가 반환된다

```javascript
function MyClass(name) {
this.name = name;
return 'hello'; // 원시 값을 반환
}

const instance = new MyClass('Alice');
console.log(instance.name); // Alice
console.log(instance); // MyClass { name: 'Alice' }
```
결론
생성자 함수에서 명시적으로 객체를 반환하면: 그 객체가 반환된다.
생성자 함수에서 명시적으로 원시 값을 반환하면: 반환 값이 무시되고 암묵적으로 this가 반환된다.
이는 JavaScript의 생성자 함수의 동작 방식이다. 생성자 함수는 기본적으로 새로운 객체를 생성하고, 그 객체를 반환하도록 설계되어 있다. 
### 이 동작은 생성자 함수가 반환하는 값을 덮어쓰는 경우를 제외하고, 기본적으로 this 객체가 반환되도록 한다.
