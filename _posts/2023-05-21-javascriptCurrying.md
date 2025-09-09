---
layout: post
title:  "커링 (Currying)"
summary: "함수의 재사용성을 높이기 위해 함수자체를 return하는 함수이다."
author: yoo94
date: '2023-05-21 17:35:23 +0530'
category: Frontend2
tags:
- JavaScript
- 커링
- 고차함수
- 함수형프로그래밍
- 함수재사용
- 화살표함수
- 프론트엔드
- 함수조합
keywords: JavaScript, 커링, Currying, 고차 함수, 함수형 프로그래밍, 함수 재사용, 함수 조합, 화살표 함수, 함수 반환, 인자 분리, 재사용성 향상, 유연한 함수 설계
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/Currying/
---
커링 (Currying) 이란, 함수의 재사용성을 높이기 위해 함수자체를 return하는 함수이다.

*커링과 같이 함수 자체를 인자로 받거나 반환하는 함수를 고차함수라고 하기도 한다.
###### 일반함수

```js
function add(num1, num2) {
    console.log(num1 + num2);
}

add(5, 8); // 13

```

###### 커링함수

```js
function add(num1, num2) {
    return num1 + num2;
}

// add() 함수를 return 하는 또 다른 함수를 return
function addPlus(num1) {
    return function(num2) {
        console.log(add(num1, num2));
    }
}

// 화살표 함수로 표현 (위와 동일)
addPlus = num1 => num2 => console.log(add(num1, num2));

// 출력 (파라미터를 하나씩)
addPlus(5)(4); // 9

```

일반함수

```js
// first = 010, tel = 010이후의 8자리
function phoneNum(first, tel) {
	console.log(first + tel);
}

phoneNum(01001230505); // 01001230505
phoneNum(01005253433); // 01005253433

```

커링 함수 활용
```js
function phoneNum(first, tel) {
	console.log(first + tel);
}

const phoneNumber = first => number => phoneNum(first, number);
const phoneNumber010 = phoneNumber('010');

phoneNumber010(01230505); // 01001230505
phoneNumber010(05253433); // 01005253433

```

