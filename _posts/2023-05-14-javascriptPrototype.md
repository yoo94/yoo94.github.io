---
layout: post
title:  "상속과 프로토타입?"
summary: "상속과 관련하여, JavaScript에는 객체라는 하나의 구조만 있다."
author: yoo94
date: '2023-05-14 17:35:23 +0530'
category: javaScript
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/javascriptPrototype/
---
상속과 관련하여, JavaScript에는 객체라는 하나의 구조만 있다. 각 객체에는  **프로토타입**이라는 다른 객체에 대한 링크를 보유하는 비공개 속성이 있다

클래스는 현재 널리 채택되어 JavaScript의 새로운 패러다임이 되었지만, 클래스는 새로운 상속 패턴을 가져오지 않는다

그 프로토타입 객체도 자신만의 프로토타입을 가지고 있으며, 프로토타입으로  `null`을 가진 객체에 도달할 때까지 이 연결은 계속된다.
#### 프로토타입 체인을 이용한 상속

객체의  `[[Prototype]]`을 지정하는 방법에는 여러 가지가 있으며,  {__proto__: ... } 구문이 표준

```js
const o = {
  a: 1,
  b: 2,
  // __proto__는 [[Prototype]]을 설정합니다.
  // 여기에 다른 객체 리터럴로 지정되어 있습니다.
  __proto__: {
    b: 3,
    c: 4,
  },
};
```



```js
const o = {
  a: 1,
  b: 2,
  // __proto__는 [[Prototype]]을 설정합니다.
  // 여기에 다른 객체 리터럴로 지정되어 있습니다.
  __proto__: {
    b: 3,
    c: 4,
    __proto__: {
      d: 5,
    },
  },
};

// { a: 1, b: 2 } ---> { b: 3, c: 4 } ---> { d: 5 } ---> Object.prototype ---> null

console.log(o.d); // 5
```

##### 메서드 상속

상속된 함수가 실행 될 때,  [`this`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this)  값은 함수가 자체 속성인 프로토타입 객체가 아니라 상속 객체를 가리킵니다.

```js
const parent = {
  value: 2,
  method() {
    return this.value + 1;
  },
};

console.log(parent.method()); // 3
// 이 경우 parent.method를 호출할 때, 'this'는 부모를 가리킵니다.

// 자식은 부모로부터 상속받는 객체입니다.
const child = {
  __proto__: parent,
};
console.log(child.method()); // 3
// child.method가 호출되면, 'this'는 자식을 가리킵니다.
// 자식이 부모의 메서드를 상속받을 때,
// 자식에서 'value' 속성을 찾습니다. 그러나 자식은 'value'라는 자체 속성이 없기 때문에,
// 해당 속성은 [[Prototype]]에서 찾을 수 있으며, 이는 parent.value입니다.

child.value = 4; // 자식의 속성 'value'에 값 4를 할당합니다.
// 이 코드는 부모의 'value' 속성을 숨깁니다.
// 자식 객체는 이제 다음과 같습니다.
// { value: 4, __proto__: { value: 2, method: [Function] } }
console.log(child.method()); // 5
// Since child now has the 'value' property, 'this.value' means
// 자식은 이제 'value' 속성을 가지므로 'this.value'는 child.value를 의미합니다.
```

#### 생성자

모든 인스턴스가 동일한 몇가지 동일한 속성을 공유하는 경우

```js
const boxPrototype = {
  getValue() {
    return this.value;
  },
};

const boxes = [
  { value: 1, __proto__: boxPrototype },
  { value: 2, __proto__: boxPrototype },
  { value: 3, __proto__: boxPrototype },
];
```

```js
// 생성자 함수
function Box(value) {
  this.value = value;
}

// Box() 생성자에서 생성된 모든 속성
Box.prototype.getValue = function () {
  return this.value;
};

const boxes = [new Box(1), new Box(2), new Box(3)];
```
생성자는  [`new`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/new)로 호출되는 함수입니다.

위 생성자 함수는  [classes](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes)에서 다음과 같이 다시 작성할 수 있습니다.

```js
class Box {
  constructor(value) {
    this.value = value;
  }

  // 메서드는 Box.prototype에 생성됩니다.
  getValue() {
    return this.value;
  }
}
```

아래처럼 재할당이 가능하지만 하지 않는 것이 좋다.

```js
function Box(value) {
  this.value = value;
}
Box.prototype.getValue = function () {
  return this.value;
};
const box = new Box(1);

// 인스턴스가 이미 생성된 후, `Box.prototype`을 변경합니다.
Box.prototype.getValue = function () {
  return this.value + 1;
};
box.getValue(); // 2
```

