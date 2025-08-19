---
layout: post
title: "크롬 확장자 만들기"
summary: "불편해서 만들어야겟어!"
author: yoo94
date: "202-08-11 5:30:23 +0530"
category: 임시DevLog,임시TechMisc
keywords: 
tags:
  - DevTools
thumbnail: /blog/postImg/20250811bughunter.png
permalink: blog/react/googleExtention/
published: false

---

## 뭔가 불편하다 -> 개발자다 -> 만들어서 해결하자 


### 목차
1. [크롬확장프로그램이란?](#1-크롬확장프로그램이란)
2. [이전에 만든 확장 프로그램?](#2-이전에-만든-확장-프로그램)
3. [chrome 확장프로그램 절차](#3-chrome-확장프로그램-절차)
4. [이제 만들어보자](#4-이제-만들어보자)
5. [크롬에 등록을 해보자](#5-크롬에-등록을-해보자)
6. [최종 정리](#6-최종-정리)

---

## 1. 크롬확장프로그램이란?

[크롬 확장프로그램 Chrome Extension](https://chromewebstore.google.com)은 구글 크롬 브라우저의 기능을 확장하거나, 사용자의 편의성을 높이기 위해 추가로 설치할 수 있는 작은 소프트웨어.  
확장프로그램을 통해 웹페이지의 동작을 제어하거나, 새로운 기능을 추가하고, 반복적인 작업을 자동화할 수 있다.

- **주요 특징**
  - 크롬 웹스토어를 통해 쉽게 설치/삭제 가능
  - HTML, CSS, JavaScript 등 웹 기술로 개발
  - 브라우저 UI에 버튼, 팝업, 사이드바 등 다양한 형태로 동작
  - 웹페이지의 내용에 접근하거나 수정 가능(권한 설정 필요)

즉, 크롬 확장프로그램은 브라우저를 나만의 도구로 커스터마이즈할 수 있는 수단이다.

리액트를 하는 개발자라면 React Developer Tools 이라는 크롬 확장프로그램을 사용해 본 적이 있을것이다. 

![React Developer Tools](/blog/postImg/20250819reacttoos.png)

나도 이 익스텐션에 도움을 굉장히 많이 받고있다. 이런것이 크롬 확장 프로그램이다.

---

## 2. 이전에 내가 만든 확장 프로그램?

![20250819velltodo](/blog/postImg/20250819velltodo.png)

아무도 사용은 안하고있지만, 나는 잘 사용하고 있다.

직업 특성상

- 시간관련된 로직이 제대로 돌아가는지 확인
- 빠르게 쳐내야할 작은 단위에 일감들을 기록하고 체크하기
- 메모장까지 켜서 굳이 오래 저장할 필요없는 글들이 많음

위 세가지 이유로 세개를 통합해서 그냥 구글 확장프로그램으로 만들어서 등록하여 내가 아주 잘 사용중이다 

이런식으로 가끔 pwa로 어플 만들어서 사용하기도 하고 그러는 와중에 내가 기억력이 짧은관계로

에러코드를 보면 항상 검색해 보고는 하는데 그게 너무 귀찮아서 사이드 패널에 띄워놓고 그냥 코드 입력하면

원인과 해결법을 알려주는 확장프로그램을 만들고자 했다. 이번에는 만드는 김에 기록하면서 하도록 하자.

---

## 3. chrome 확장프로그램 절차

1. **manifest.json 파일 생성** : 크롬 확장프로그램의 필수 설정 파일

2. **popup.html 파일 생성** : 확장프로그램 아이콘 클릭 시 보여줄 UI

3. **popup.js 파일 생성** : popup.html에서 동작할 JS 코드. (index.js와 분리)

4. **에러코드 데이터(JSON) 준비** : 검색할 에러코드와 설명, 대처방안 등이 담긴 JSON 파일을 만듦.

5. **검색 UI 및 로직 구현** : popup.html에 검색 input과 결과 표시 영역을 만들고, popup.js에서 검색 기능을 구현.


## 4. 이제 만들어보자

4-1. manifest.json 생성

아래는 기본

```json
{
  "manifest_version": 3,
  "name": "WhatTheBug",
  "version": "1.0.0",
  "description": "에러코드 검색 및 설명 제공 확장프로그램",
  "action": {
    "default_popup": "src/popup.html",
    "default_icon": {
      "16": "icon16.png",
      "32": "icon32.png",
      "48": "icon48.png",
      "128": "icon128.png"
    }
  },
  "icons": {
    "16": "icon16.png",
    "32": "icon32.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },
  "permissions": []
}

```

확장프로그램이 타이머처럼 백그라운드에서도 돌아가야한다던가 사이드패널이나 로컬스토리지같은걸 사용해야한다면 
아래 다양한 옵션을 검색해서 내 파일과 연결해줘야한다. 
**또한 추후에 크롬에 등록할때 왜 그런 기능을  사용해야하는지 소명도 해야한다.** 

이번 프로젝트는 다 필요없으니 스킵 ~~~ 
(이건 다른 주제인데 ~ 이 물결표시 많이 쓰면 3040대라던데.. ㅎㅎ;; 정확한듯)

```json
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_title": "Open Todo Sidebar"
  },
  "side_panel": {
    "default_path": "index.html"
  },
```




## 5. 크롬에 등록을 해보자