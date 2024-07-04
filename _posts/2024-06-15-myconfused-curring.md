---
layout: post
title:  "js curring?"
summary: "커링이란 무엇인가"
author: yoo94
date: '2024-06-15 15:35:23 +0530'
category: ['myconfused','javaScript']
tags: myconfused, curring
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: /blog/curring/
---

### 커링이란?
커링은 인자를 여러개 받는 함수를 분리하여, 인자를 하나씩만 받는 함수의 체인으로 만드는 방법이다

인자가 많아지거나 재사용의 필요성이 느껴질 경우 커링 기법은 이와 같이 많은 도움이 될 수 있다.또한 재사용성이 증가한다.
```javascript
// 커링을 사용한 함수 

const currying = a => b => c => a*b*c; console.log(currying(1)(2)(3)); 
// 인자 값 고정으로 재사용성 높여보기 
const alwaysMultiple2 = currying(1)(2); console.log(alwaysMultiple2(3)); 
// 결과 값 // 6 // 6

```


```javascript
const curry = (func) => {
return curried = (...args) => {
if (args.length >= func.length) {
return func.apply(null, args);
} else {
return (...args2) => {
return curried.apply(null, args.concat(args2));
}
}
};
}

const mul = (a, b, c) => {
return a*b*c;
}

const curriedSum = curry(mul);

console.log(curriedSum(1, 2, 3) ); // 6, 보통때 처럼 단일 callable 형식으로 호출하기
console.log(curriedSum(1)(2,3) ); // 6, 첫 번째 인수를 커링하기
console.log(curriedSum(1)(2)(3) ); // 6, 모두 커링하기
```

