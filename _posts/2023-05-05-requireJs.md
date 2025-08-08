---
layout: post
title:  "requireJs란"
summary: "이제는 사장된... 그 라이브러리.."
author: yoo94
date: '2023-05-05 12:35:23 +0530'
category: Frontend1
tags: requirejs
keywords: requirejs
thumbnail: https://avatars.githubusercontent.com/u/1781835?s=280&v=4
permalink: blog/requirejs/
---


#### require js 사용
require js : AMD 기반 스크립트 로더. 자바스크립트 파일/모듈 로더.  
*AMD : 비동기적으로 스크립트를 로딩하기 위한 방법을 정의한 API를 의미.

사용목적 :  
일반적으로 자바스크립트를 하나의 파일로 작성하는 경우가 많다. 그런데 코드가 점점 방대해지면 나중에 관리가 쉽지않다. 이를위해 기능이나 용도별로 여러 파일로 분할하여 사용한다.

##### 모듈 정의와 사용

모듈을 정의하는 기본 형태는 다음과 같다.

```js
// 모듈 정의의 기본 형태
define([ // 의존 모듈들을 나열한다. 모듈이 한 개라도 배열로 넘겨야 한다.  
    'js/util',
    'js/Ajax',
    'js/Event'
], function (util, Ajax, Event) { // 의존 모듈들은 순서대로 매개변수에 담긴다.
    // 의존 모듈들이 모두 로딩 완료되면 이 함수를 실행한다.
    // 초기화 영역
    var i = 0;

    function increase() {
        i++;
    }

    function get() {
      return i;
    }

    // 외부에 노출할 함수들만 반환한다.
    return {
        increase: increase,
        get: get
    };
});


require([  
    'js/foo'
], function (foo) {
    console.log(foo.get()); // 0
    foo.increase();
    console.log(foo.get()); // 1
});

```

로딩 순서가 중요하다면 아래와 같이 require를 중첩해서 사용하는 방법이 있다.


```js
require(['js/first'], function (first) {  
    require(['js/second'], function (second) {
        //
    });    
});
```
