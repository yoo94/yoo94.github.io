---
layout: post
title:  "rem과 em의 차이? "
summary: "동적 크기?"
author: yoo94
date: '2024-05-20 19:35:23 +0530'
category: ['myconfused','css']
tags: myconfused, rem, em
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/rem-em/
---

## rem이랑 em의 차이점은?

REM과 EM은 모두 상대적 크기 단위로, 요소의 크기를 부모 요소의 크기에 비례하여 조정한다.

REM은 루트 요소(html)의 폰트 크기를 기준으로 하며, EM은 부모 요소의 폰트 크기를 기준으로 한다.

예를 들어, 루트 요소의 폰트 크기가 16px일 때, 1rem은 16px과 동일한 크기를 나타낸다.

반면, EM은 상속의 개념을 사용하여, 부모 요소의 폰트 크기에 따라 그 크기가 달라진다.

이는 중첩된 요소의 스타일링을 할 때 EM이 REM보다 복잡해질 수 있음을 의미한다.

왜냐하면, 각 요소의 크기가 부모 요소의 크기에 따라 달라지기 때문이다.

따라서, 폰트 크기뿐만 아니라 패딩, 마진 등의 크기를 지정할 때도 REM을 사용하면 더 일관된 레이아웃을 구성할 수 있다.

EM은 컴포넌트의 상대적 크기 조정이 필요할 때 유용하게 사용될 수 있다.

