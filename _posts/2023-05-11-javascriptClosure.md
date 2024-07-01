---
layout: post
title:  "클로저 (Closure) 란"
summary: "함수가 선언된 어휘적 환경(Lexical Environment)의 조합"
author: yoo94
date: '2023-05-11 15:35:23 +0530'
category: javaScript
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: /blog/Closure/
---
클로저는 함수와 함수가 선언된 어휘적 환경(Lexical Environment)의 조합이다. 즉, 
 **함수 안에 함수를 선언한 환경에서의 관계를 의미한다.

함수안에 함수를 선언한 환경은 내부 함수에서 외부 함수로 지역변수를 접근할 수 있지만 외부 함수의 실행이 끝나고 외부 함수가 소멸된 이후에도 
**내부 함수가 외부 함수의 변수에 접근할 수 있는 것을 의미한다.

발생하는 이유는 자바스크립트는 함수를 리턴하고 리턴되는 함수가 클로저를 형성하기 때문에 접근이 가능합니다. 클로저는 반환된 내부함수가 
 **자신이 선언되었을때의 환경(Lexical Environment)에서의 스코프를 기억하기 때문에 접근이 가능합니다.**
## 2) 클로저는 왜 사용해야 하는것일까?

1. 정보의 접근 제한(캡슐화) - Private Method 를 구성 할 수 있다
- 자바스크립트 내에서는 다른 언어와 달리 메소드를 Private Method 형태로 선언 할 수 있는 기능을 제공하지 않는다.그렇기에 이와 비슷한 형태로 정보의 접근을 제한하는 캡슐화를 클로저 개념을 이용하여 구성 할 수 있다.


2. 상태유지
- 클로저 함수는 외부 함수의 실행이 끝나더라도 외부 함수 내 변수를 사용 할 수 있기에 이러한 특성을 이용하여 특정 데이터를 스코프 안에 두고 계속 최신 상태로 유지하여 사용한다.

3. 전역 변수의 사용 억제 - 모듈화에 유리하다.
- 클로저 함수를 각각의 변수에 할당하면 각자 독립적으로 값을 사용하고 보존할 수 있다.  
  이와 같이 함수의 재사용성을 극대화 함수 하나를 독립적인 부품의 형태로 분리하는 것을 모듈화라고한다.
