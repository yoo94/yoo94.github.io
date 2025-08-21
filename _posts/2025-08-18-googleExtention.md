---
layout: post
title: "크롬 확장자 만들기"
summary: "불편해서 만들어야겟어!"
author: yoo94
date: "202-08-11 5:30:23 +0530"
category: 임시DevLog,임시TechMisc
layout: post
title: "크롬 확장자 만들기"
summary: "불편해서 만들어야겟어!"
author: yoo94
date: "2025-08-18 5:30:23 +0530"
category: DevLog
keywords: 크롬 확장프로그램 만들기,Chrome Extension 개발,manifest.json 작성법,브라우저 확장프로그램,웹스토어 등록,JavaScript 확장프로그램,개발자 도구,크롬 웹스토어,확장프로그램 개발 가이드,브라우저 커스터마이징
tags:
  - 크롬확장프로그램
  - Chrome Extension  
  - 웹개발
  - JavaScript
  - manifest.json
  - 브라우저개발
  - 웹스토어
  - 개발도구
  - 생산성도구
  - 사이드프로젝트
  - 개발자도구
  - HTML
  - CSS
  - 웹팩
  - 번들링
tags:
  - DevTools
thumbnail: /blog/postImg/2508whatthebug.png
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

## 4-1. manifest.json 생성

아래는 기본이고 아이콘이 필요하다 16은 16x16이라고 생각하면되고
이미지 크기 조절사이트나 그림판에서도 조절 가능하다.

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

js나 html 같은건 기능에 맞게 잘 만들면된다. 웹뷰로 빌드한 파일을 보여준다고 생각하면 된다.
내 소스가 궁금하면 **[what the bug](https://github.com/yoo94/whatthebug)** 요기 참고 바란다.

다 개발하고 로컬에서 확인 했으면 내 로컬 개발자도구에 등록해서 사용해 볼 수도 있다.

## 4-2 테스트를 위한 개발자도구 (로컬)

먼저 **[크롬 익스텐션](chrome://extensions/)** 오른쪽에 확장프로그램 툴바에 맨 끝에 있는 확장프로그램 관리를 클릭해도되고
chrome://extensions/ 이 문자열을 크롬 주소창에 넣어도 된다.

![first](/blog/postImg/250821local.png)

여기서 압축해제된 확장 프로그램 로드라는 버튼이 있는데, 클릭해서 번들링 툴이나 빌드 툴을 이용한 빌트 디렉토리를 넣어주면 된다.

```json
{
  "name": "whatthebug",
  "version": "1.0.0",
  "description": "개발하면서 발생하는 에러코드 검색",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "build": "webpack",
    "zip": "zip -r whatthebug-extension.zip build/"
  },
  "keywords": [],
  "author": "yoo94",
  "license": "ISC",
  "devDependencies": {
    "copy-webpack-plugin": "^13.0.1",
    "webpack": "^5.101.3",
    "webpack-cli": "^6.0.1"
  }
}

```

나같은 경우는 웹팩을 설치해서 번들링을 해주었고, 
등록을 하게되면 위에 보여준 이미지처럼 whtthebug가 생겼다.
그다음 툴바에서 다른 확장프로그램 사용하듯이 하면 된다.

## 5. 크롬에 등록을 해보자

#### [크롬 확장프로그램 대시보드](https://chrome.google.com/webstore/devconsole/)
여기 들어가면 등록할수 있다.

![dashboard](/blog/postImg/250821dash.png)

오른쪽 위에 새항목을 클릭하면, zip 파일을 입력하라고하는데

스토어 등록 정보를 입력하는곳이 나온다. 

![side](/blog/postImg/250821side.png)

이 사이드 메뉴에서 **빌드** 부분을 작성하면된다. 


![first](/blog/postImg/250821first.png)

쓸때마다 대학생때 처럼 저장안해서 다 날려먹지말고 반드시 오른쪽 위에 임시저장을 눌러가면서 하면된다.

**또한 임시저장 옆에 제출할 수 없는 이유 라는게 있는데 누르면 어느 부분이 부족해서 제출을 못하는지 알려준다.**

![second](/blog/postImg/250821second.png)


![third](/blog/postImg/250821third.png)

위에서 말했듯이 백그라운드나 사이드패널, 스토리지를 사용하는 경우에는 왜 사용하는지에대한 항목도 작성해야한다.

사실 대충쓰면 되니까 ai시키면 다 만들어준다. ㅋㅋ 

그리고 개인정보 보호탭ㅇ

개인정보처리방침 페이지를 입력해야하는 부분이 있는데 

나같은 경우에는 [https://yoo94.github.io/policy/](https://yoo94.github.io/policy) 여기에 만들었으니 참고 부탁합니다~

다 채운다음에 제출을 하면~~

![250821dashmain](/blog/postImg/250821dashmain.png)


이렇게 검토 대기중이 되고, 3일정도 기다리면 승인해준다.

끝!!