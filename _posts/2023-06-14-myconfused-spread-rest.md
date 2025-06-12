---
layout: post
title:  "js spread, rest, 구조분해할당"
summary: "커링이란 무엇인가"
author: yoo94
date: '2023-06-14 12:35:23 +0530'
category: ['myconfused','javaScript']
tags: myconfused, spread, rest
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/spread-rest/
---

#### Spread 
연산자(...)는 배열이나 객체를 개별 요소로 분해하여 사용할 수 있게 해준다. 배열의 요소를 새로운 배열에 복사하거나 객체의 속성을 새로운 객체에 복사할 때 유용.

예제:

```javascript
// 배열의 Spread
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];
console.log(arr2); // [1, 2, 3, 4, 5]

// 객체의 Spread
const obj1 = {a: 1, b: 2};
const obj2 = {...obj1, c: 3};
console.log(obj2); // {a: 1, b: 2, c: 3}
```

#### Rest 

Rest 연산자(...)는 함수의 매개변수나 배열/객체의 일부 요소를 변수에 할당할 때 사용. 
함수의 인자 목록을 배열로 받을 때나, 배열/객체에서 일부 요소를 분리하고 나머지를 한 변수에 담을 때 유용.

첫번째 예제처럼 몇개의 매개변수를 받을지 모를때 유용하다.
```javascript
// 함수 매개변수에서의 Rest
function sum(...args) {
return args.reduce((acc, cur) => acc + cur, 0);
}
console.log(sum(1, 2, 3)); // 6

// 배열에서의 Rest
const [first, ...rest] = [1, 2, 3, 4];
console.log(first); // 1
console.log(rest); // [2, 3, 4]

// 객체에서의 Rest
const {a, ...restObj} = {a: 1, b: 2, c: 3};
console.log(a); // 1
console.log(restObj); // {b: 2, c: 3}
```

##### 구조분해 할당

구조분해 할당은 배열이나 객체의 속성을 쉽게 추출하여 변수에 할당할 수 있게 해줍니다.

```javascript
// 배열의 구조분해 할당
const numbers = [1, 2, 3];
const [one, two, three] = numbers;
console.log(one); // 1
console.log(two); // 2
console.log(three); // 3

// 객체의 구조분해 할당
const person = {name: 'John', age: 30};
const {name, age} = person;
console.log(name); // John
console.log(age); // 30

// 함수 매개변수에서의 구조분해 할당
function greet({name, age}) {
console.log(`Hello, my name is ${name} and I am ${age} years old.`);
}
greet(person); // Hello, my name is John and I am 30 years old.
```

