---
layout: post
title:  "DOM이란"
summary: ""
author: yoo94
date: '2023-11-16 13:35:23 +0530'
category: ['myconfused','javaScript']
tags: javaScript,DOM
keywords: DOM
thumbnail: 
permalink: blog/DOM/
---
## DOM이란

문서객체모델로 html,xml문서의 인터페이스이다. 
문서 내의 모든 요소를 정의하고 다양한 프로그램들이 페이지의 구조를 읽고 조작 할 수 있도록 api를 제공해준다. 
웹 브라우저와 상호작용하여 문서를 동적으로 조작할 수 있도록 해준다

## DOM의 필요성
•  동적 콘텐츠 변경: JavaScript 등을 사용하여 HTML 문서의 구조, 스타일, 내용을 실시간으로 변경할 수 있다.
•  이벤트 처리: 사용자 입력, 클릭, 폼 제출 등 이벤트에 반응하여 문서를 동적으로 업데이트할 수 있다.
•  데이터 바인딩: JavaScript 객체와 HTML 요소를 연결하여 데이터 변화에 따라 UI를 업데이트할 수 있다.
•  웹 애플리케이션 개발: 복잡한 사용자 인터페이스와 상호작용을 구현하는 데 필수적.

## 왜 계층구조인가
HTML,XML 문서는 본질적으로 중첩된 요소들로 구성된 트리 구조다. 
DOM은 이 구조를 그대로 반영하여 각 요소가 부모-자식 관계를 가진다. 
또한 계층적 구조로 표현하면 탐색 및 조작 용이하고 구조적 정보를 제공하여 검색엔진에 노출이 쉬워진다.

### BOM은?
DOM은 document, 웹 문서에 대한 제어와 변경을 하고 BOM은 window 속성에 속하여 document가 아닌 window를 제어를 한다.
