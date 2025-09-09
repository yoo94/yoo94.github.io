---
layout: post
title: "js eventloop "
summary: "자바스크립트 모듈 시스템을 사용하는 이유?"
author: yoo94
date: "2024-07-01 19:35:23 +0530"
category: Frontend2
tags:
- JavaScript
- 이벤트루프
- 비동기처리
- 콜스택
- 힙메모리
- 메시지큐
- 논블로킹
- 웹워커
- postMessage
- 프론트엔드
keywords: JavaScript, 이벤트 루프, 비동기 처리, 콜 스택, 힙 메모리, 메시지 큐, 논블로킹, postMessage, 웹 워커, iframe 통신, IndexedDB, XHR, 런타임 모델, 스택 프레임, 중첩 함수thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/eventloop/
---

JavaScript 이벤트 루프는 비동기 작업을 처리하는 메커니즘이다.

개념

1. Call Stack (호출 스택): 현재 실행 중인 함수가 쌓이는 곳.
2. Web APIs: 타이머, DOM 이벤트, HTTP 요청 등 브라우저에서 제공하는 비동기 API.
3. Callback Queue (콜백 큐): 비동기 작업이 완료된 후 실행될 콜백 함수들이 대기하는 곳.
4. Event Loop (이벤트 루프): 호출 스택이 비어있을 때 콜백 큐에서 함수를 가져와 실행하는 반복적인 과정.

```text
  +--------------+
    |  Call Stack  |
    +--------------+
           |
           |    (1) 비동기 작업 호출
           |
           v
    +--------------+
    |  Web APIs    |
    +--------------+
           |
           |    (2) 비동기 작업 완료
           |
           v
    +--------------+
    |Microtask Queue|   <-- 우선 처리
    +--------------+
           |
           |    (3) 이벤트 루프에 의해 호출 스택으로 이동
           |
           v
    +--------------+
    |  Call Stack  |
    +--------------+
           |
           |    (4) 실행
           |
           v
    +--------------+
    | Task Queue   |
    +--------------+
           |
           |    (5) 마이크로태스크가 모두 처리된 후 호출 스택으로 이동
           |
           v
    +--------------+
    |  Call Stack  |
    +--------------+
           |
           |    (6) 실행
           |
```

- Task Queue : setTimeout, setInterval, fetch, addEventListener 와 같이 비동기로 처리되는 함수들의 콜백 함수가 들어가는 큐
  (macrotask queue 는 보통 task queue 라고 부른다)

- Microtask Queue : promise.then, process.nextTick, MutationObserver 와 같이 우선적으로 비동기로 처리되는 함수들의 콜백 함수가 들어가는 큐
  (처리 우선순위가 높음)

#### 동작 과정

1. 호출 스택(Call Stack)\*\*에 함수가 들어와 실행됨.
2. 비동기 작업(예: 타이머, HTTP 요청)이 호출되면, 해당 작업은 Web APIs로 보내짐.
3. 비동기 작업이 완료되면, 콜백 함수가 Callback Queue에 들어감.
4. 이벤트 루프(Event Loop)\*\*는 호출 스택이 비어 있는지 확인하고, 비어 있다면 콜백 큐에서 함수를 가져와 호출 스택에 넣고 실행함.

### web api 종류

DOM : HTML 문서의 구조와 내용을 표현하고 조작할 수 있는 객체
XMLHttpRequest: 서버와 비동기적으로 데이터를 교환할 수 있는 객체. AJAX기술의 핵심.
Timer API: 일정한 시간 간격으로 함수를 실행하거나 지연시키는 메소드들을 제공
Console API : 개발자 도구에서 콘솔 기능을 제공
Canvas API: <canvas> 요소를 통해 그래픽을 그리거나 애니메이션을 만들 수 있는 메소드들을 제공
Geolocation API: 웹 브라우저에서 사용자의 현재 위치 정보를 얻을 수 있는 메소드들을 제공
