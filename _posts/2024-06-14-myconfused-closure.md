---
layout: post
title:  "js closure 클로저란?"
summary: ""
author: yoo94
date: "2024-06-14 15:35:23 +0530"
category: Frontend2
tags: myconfused, closure
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/closure/
---

## 클로저란?
클로저는 자바스크립트의 고급 주제 중 하나로, 함수와 그 함수가 선언된 렉시컬 환경의 조합을 의미한다. 
이는 자바스크립트에서 매우 강력한 기능을 제공하며, 데이터를 은닉하고 캡슐화하는 데 유용하게 사용된다.
클로저는 내부 함수가 외부 함수의 스코프에 접근할 수 있게 해주며, 
외부 함수의 실행이 끝난 후에도 외부 함수의 변수에 접근할 수 있게 한다.
이러한 특성 때문에 클로저는 모듈 패턴, 콜백 함수, 고차 함수 등 다양한 곳에서 활용된다.
```js

const myModule = (function() {
let privateVariable = 'I am private';
return {
getPrivateVariable: function() {
return privateVariable;
}
};
})();
console.log(myModule.getPrivateVariable());  // 출력: I am private```
```

즉시 실행 함수 표현(IIFE): (function() { ... })()의 형태로 정의된 함수는 즉시 실행된다. 
이 함수 내에서 정의된 변수 privateVariable은 외부에서 접근할 수 없다.
private 변수: privateVariable은 함수 스코프 내에서만 접근 가능한 변수로, 외부에서 직접 접근할 수 없다.
공개 메서드: getPrivateVariable 메서드는 privateVariable을 반환하는 함수를 객체로 반환한다. 
이 객체는 외부에서 접근 가능한 형태로 반환되므로, myModule.getPrivateVariable()을 호출하면 privateVariable의 값을 얻을 수 있다.
