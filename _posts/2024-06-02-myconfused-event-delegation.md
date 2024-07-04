---
layout: post
title:  "js 이벤트 위임이란(event delegation)"
summary: "자바스크립트 이벤트 위임이란?"
author: yoo94
date: '2024-06-02 13:35:23 +0530'
category: myconfused
tags: myconfused, event, delegation
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: /blog/event-delegation/
---

## 이벤트 위임이란?
js에서는 사용자의 액션에 의해 이벤트 발생 시 자식 엘리먼트에서 발생하는 이벤트를 버블링으로 인해 부모 엘리먼트에서도 감지 할 수 있다. 
이러한 방식을 이용해 자식에서 하나하나 하는것이 아닌 부모에서 한꺼번에 처리하기위해 부모에게 이벤트를 위임하는 것이 이벤트 위임이다.

- 버블링 : 특정 이벤트가 상위개념으로 전달되어 가는 특성

- 캡처링 : 버블링과 반대방향 탐색, 옵션을 따로 설정해야함
