---
layout: post
title:  "symentic tag?"
summary: "html을 사용하지 왜 시맨틱 태그를 사용해야되냐?"
author: yoo94
date: '2024-05-09 09:35:23 +0530'
category: ['myconfused','webetc']
tags: myconfused, symentic, html
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/symentic-tag/
---

## 시맨틱 태그란?
시맨틱 태그란 의미가 있는 태그를 말한다. 모든 block 영역은 div 태그로, inline 요소는 span 태그와 달리, header, main, footer, section, article과 같은 태그 자체에 의미가 담긴 태그를 말한다.

### 왜 시맨틱 태그를 사용해야 할까?

영역마다 무슨 태그를 써야하는지 생각하는 게 귀찮고 그냥 다 div 태그를 써버리면 되는데 뭐하러 시맨틱 태그를 사용하나?

1 검색엔진 최적화 – 웹사이트를 크롤링할 때 웹사이트의 내부에 담긴 정보를 토대로 사이트를 분석한다. 그럴 때 , 의미있는 태그를 사용하면 좀 더 정확한 구조로 분석이 가능하다.
2. 쉬운 소스코드 구조화 – 브라우저가 웹문서의 소스코드를 보고 어디가 헤더인지 어디가 본문인지 알수 있고, 웹 문서를 분석하는 서비스 같은 것들이 있을 때 용이하다.

3. 코드 가독성 – 여러 사람이 함께 작업을 하면 굳이 클래스를 지정하지 않아도 쉽게 어디가 헤더고 본문인지 알기 쉽다.
   

### 종류
   header: 헤더 영역에 사용하는 태그. 로고 등이 들어있다.
   nav: 네비게이션 바(메뉴) 영역에 사용하는 태그.
   section: article 보다 큰 영역을 나타낼 때 사용하는 태그.
   article: 보통 제목 태그와 문단 태그를 포함하며, 개별 콘텐츠에 사용하는 태그.
   aside: 사이드 영역에 사용하는 태그. 보통 top버튼이나 본문 영역과 별개의 내용을 포함한다.
   footer: 풋터 영역에 사용하는 태그. 회사의 정보 등이 들어있다.
