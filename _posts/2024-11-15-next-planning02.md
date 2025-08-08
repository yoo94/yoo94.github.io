---
layout: post
title: "next js application 페이지,레이아웃 설정"
summary: "step 2"
author: yoo94
date: "2024-11-15 18:32:23 +0530"
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
permalink: blog/nextjs-planning02/
---

### 페이지 경로 정의

| **파일 위치 (Pages Router)** | **설명 (URL)**                    |
| ---------------------------- | --------------------------------- |
| /pages/stores/index.js       | 맛집 목록 (/stores)               |
| /pages/stores/new.js         | 맛집 생성 페이지 (/stores/new)    |
| /pages/stores/[id]/index.js  | 맛집 상세 페이지 (/stores/1)      |
| /pages/stores/[id]/edit.js   | 맛집 수정 페이지 (/stores/1/edit) |
| /pages/users/login.js        | 로그인 페이지 (/users/login)      |
| /pages/users/mypage.js       | 마이페이지 (/users/mypage)        |
| /pages/users/likes.js        | 찜한 맛집 (/users/likes)          |

### 최상위 index에다가 Link를 다 달아놧다.

```tsx
import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Map Index Page</h1>
      <ul>
        <li>
          <Link href="/stores">맛집 목록</Link>
        </li>
        <li>
          <Link href="/stores/new">맛집 생성</Link>
        </li>
        <li>
          <Link href="/stores/1">맛집 상세페이지</Link>
        </li>
        <li>
          <Link href="/stores/1/edit">맛집 수정 페이지</Link>
        </li>
        <li>
          <Link href="/users/login">로그인페이지</Link>
        </li>
        <li>
          <Link href="/users/mypage">마이페이지</Link>
        </li>
        <li>
          <Link href="/users/likes">찜한 맛집</Link>
        </li>
      </ul>
    </div>
  );
}
```

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
