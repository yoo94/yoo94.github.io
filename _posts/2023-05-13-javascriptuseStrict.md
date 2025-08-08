---
layout: post
title:  "useStrict?"
summary: "ES5에선 use strict 를 사용한다. ES6는 글쎼.."
author: yoo94
date: '2023-05-13 15:35:23 +0530'
category: Frontend1
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/useStrict/
---
###### var 키워드 문제

var키워드를 사용하지 않고 변수를 선언하면 글로벌 오브젝트에 설정되어 렉시컬 환경 구조에 맞지 않는다.
ES5에선 use strict 를 사용한다.
ES6에서는 let과 const변수를 사용하여 scope에 제약을 둔다.


---
###### use strict 모드
- js 오류는 아니지만 함정이 될 어떤 일을 오류가 발생하도록 변경하여 제거한다. 디버깅이 효과적이게 된다.
- js 엔진의 최적화 처리를 어렵게 만다는 오류를 수정한다.
- es5에서는 필수라고 볼 수 있다.

with문이나 eval()함수가 대표적으로 오류가 된다.

---
###### node js 코드

js는 single thread 이므로, 동기적으로 하나 하고 끝내고 다음하고 끝내고의 형식으로 처리한다. 그러나 nodejs는 비동기 처리를 한다. 먼저 끝낼 수 있는 작업을 먼저 처리한다는 얘기이다.
context 형태가 효율적이라는 것이다.
