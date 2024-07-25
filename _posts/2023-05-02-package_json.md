---
layout: post
title:  "React 패키지.json뭐야?"
summary: "패키지.json뭐야?"
author: yoo94
date: '2023-05-02 16:35:23 +0530'
category: react
tags: react
keywords: react
thumbnail: https://blog.kakaocdn.net/dn/CXCxi/btszJHkBdaR/gzidgB00mb931TLMKkS3QK/img.png
permalink: blog/package_json/
---
## package.json은 React의 문서가 아니라 node.js의 문서이다.**

package 는 라이브러리,프레임워크 등의 통칭이고

package.json은 패키지 정보,패키지 실행에 필요한 구성과 방법을 정의한다.

package.json파일은 프로젝트 단위로 설치한다.

[https://www.npmjs.com/](https://www.npmjs.com/)

아래 공식문서 들어가면 관련 CLI들 많이 나오니 읽어보고 필요한거있으면 설치해서 사용해보도록!


일단 설치

```powershell
npm init
```

package.json은 JSON형태여야한다. (공식문서가 그렇다함)

즉 객체의 형태가 {key : "value"} 가 아니라 {"key": "value"} 처럼 큰 따옴표로 키도 감싸줘야한다는 말이다.

(앞에꺼는 js의 객체 형태이다.)

package.json의 프로퍼티를 보자


name : 패키지이름

version : 패키지 버전 (외부 공개 시 필수 작성)

description : 패키지 설명

main : 패키지 중에서 메인 파일 이름 module ID

script : 실행되는 스크립트 명령어들을 작성

author : 패키지 제작자 

license : 패키지 라이센스

-------------- 설명은 대충 여기까지 하고,



실행을 한번 해보자. 위에 script에다가  아래 내용을 넣은다음


"start":"node js파일.js"


## npm run start를 터미널에 입력하면 js파일에 있는 js가 실행된다.

즉 터미널에 node js파일.js를 그냥 쳐버린거랑 같은 것이다.

위에처럼 작성해 놓으면 한번에 실행할 수 있게 해주는 것이다.

npm run (command) 은 약어이고 npm runt-script (command) 가 정석이다

## 참고로 npm run command에서 command가 start, stop, restart, test + command는 run을 생략할 수 있다.**
