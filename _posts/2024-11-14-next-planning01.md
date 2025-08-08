---
layout: post
title: "next js application 기획 및 폴더구조 파악"
summary: "step 1"
author: yoo94
date: "2024-11-14 18:32:23 +0530"
category: DevLog
tags:
  - nextjs
  - planning
  - 기획
  - 처음부터
  - cna
  - tailwind
  - next auth
  - react query
  - recoil
  - GoDaddy
  - prisma
  - supa-base
  - vercel 배포
  - 구글 애널리틱스 적용
  - 카카오 지도 api
thumbnail:
permalink: blog/nextjs-planning01/
---

### nextjs 로 사이트를 구축할때 a to z까지의 순서를 기록해 보고자 한다. 자세히는 아니고 기획적인 부분만하겠다.

#### 페이지 라우터를 쓸것이고 마지막에 점진적으로 앱라우터로 바꾸는것도 다뤄볼 예정이다.

_개념은 안다룹니다._

#### 만들어볼 어플리케이션은 맛집 싸이트이다.

#### 기술 스택

- next js
- cna
- tailwind
- next auth
- react query
- recoil
- GoDaddy
- prisma
- supa-base
- vercel 배포
- 구글 애널리틱스 적용
- 카카오 지도 api

---

## 진행순서

#### 1. 프로젝트 세팅 - 페이지 세팅 등

#### 2. 컴포넌트 생성 - 레이아웃, 컴포넌트, 스타일링

#### 3. next-auth 적용

#### 4. 지도 api 등 각종 api 적용

#### 5. 배포 및 도메인 연결

위 순서로 진행 할 것이다.

---

### 다이어그램

<img src="/blog/postImg/diagram.png" alt="Pasted image diagram.png" style="max-width:100%;">

---

### 유저스토리

| **유저 스토리**                                              | **기능 설계**                                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| 로그인된 사용자만 지도 서비스를 사용할 수 있다.              | Next-auth를 이용한 사용자 인증 관리 (SNS 로그인)                                      |
| 지도 마커를 누르면, 해당 마커의 정보를 띄울 수 있다.         | Recoil을 이용한 마커 관리 (active한 마커 관리)                                        |
| 상세 페이지에서는 맛집 상세 정보 & 댓글을 볼 수 있다.        | Next.js의 pages를 이용한 라우팅, getServerSideProps로 데이터 가져오기                 |
| 좋아요를 누르면 찜한 가게 리스트에서 모아볼 수 있다.         | Like 모델링, 좋아요 누르고 취소할 수 있는 API 설계                                    |
| 상세 페이지에서 댓글을 달 수 있고, 내 댓글만 모아볼 수 있다. | Comment 모델링, 댓글 API 설계, 마이페이지에서 사용자 댓글 모아보기                    |
| 맛집을 리스트로 정렬 & 키워드 검색해서 볼 수 있다.           | React Query의 infinite scroll 이용한 무한 스크롤, Recoil을 이용한 키워드 검색 및 정렬 |
| 새로운 맛집을 등록할 수 있고, 원하는 주소를 넣을 수 있다.    | Daum 주소 API를 활용한 주소 데이터 생성                                               |
| 지도를 현재 위치로 이동시키고, 내 주변 맛집을 볼 수 있다.    | geolocation을 활용한 현재 위치 가져오기 적용                                          |

---

### 폴더구조는 다음과 같다.

| **최상위 폴더 (폴더명)** | **설명**                          |
| ------------------------ | --------------------------------- |
| pages                    | Pages router (페이지 라우터)      |
| public                   | 이미지 파일 등 정적 파일 관리     |
| src                      | (선택사항) 애플리케이션 소스 폴더 |

---

### next.js 파일구조

| **최상위 파일 (파일명)**     | **설명**                                |
| ---------------------------- | --------------------------------------- |
| next.config.js               | Next.js 프로젝트 설정 파일              |
| package.json                 | 프로젝트 패키지 의존성 및 스크립트 관리 |
| middleware.ts                | Next.js 미들웨어 파일                   |
| .env                         | 환경변수 파일                           |
| .eslintrc.json               | ESLint 설정 파일                        |
| .gitignore                   | Git 에서 무시할 파일들 정리             |
| .next-env.d.ts               | Next.js 타입스크립트 선언 파일          |
| tsconfig.json, jsconfig.json | 타입스크립트 / 자바스크립트 설정 파일   |
| postcss.config.js            | Tailwind CSS 설정 파일                  |

---

### 페이지 라우터 파일

| **파일명**    | **설명**                                                                               |
| ------------- | -------------------------------------------------------------------------------------- |
| \_app.js      | Next.js 커스텀 레이아웃 및 전역 설정 정의                                              |
| \_document.js | Next.js의 커스텀 문서 파일 (HTML 구조 정의, 스타일, 메타태그, 서버 사이드 렌더링 설정) |
| \_error.js    | Next.js 커스텀 에러 처리 페이지                                                        |
| 404.js        | 404 에러가 났을 때 뜨는 페이지                                                         |
| 500.js        | 500 에러가 났을 때 뜨는 페이지                                                         |

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

---

_출처 및 참고_

패스트캠퍼스 강의 중 - 최적화부터 유지보수까지 한번에 끝내기
