---
layout: post
title:  "reflow repaint"
summary: ""
author: yoo94
date: "2024-07-02 19:35:23 +0530"
category: DevLog
tags: eventloop
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/reflow-repaint/
---

## Reflow(리플로우)
정의: 브라우저가 DOM 요소의 위치와 크기를 다시 계산하는 과정.
발생 시기: DOM 요소의 스타일 변경, 요소 추가/제거, 윈도우 크기 변경 등.
비용: Reflow는 레이아웃 전체를 다시 계산해야 하므로 비용이 많이 듭니다.

## Repaint(리페인트)
정의: 브라우저가 요소의 스타일(색상, 배경, 그림자 등)을 변경하고 다시 그릴 때 발생하는 과정.
발생 시기: CSS로 스타일 속성 변경, 텍스트 내용 변경, 클래스 변경 등.
비용: Repaint는 그리기 작업이므로, Reflow보다 비용이 적습니다.
Reflow와 Repaint의 성능 차이
Reflow는 레이아웃 전체를 다시 계산하므로 비용이 많이 듭니다.
예를 들어, 스크롤이나 윈도우 크기 변경 등 레이아웃에 영향을 주는 상황에서 발생합니다.
Repaint는 스타일 변경 시 발생하며, Reflow보다 비용이 적습니다. 비교적 덜 빈번하게 발생합니다.

```text
  |   브라우저       |
        |   (Browser)      |
        +------------------+
                 |
                 v
        +------------------+
        |   DOM 트리        |
        |   (DOM Tree)      |
        +------------------+
                 |
                 v
        +------------------+
        |   레이아웃 계산   | <--- Reflow (리플로우)
        |   (Layout)       |
        +------------------+
                 |
                 v
        +------------------+
        |   페인팅         | <--- Repaint (리페인트)
        |   (Painting)     |
        +------------------+
                 |
                 v
        +------------------+
        |   화면 출력       |
        |   (Rendering)    |
        +------------------+
```
### 리플로우를 최소화하기 위한 방법
1. 일괄 처리 (Batch Processing):

여러 DOM 요소에 대한 스타일 변경을 한 번에 처리.
예시: 스타일 속성을 클래스에 일괄 적용하여 한 번에 변경.
```js
코드 복사
// 예시: 여러 요소의 스타일을 개별적으로 변경하는 대신 클래스 변경을 통해 한 번에 처리
document.body.classList.add('new-style');
```

2. 가상 요소 사용:

:hover와 같은 가상 클래스를 사용하여 사용자 인터랙션에 반응.
CSS 트리거를 최소화하여 Reflow를 줄임.
```css
/* 예시: 가상 클래스를 사용하여 사용자 인터랙션 처리 */
.button:hover {
background-color: blue;
}
```

3. 크기 고정:

요소의 크기를 고정하여 레이아웃 변경을 최소화.
동적으로 크기가 변경되는 요소에는 주의가 필요.
```css
/* 예시: 요소의 크기를 고정 */
.fixed-size {
width: 100px;
height: 100px;
}
```

