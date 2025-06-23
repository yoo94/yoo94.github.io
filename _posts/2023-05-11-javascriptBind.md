---
layout: post
title:  "기본 자료형"
summary: "자바스크립트 여덟 가지 기본 자료형"
author: yoo94
date: '2023-05-11 14:35:23 +0530'
category: javaScript
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/jsBind/
---
자바스크립트에는 여덟 가지 기본 자료형이 있다.

Number - 원시
bigint - 원시
string - 원시
boolean - 원시
null - 원시
unidefined - 원시
object
symbol

##### Number

```js
let n = 123;
n = 12.345;
```

_숫자형(number type)_ 은 정수 및 부동소수점 숫자(floating point number)

숫자형과 관련된 연산은 다양한데, 곱셈 `*`, 나눗셈 `/`, 덧셈 `+`, 뺄셈 `-` 등

숫자형엔 일반적인 숫자 외에 `Infinity`, `-Infinity`, `NaN`같은 '특수 숫자 값(special numeric value)'이 포함

##### BigInt

내부 표현 방식 때문에 자바스크립트에선 `(253-1)`(`9007199254740991`) 보다 큰 값 혹은 `-(253-1)` 보다 작은 정수는 '숫자형’을 사용해 나타낼 수 없다.

`BigInt`형은 표준으로 채택된 지 얼마 안 된 자료형으로, 길이에 상관없이 정수를 나타낼 수 있습다.
`BigInt`형 값은 정수 리터럴 끝에 `n`을 붙이면 만들 수 있다.

```js
// 끝에 'n'이 붙으면 BigInt형 자료입니다.
const bigInt = 1234567890123456789012345678901234567890n;
```


##### string

자바스크립트에선 문자열(string)을 따옴표로 묶는다.

```js
let str = "Hello";
let str2 = 'Single quotes are ok too';
let phrase = `can embed another ${str}`;
```

1. 큰따옴표: `"Hello"`
2. 작은따옴표: `'Hello'`
3. 역 따옴표(백틱, backtick): `` `Hello` ``
4.
큰따옴표와 작은따옴표는 ‘기본적인’ 따옴표로, 자바스크립트에서는 이 둘에 차이를 두지 않는다.

역 따옴표로 변수나 표현식을 감싼 후 `${…}`안에 넣어주면, 아래와 같이 원하는 변수나 표현식을 문자열 중간에 손쉽게 넣을 수 있다.

```js
let name = "John";

// 변수를 문자열 중간에 삽입
alert( `Hello, ${name}!` ); // Hello, John!

// 표현식을 문자열 중간에 삽입
alert( `the result is ${1 + 2}` ); // the result is 3
```

##### boolean

불린형(논리 타입)은 `true`와 `false` 두 가지 값밖에 없는 자료형

##### null

`null` 값은 지금까지 소개한 자료형 중 어느 자료형에도 속하지 않는 값

. 다른 언어에선 `null`을 '존재하지 않는 객체에 대한 참조’나 '널 포인터(null pointer)'를 나타낼 때 사용
하지만 자바스크립트에선 `null`을 ‘존재하지 않는(nothing)’ 값, ‘비어 있는(empty)’ 값, ‘알 수 없는(unknown)’ 값을 나타내는 데 사용

##### undefined

`undefined` 값도 `null` 값처럼 자신만의 자료형을 형성

`undefined`는 '값이 할당되지 않은 상태’를 나타낼 때 사용


##### object , symbol

객체형을 제외한 다른 자료형은 문자열이든 숫자든 한 가지만 표현할 수 있기 때문에 원시(primitive) 자료형이라 부른다. 반면 객체는 데이터 컬렉션이나 복잡한 개체(entity)를 표현
