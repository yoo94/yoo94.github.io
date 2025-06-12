---
layout: post
title:  "상속과 프로토타입?"
summary: "작업을 처리하는 이벤트 루프에 기반하고 있다."
author: yoo94
date: '2023-05-19 17:35:23 +0530'
category: javaScript
tags: javaScript
keywords: javaScript
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: blog/javascriptEventloop/
---
JavaScript의 런타임 모델은 코드의 실행, 이벤트의 수집과 처리, 큐에 대기 중인 하위 작업을 처리하는 **이벤트 루프**에 기반하고 있다.

<img src="/blog/postImg/Pasted image 20240328094714.png" alt="Pasted image 20240328094714.png" style="max-width:100%;">


##### 스택

함수의 호출들은 '프레임' 스택을 형성합니다.

```javascript
function foo(b) {
  const a = 10;
  return a + b + 11;
}

function bar(x) {
  const y = 3;
  return foo(x * y);
}

const baz = bar(7); // 42를 baz에 할당
```

위 코드의 실행 순서는 다음과 같습니다.

1. `bar`를 호출할 때, `bar`의 인수와 지역 변수를 포함하는 첫 번째 프레임이 생성됩니다.
2. `bar`가 `foo`를 호출할 때, `foo`의 인수와 지역 변수를 포함하는 두 번째 프레임이 생성되어 첫 번째 프레임의 위로 추가됩니다.
3. `foo`가 반환되면, 맨 위의 프레임 요소를 스택 밖으로 꺼냅니다(`bar` 호출 프레임만 남게 됩니다).
4. `bar`가 반환되면, 스택이 비어있게 됩니다.

인수와 지역 변수는 스택 바깥에 저장되므로, 바깥 함수가 반환된 후에도 계속 존재할 수 있습니다. 중첩 함수에서 지역 변수에 접근할 수 있는 이유가 이것입니다.

##### 힙

객체는 힙에 할당됩니다. 힙은 단순히 메모리의 큰 (그리고 대부분 구조화되지 않은) 영역을 지칭하는 용어입니다.

##### 큐
JavaScript 런타임은 메시지 큐, 즉 처리할 메시지의 대기열입니다. 각각의 메시지에는 메시지를 처리하기 위한 함수가 연결되어 있습니다.
런타임은 대기열에서 가장 오래된 메시지부터 큐에서 꺼내 처리하기 시작합니다. 이를 위해 런타임은 꺼낸 메시지를 매개변수로, 메시지에 연결된 함수를 호출합니다. 함수를 호출하면 해당 함수가 사용할 새로운 스택 프레임이 생성됩니다.
함수 처리는 스택이 다시 텅 빌 때까지 계속됩니다. 그 후, 큐에 메시지가 남아있으면 같은 방법으로 처리를 계속 진행합니다.


#### 이벤트 루프

**이벤트 루프**는 이 기능을 구현할 때 보통 사용하는 방식에서 그 이름을 얻었으며, 대략 다음과 같은 형태입니다.


```javascript
while (queue.waitForMessage()) {
  queue.processNextMessage();
}
```

`queue.waitForMessage()` 함수는 현재 처리할 수 있는 메시지가 존재하지 않으면 새로운 메시지가 도착할 때까지 동기적으로 대기합니다.

##### 다수의 런타임 간 통신

웹 워커나 교차 출처 `iframe`은 자신만의 스택, 힙, 메시지 큐를 가집니다. 서로 다른 두 런타임은 [`postMessage`](https://developer.mozilla.org/ko/docs/Web/API/Window/postMessage) 메서드를 통해 메시지를 보내는 방식으로만 서로 통신할 수 있습니다. 상대가 `message` 이벤트를 수신하고 있을 때, `postMessage`는 상대 런타임에 메시지를 추가합니다.

##### 논 블로킹
다른 많은 언어와 달리 JavaScript는 절대 블로킹 연산을 하지 않습니다. 논 블로킹은 이벤트 루프 모델의 무척 흥미로운 특징으로, 대부분의 입출력 처리가 이벤트와 콜백을 통해 수행되므로, 애플리케이션이 [IndexedDB](https://developer.mozilla.org/ko/docs/Web/API/IndexedDB_API) 질의나 [XHR](https://developer.mozilla.org/ko/docs/Web/API/XMLHttpRequest) 요청의 반환을 대기 중이더라도, 여전히 사용자 입력 등 다른 것들을 처리할 수 있는 것입니다.

