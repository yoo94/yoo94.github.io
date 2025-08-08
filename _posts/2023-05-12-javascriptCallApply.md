---
layout: post
title:  "call, apply"
summary: "call, apply란 무엇일까?"
author: yoo94
date: '2023-05-12 13:35:23 +0530'
category: Frontend1
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/call_apply/
---
**call, apply**

함수를 호출하는 함수로 첫번째 인자에 this로 세팅하고 싶은 객체를 넘겨 this를 바꾸고 나서 실행한다.

```js
const obj = {name:"fansor"};

const hi = function(hobby){
	console.log(`hello my name is ${this.name}, my hobby is ${hobby}`);
}

hi("soccer") //hello my name is , my hobby is soccer
hi.call(obj,"soccer") //hello my name is fansor, my hobby is soccer
hi.apply(obj,["soccer"]) //hello my name is fansor, my hobby is soccer
```

첫번째 인자를 제외하고 파라미터를 입력하는 방식이 다르다!!

call과 다르게 apply는 두번째 인자부터 모두 배열에 넣어줘야 한다!! 

