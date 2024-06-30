---
layout: post
title:  "반응형 디자인과 미디어 쿼리"
summary: "responsive web design"
author: yoo94
date: '2023-10-29 17:35:23 +0530'
category: webetc
tags: webetc
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/180px-CSS3_logo_and_wordmark.svg.png
permalink: /blog/media_query/
---
## 반응형 웹 디자인
(responsive web design, RWD)이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 디스플레이의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법을 말한다.

웹사이트를 PC용과 모바일용으로 각각 별개로 제작하지 않고, 하나의 공용 웹사이트를 만들어 다양한 디바이스에 대응할 수 있다. PC용 URL과 모바일용 URL이 동일하기 때문에 검색 포털 등 광고를 통한 사용자 접속을 효율적으로 관리할 수 있다.
또한 웹 페이지 내용을 수정할 경우, 하나의 페이지만 수정하면 PC와 모바일 등 다양한 디바이스에서 동일하게 반영된다.
반응형 웹의 핵심 기술은 가변 그리드(fluid grid), 유연한 이미지(flexible images), 미디어 쿼리(media query)이다. 반대말은 디바이스별로 별도의 웹사이트를 제작하는 적응형 웹(adaptive web)이다.


### 반응형과 적응형 차이
반응형 : 디바이스별로 반응하여 %로 적용함
적응형 : 대표적인 사이즈별로 모든 디자인을 만들어 사이즈를 감지하여 적용함


## 미디어 쿼리
미디어쿼리를 사용하면 일련의 테스트를 실행하고 CSS를 선택적으로 적용하여 사용자의 요구에 맞게 스타일을 지정할 수 있다.

뷰포트의 너비가 `80rem` 이상인지 테스트한다. `.container` 선택기에 대한 CSS는 이 두 가지가 참인 경우에만 적용된다.

```scss
@media screen and (min-width: 80rem) {
  .container {
    margin: 1em 2em;
  }
}
```