---
layout: post
title:  "javaScript Classes"
summary: "메서드, 생성자"
author: yoo94
date: '2024-07-18 16:35:23 +0530'
category: DevLog
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/javascript-class/
---

#### class는 객체를 만드는 특별한 함수이다. class로 만든 객체는 인스턴스 객체라고한다.

class에는 constructor와 메서드를 정의 할 수 있다.
constructor는 인스턴스를 만들 때, 그안에 값들을 초기화해준다.

메서드는 생성방식이 여러가지이다.

1. 클래스 선언 내부에 메서드 정의
```js
class MyClass {
constructor(name) {
this.name = name;
}

// 메서드 정의
sayHello() {
console.log(`Hello, ${this.name}!`);
}
}

const myInstance = new MyClass('Alice');
myInstance.sayHello(); // Hello, Alice!
```
2. 프로토타입을 사용하여 메서드 추가
```js
class MyClass {
constructor(name) {
this.name = name;
}
}

MyClass.prototype.sayHello = function() {
console.log(`Hello, ${this.name}!`);
};

const myInstance = new MyClass('Bob');
myInstance.sayHello(); // Hello, Bob!
```
3. ES6 화살표 함수를 사용한 메서드 추가
```js
class MyClass {
constructor(name) {
this.name = name;
// 화살표 함수로 메서드 정의
this.sayHello = () => {
console.log(`Hello, ${this.name}!`);
};
}
}

const myInstance = new MyClass('Charlie');
myInstance.sayHello(); // Hello, Charlie!
```
4. 클래스 필드 문법을 사용하여 메서드 추가
```js
class MyClass {
name = '';

constructor(name) {
this.name = name;
}

// 클래스 필드로 메서드 정의
sayHello = () => {
console.log(`Hello, ${this.name}!`);
};
}

const myInstance = new MyClass('Dave');
myInstance.sayHello(); // Hello, Dave!
```
5. 동적으로 메서드 추가
   객체를 생성한 후 동적으로 메서드를 추가할 수도 있습니다.

```js
class MyClass {
constructor(name) {
this.name = name;
}
}

const myInstance = new MyClass('Eve');


// 동적으로 메서드 추가
myInstance.sayHello = function() {
console.log(`Hello, ${this.name}!`);
};
myInstance.sayHello(); // Hello, Eve!
```
### 위의 방법들은 모두 프로토타입 메서드를 생성한다.

##static 메서드
정적 메서드 선언 및 호출
static 키워드를 사용하여 선언된 메서드는 클래스 자체의 메서드가 되며, 클래스의 인스턴스가 아닌 클래스 이름을 통해 호출됩니다

#### 프로토타입 체인에서의 차이
정적 메서드는 클래스 자체에 속하고, 프로토타입 체인에 속하지 않습니다. 이를 확인하기 위해 객체의 프로토타입 체인을 살펴볼 수 있습니다.

```js
class MyClass {
static staticMethod() {
console.log('This is a static method');
}

instanceMethod() {
console.log('This is an instance method');
}
}

MyClass.staticMethod(); // This is a static method

const myInstance = new MyClass();
myInstance.instanceMethod(); // This is an instance method
// myInstance.staticMethod(); // 에러: myInstance.staticMethod는 함수가 아닙니다.
```


## 잠깐 그럼 생성자 안에랑 밖이랑 메서드는 어떤 차이가 있을까?
둘다 프로토타입 메서드를 정의하는 것이다.
class에 묶어서 정의하려면 static을 사용하면 된다.

