---
layout: post
title:  "js 이벤트 위임이란(event delegation)"
summary: "자바스크립트 이벤트 위임이란?"
author: yoo94
date: '2024-07-17 20:35:23 +0530'
category: Frontend2
tags:
- JavaScript
- 이벤트위임
- 이벤트버블링
- 이벤트캡처링
- DOM이벤트
- 프론트엔드
- event delegation
- event propagation
- 이벤트핸들링
- myconfused
keywords: JavaScript, 이벤트 위임, event delegation, 이벤트 버블링, 이벤트 캡처링, event.target, event.currentTarget, event.stopPropagation, event.stopImmediatePropagation, DOM 이벤트 흐름, 이벤트 전파, 이벤트 핸들링 최적화, 성능 개선
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/event-delegation/
---
update : 버블링 캡처링에 관한 추가 정보

## 이벤트 위임이란?
js에서는 사용자의 액션에 의해 이벤트 발생 시 자식 엘리먼트에서 발생하는 이벤트를 버블링으로 인해 부모 엘리먼트에서도 감지 할 수 있다. 
이러한 방식을 이용해 자식에서 하나하나 하는것이 아닌 부모에서 한꺼번에 처리하기위해 부모에게 이벤트를 위임하는 것이 이벤트 위임이다.

- 버블링 : 특정 이벤트가 상위개념으로 전달되어 가는 특성

- 캡처링 : 버블링과 반대방향 탐색, 옵션을 따로 설정해야함

캡처링 단계 – 이벤트가 하위 요소로 전파되는 단계
타깃 단계 – 이벤트가 실제 타깃 요소에 전달되는 단계
버블링 단계 – 이벤트가 상위 요소로 전파되는 단계

## 프로세스
이벤트가 발생하면 이벤트가 발생한 가장 안쪽 요소가 '타깃 요소(event.target)'가 된다.
이벤트는 document에서 시작해 DOM 트리를 따라 event.target까지 내려간다. (캡처링)
이후 타깃 요소에 설정된 핸들러가 호출된다.
이후엔 이벤트가 event.target부터 시작해서 다시 최상위 노드까지 전달되면서 각 요소에 on<event>로 할당한 핸들러와 addEventListener로 할당한 핸들러를 동작시킴.
### 예
HTML → BODY → FORM → DIV (캡처링 단계, 첫 번째 리스너)
P (타깃 단계, 캡쳐링과 버블링 둘 다에 리스너를 설정하게되면 두 번 호출.)
DIV → FORM → BODY → HTML (버블링 단계, 두 번째 리스너)

### event객체
각 핸들러는 아래와 같은 event 객체의 프로퍼티에 접근할 수 있다.

event.target – 이벤트가 발생한 가장 안쪽의 요소
event.currentTarget (=this) – 이벤트를 핸들링 하는 현재 요소 (핸들러가 실제 할당된 요소)
event.eventPhase – 현재 이벤트 흐름 단계(캡처링=1, 타깃=2, 버블링=3)

핸들러에서 event.stopPropagation()을 사용해 이벤트 버블링을 멈출 수 다.
지금은 상위 요소에서 이벤트가 어떻게 쓰일지 확실치 않더라도, 추후에 버블링이 필요한 경우가 생기기 때문에 권장하지 않는다.

##### event.stopImmediatePropagation()
event.stopPropagation()은 위쪽으로 일어나는 버블링은 막아주지만, 다른 핸들러들이 동작하는 건 막지 못한다.

버블링을 멈추고, 요소에 할당된 다른 핸들러의 동작도 막으려면 event.stopImmediatePropagation()을 사용해야 한다. 
이 메서드를 사용하면 요소에 할당된 특정 이벤트를 처리하는 핸들러 모두가 동작하지 않는다.

간단하게 이렇게 생각하자
//이벤트 상위 전파 중단
event.stopPropagation();

//이벤트 상위, 현재 레벨에 걸린 다른 이벤트 또한 동작 중단
event.stopImmediatePropatation();
