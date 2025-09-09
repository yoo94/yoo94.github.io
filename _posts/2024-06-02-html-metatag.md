---
layout: post
title: "메타 태그(Meta Tag)"
summary: "차이"
author: yoo94
date: "2024-06-02 16:35:23 +0530"
category: Frontend1
tags:
- MetaTag
- HTML
- 웹표준
- SEO
- 웹접근성
- OpenGraph
- viewport
- 웹퍼블리싱
- 프론트엔드
- 문서정보
keywords: Meta Tag, HTML 메타 태그, http-equiv, content 속성, name 속성, viewport 설정, SEO 최적화, Open Graph, 페이지 정보, 캐시 제어, 리디렉션, 문서 인코딩, 소셜 미디어 공유, 웹 접근성, 웹 표준
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/120px-HTML5_logo_and_wordmark.svg.png
permalink: blog/javascript-metatag/
---

# 메타 태그(Meta Tag)란?

HTML 메타 태그는 웹 페이지의 정보를 설명하고, 브라우저에게 추가적인 정보를 제공하는데 사용되는 특별한 태그
웹 페이지의 제목, 문자 인코딩, 페이지 설명, 작성자 등과 같은 정보를 제공 ####메타 태그는 웹 페이지의 검색 엔진 최적화(SEO)에도 영향을 미친다.
소셜 미디어에서 공유될 때 웹 페이지가 보여지는 방식을 결정할 수 있다.

## 메타 태그의 속성

### http-equiv="항목명"

웹 브라우저가 서버에 명령을 내리는 속성으로 name 속성 대신하여 사용될 수 있으며,
HTML 문서가 응답 헤더와 함께 웹 서버로부터 웹 브라우저에 전송되었을 때에만 의미를 갖는다.

### content="정보값"

meta 정보의 내용을 지정.

### name="정보 이름"

몇 개의 meta 정보의 이름을 정할 수 있으며 지정하지 않으면 http-equiv와 같은 기능

---

## 사용예

#### Content-Type

HTML 문서의 MIME 타입과 문자 인코딩을 설정.

```html
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
```

---

#### Refresh

페이지를 일정 시간 후에 새로 고침하거나 다른 URL로 리디렉션
첫 번째 예: 30초 후 페이지 새로 고침
두 번째 예: 5초 후 https://example.com로 리디렉션

```html
<meta http-equiv="Refresh" content="30" />
<meta http-equiv="Refresh" content="5; url=https://example.com" />
```

---

#### Cache-Control

문서의 캐싱 동작을 제어

```html
<meta http-equiv="Cache-Control" content="no-cache" />
```

---

#### Pragma

HTTP/1.0에서 캐싱을 제어

```html
<meta http-equiv="Pragma" content="no-cache" />
```

---

#### Expires

문서(캐시)의 만료 날짜와 시간을 설정합니다.

```html
<meta http-equiv="Expires" content="Wed, 21 Oct 2025 07:28:00 GMT" />
```

---

#### X-UA-Compatible

문서가 Internet Explorer에서 어떤 호환성 모드로 표시될지를 지정합니다.
예: IE=edge (최신 렌더링 엔진 사용)

```html
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
```

---

#### viewport

#####width=device-width

- 이 속성은 뷰포트의 너비를 설정합니다.
- device-width로 설정하면, 뷰포트의 너비를 디바이스의 화면 너비와 동일하게 만듭니다.
- 예를 들어, 모바일 디바이스에서 이 값을 설정하면, 페이지의 너비가 디바이스 화면 너비와 일치하여 콘텐츠가 화면에 맞게 조정됩니다.

#####initial-scale=1.0

- 이 속성은 페이지가 처음 로드될 때의 초기 확대/축소 비율을 설정합니다.
- 1.0으로 설정하면, 페이지가 기본 크기로 표시됩니다(즉, 100% 확대/축소).
- 이 값은 사용자가 페이지를 처음 볼 때 페이지의 실제 크기를 반영합니다.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

---

#### 페이지 제목 설정

```html
<meta name="title" content="웹 페이지 제목" />
```

---

#### 페이지 저자 정보

```html
<meta name="author" content="작성자 이름" />
```

---

#### 소셜 미디어 공유

```html
<meta property="og:title" content="웹 페이지 제목" />
<meta property="og:description" content="웹 페이지에 대한 설명" />
<meta property="og:image" content="이미지 URL" />
<meta property="og:url" content="웹 페이지 URL" />
```

#### 날짜 (제작일)

````html
<meta name="Date" content="2016-02-15T07:45:37+09:00" />
```--- #### 홈페이지 주제를 지정 ```html
<meta http-equiv="Subject" content="웹 표준을 위한 사이트" />
````

---

#### 메일 주소를 지정

```html
<meta http-equiv="Reply-To" content="naver@naver.com" />
<meta http-equiv="Email" content="naver@naver.com" />
```

---

#### 페이지 들어갈 때 장면 전환 효과

```html
<meta http-equiv="Page-Enter" content="revealtrans(Duration=1,Transition=12)" />
```
