---
layout: post
title:  "instance 와 prototype 의 멤버추가"
summary: "차이"
author: yoo94
date: '2024-07-18 16:35:23 +0530'
category: Frontend1
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/javascript-class2/
---
### 결론부터 말하자면 
- 모든 인스턴스가 동일한 메서드를 공유하도록 합니다.
- 클래스 생성자를 사용한 인스턴스 멤버 추가는 각 인스턴스가 고유한 메서드를 가지게 하며, 인스턴스별로 개별적인 동작을 정의할 수 있습니다.

프로토타입을 사용한 메서드 추가
```js
function MyClass(name) {
this.name = name;
}

MyClass.prototype.sayHello = function() {
console.log(`Hello, ${this.name}!`);
};

const instance1 = new MyClass('Alice');
instance1.sayHello(); // Hello, Alice!

```
클래스 문법을 사용한 인스턴스 메서드 추가
```js
class MyClass {
constructor(name) {
   this.name = name;
   this.sayHello = function() {
      console.log(`Hello, ${this.name}!`);
   };
 }
}
const instance1 = new MyClass('Alice');
const instance2 = new MyClass('Bob');

instance1.sayHello(); // Hello, Alice!
instance2.sayHello(); // Hello, Bob!

// 인스턴스마다 고유한 메서드
console.log(instance1.sayHello === instance2.sayHello); // false

```
