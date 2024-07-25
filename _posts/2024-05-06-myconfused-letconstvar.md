---
layout: post
title:  "let const var 차이점"
summary: "스코프의 차이?"
author: yoo94
date: '2024-05-06 17:35:23 +0530'
category: ['myconfused','javaScript']
tags: myconfused, let, const, var
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/let_const_var/
---

## var
Var는 함수 스코프를 가진다. 
변 수가 선언된 함수 내에서만 지역변수로 작동하고 함수 외부에서는 전역 변수로 작동한다(window 객체의 속성으로 추가된다)

## let / const
Let과 const는 블록스코프를 가지며 {}중괄호로 둘러싸인 블록 내에서만 유효하다

let과 const는 블록 스코프를 가지기 때문에,
글로벌 스코프에서도 해당 변수들은 글로벌 객체의 속성으로 추가되지 않아 글로벌 네임스페이스를 오염시키지 않는다. 
글로벌 변수를 사용할 때 발생할 수 있는 충돌을 방지하고, 코드의 모듈성을 높이는 데 기여한다.

### 호이스팅과의 관련
Var로 선언된 변수는 호이스팅되어 함수나 전역 스코프의 최상단으로 끌어올려진다.
반면 let과const는 호이스팅은 되지만, 선언 전에 접근할 수 없는 일시적 사각지대를 가진다.

 
호이스팅은 자바스크립트에서 변수와 함수선언을 코드를 실행하기 전에 메모리에 저장하히야 코드의 최상단으로 끌어올리는 동작을 말한다.
Var는 undefined로 초기화되며, 이후 값이 할당된다. 그래서 var로 선언된 변수는 선언 전에도 접근할 수 있다.

Let과 const는 초기화 되지않고 실행하다가 도달했을 때 초기화되기 때문에 접근하려하면 참조에러가 발생한다.

### let과 const의 차이
const는 let과 유사하게 블록 스코프를 가지지만, 재할당이 불가능하다. 
이는 const로 선언된 변수는 초기화 시 할당된 값이 변경될 수 없다는 것을 의미한다. 
왜냐하면 const는 변수의 값이 변경되는 것을 방지하기 위해 설계되었기 때문이다.

### 정리
var는 함수 스코프와 호이스팅의 특성을 가지며, 글로벌 객체의 속성으로 추가됩니다. 
let과 const는 블록 스코프를 가지며, const는 재할당과 재선언이 불가능하다.
