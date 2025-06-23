---
layout: post
title: "호이스팅 hoisting 과 scope"
summary: "호이스팅이랑 스코프가 뭐지ㅣ?"
author: yoo94
date: "2024-05-07 17:35:23 +0530"
category: ["myconfused", "javaScript"]
tags: myconfused, hoisting, scope
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/hoisiting-scope/
---

## 호이스팅이랑 스코프는 무엇인가?

### 호이스팅

호이스팅은 코드에 선언된 변수 및 함수를 끌어올려 유효 범위의 최상단에 선언하는 것을 말한다.

1. 자바스크립트 엔진은 함수선언문 해석 -> 변수 초기화 -> 코드실행 순서로 진행된다.
2. 코드를 실행할 땐 이미 함수 선언문과 변수가 생성되어있는 상태이기 때문에
3. 어디에서든 함수나 변수를 호출할 수 있다.

위의 단계를 호이스팅이라고 한다.

즉 함수 내에서 선언한 함수 범위(function scope)의 변수는 해당 함수의 최상단으로,
함수 밖에서 선언한 전역 범위(global scope)의 전역 변수는 스크립트 단위의 최상단으로 끌어올려지게 된다.

### 스코프

자바스크립트에서 스코프는 변수가 유효할 수 있는 범위, 즉 변수에 접근할 수 있는 범위를 뜻한다.
스코프는 크게 지역 스코프(Local Scope)와 전역 스코프(Global Scope)로 나눌 수 있다.

- Global Scope는 최상단의 스코프로써 이곳에서 선언된 변수(전역 변수)는 어떤 영역에서든 접근이 가능하다.
- Local Scope는 Global Scope에 포함되어 있는 영역으로 이곳에서 선언된 변수(지역 변수)는 전역(Global)에서
  선언된 변수보다 더 높은 우선순위를 가지게 되며 Local Scope에서 선언된 변수는 Global Scope에선 참조가 불가능하다는
  특징을 가지고 있다.
