---
layout: post
title: "nextJs 페이지 라우터 pre-rendering"
summary: "nextJs-pre-rendering"
author: yoo94
date: "2024-08-23 13:35:23 +0530"
category: ["nextJs"]
tags: react,nextJs
thumbnail:
permalink: blog/nextJs-pre-rendering/
---

### SSR

사용자가 새로운 사이트 요청 →

서버에서 미리 생성된 HTML 파일 제공 (화면 O, 상호작용 X) →

브라우저가 JS 파일 다운로드 (화면 O, 상호작용 X) →

브라우저가 JS 실행 (화면 O, 상호작용 O)

---

SSR 사용 서비스 예시:
주로 동적 콘텐츠를 포함하고 있는 웹 애플리케이션에 적합

예) 뉴스 웹 사이트, 블로그, 전자 상거래 플랫폼 등

##### [장점]

SEO 최적화:
SSR 된 페이지들은 검색 엔진에서 쉽게 색인화 가능.

초기 로딩 속도 개선:
사용자에게 초기 콘텐츠를 더 빠르게 표시할 수 있음.

데이터 최신화:
매 요청마다 최신 데이터를 가져올 수 있음.

##### [단점]

서버 부하:
매 요청마다 서버에서 페이지를 가져오면서 서버 자원을 많이 사용할 수 있음.

느린 네트워크 연결:
서버에서 HTML 생성해서 가져오는데, 느린 네트워크 영향을 받으면 초기 로딩이 느려질 수 있음.

```js
import React from "react";

function HomePage({ data }) {
  return (
    <div>
      <h1>Hello {data}!</h1>
    </div>
  );
}

export async function getServerSideProps() {
  const data = await fetchData(); // 서버에서 데이터 가져오기
  return {
    props: {
      data,
    },
  };
}

export default HomePage;
```

---

### 정적 사이트 생성 (SSG)

##### SSG는 페이지를 사전에 빌드 시점에서 생성하고 정적 파일로 제공하는 방식

##### 기본적으로, Next.js는 SSG 방식으로 데이터를 페칭함

초기 로딩 속도가 빠르며 SEO가 우수함

미리 빌드된 페이지를 제공하므로 서버 부하가 낮음

하지만, 정적 데이터를 사용하므로 동적 콘텐츠에는 제한이 있음

예) 주로 블로그, 포트폴리오 웹 사이트, 회사 홈페이지 등 정적인 사이트에 사용

##### [장점]

빠른 초기 로딩 속도
SEO 우수
서버 부하 낮음

##### [단점]

동적 데이터 제한
업데이트된 데이터에 대한 재빌드 필요

```js
import React from "react";

function HomePage({ data }) {
  return (
    <div>
      <h1>Hello, {data}!</h1>
    </div>
  );
}

export async function getStaticProps() {
  const data = await fetchData(); // 정적 데이터 가져오기
  return {
    props: {
      data,
    },
  };
}

export default HomePage;
```

---

### CSR

사용자가 새로운 사이트 요청 →

서버에서 빈 HTML 파일 제공 (화면 X, 상호작용 X) →

브라우저가 JS 파일 다운로드 (화면 X, 상호작용 X) →

브라우저가 JS 실행 (화면 O, 상호작용 O)

---

CSR 서비스 예시:
주로 웹 애플리케이션에서 클라이언트 측 라우팅 및 상호 작용이 많은 경우에 사용

예) SPA, 대시보드 및 관리 패널, 소셜 미디어 플랫폼, 라이브 스트리밍 및 실시간 업데이트 서비스

##### [장점]

상호 작용성: 클라이언트에서 페이지를 렌더링하므로 사용자와의 상호 작용이 빠르게 이루어짐.

서버 부하 감소: 서버는 초기 HTML만 제공하고 이후에는 클라이언트에서 데이터를 로드함.

자연스러운 앱 경험: 싱글 페이지 애플리케이션(SPA)으로 구현되는 경우가 많은데, 이는 자연스러운 앱과 유사한 사용자 경험을 제공.

##### [단점]

SEO 어려움: CSR은 초기 HTML에 콘텐츠가 없으므로 검색 엔진 최적화(SEO)를 구현하기 어려움.

그 외: 초기 로딩 후 콘텐츠 표시까지 시간이 걸리는 문제, 성능 문제, JS 의존하는 문제.

CSR 코드 예시

useEffect 내부에 데이터를 가져오는 코드를 짜서 클라이언트 측에서 데이터 로드

```javascript
import { useEffect, useState } from "react";

function MyPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // 데이터를 가져오는 코드
    fetch("/api/data")
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      {data.map((item) => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
}

export default MyPage;
```
