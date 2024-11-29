---
layout: post
title: "react query page nation"
summary: "페이지 네이션 해보자"
author: yoo94
date: '2024-11-16 19:32:23 +0530'
category: ['nextJs']
tags:
  - nextJs
  - react-query
  - react
thumbnail: 
permalink: blog/react-query2/
---

### Pagination이란?
- 정의:
긴 목록을 여러 페이지로 나눠서 보여주는 기술.
사용자 경험(UX)을 개선하기 위해 긴 목록을 한 번에 모두 보여주는 대신 분리해서 제공.

- 이점:
사용자가 필요한 정보를 쉽게 찾을 수 있도록 도움.
검색 결과, 게시물 목록, 제품 목록 등에서 효과적으로 사용.

- 서버-클라이언트 효율성:
서버는 클라이언트에 데이터를 나누어 전송하여 한 번에 대량의 데이터를 처리하는 부담을 줄임.

#### 전체
- 페이지 번호를 Query Params로 전달: 각 페이지에 해당하는 데이터를 10개씩 서버에서 가져오도록 설계.
예: GET /api/items?page=1&limit=10

- 총 페이지 수가 10 이하인 경우:모든 페이지 번호를 화면에 표시.
각 페이지 번호를 클릭하면 해당 페이지의 데이터가 로드.

- 총 페이지 수가 10 이상인 경우:현재 페이지 근처의 몇 개의 페이지만 표시.
"이전" 및 "다음" 버튼을 추가하여 다른 페이지로 이동.


---

### 설계 

1. Store 페이지
   현재 페이지 값 가져오기:

- Next.js의 **router.query**를 이용하여 현재 페이지 값을 가져옵니다.
예: useRouter().query.page

- API 호출: /api/stores?page=${} 형식으로 현재 페이지 값을 API로 전달하여 데이터를 가져옵니다.
API는 페이지에 맞는 데이터만 반환하도록 설계.

- Pagination 컴포넌트 렌더링:현재 페이지 숫자를 강조하여 Pagination 컴포넌트를 화면에 표시.

2. Pagination 컴포넌트
- 총 페이지 수와 현재 페이지 수를 Props로 받음: totalPages (전체 페이지 수)와 page (현재 페이지)를 Props로 받아 상태 관리.
- 링크 생성: 총 페이지 수만큼 버튼 또는 링크를 생성.
예: ?page=N 형태로 query parameter를 이용해 페이지를 이동.
- UI 상태: 현재 페이지는 파란색으로 강조. 
- 총 페이지 수가 10개 이상인 경우: 이전/다음 버튼 추가로 페이지 이동 가능.

3. Next.js API Routes (Prisma 활용)
- 페이지 데이터 처리:API에서 현재 페이지 값을 받아 해당 페이지에 해당하는 데이터만 클라이언트에 전달. 
- skip과 take 활용:Prisma의 skip(건너뛸 항목 수)과 take(가져올 항목 수)를 사용하여 데이터 쿼리를 최적화.
