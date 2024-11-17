---
layout: post
title:  "nextJs 페이지 라우터 data-fetching"
summary: "nextJs-data-fetching"
author: yoo94
date: '2024-08-23 13:35:23 +0530'
category: ['nextJs']
tags: react,nextJs
thumbnail: 
permalink: blog/nextJs-data-fetching/
---

## 데이터 페칭 (Data Fetching)
웹 애플리케이션에서 데이터를 가져오는 프로세스

Next.js는 다양한 데이터 페칭 방법을 제공.

서버에서 데이터를 가져와 페이지를 렌더링하거나, 클라이언트 측에서 데이터를 가져와 동적으로 페이지를 업데이트할 수 있음.

공식 문서: Next.js Data Fetching

---

주요 데이터 페칭 함수

#### getStaticProps:
빌드 시점에 필요한 데이터를 가져오는 함수

#### getStaticPaths:
동적 경로를 사용할 때, 필요한 경로의 목록을 동적으로 생성하는 함수

#### getServerSideProps:
매 요청마다 서버에서 필요한 데이터를 가져오는 함수

#### API Routes:
Next.js에서 엔드포인트를 생성/사용하여 데이터를 가져오는 방법

---

### getStaticProps

정적 페이지 생성을 위한 데이터 가져오기 함수. 런타임이 아닌, 빌드(build) 타임에서만 실행이 되므로,
변동이 거의 없는 데이터 대상으로만 적용하는 게 좋음

예를 들어, 거의 변동이 없는 FAQ 글 목록을 가져올 때 사용됨

props로 넘겨서 페이지에서 사용 가능
```javascript
export async function getStaticProps() {
const posts = await fetchPosts(); // 데이터 가져오기 함수
    return {
        props: {
        posts,
    },
};
}
```
### 언제 getStaticProps를 사용해야 할까?

- 사전에 페이지를 미리 렌더링 할 때 ,데이터를 미리 fetch하고 싶을 때 사용 (빌드 타임에 실행됨)
- 변동이 거의 없는 데이터 대상으로만 적용하는 것이 좋음.
(단, 개발 모드에서는 항상 호출됨)
- 데이터가 Headless CMS에서 온 경우 : 콘텐츠를 생성,저장,관리하는 콘텐츠관리 
시스템만 제공하고 사용자들에게 콘텐츠가 보이는 부분은 api로 제공
- 페이지를 렌더링하는 데 필요한 데이터를 사용자의 요청 전, '빌드'할 때 사용해야 하는 경우
- SEO 최적화와 빠른 렌더링이 필요할 때
- 렌더링이 매우 빨라야 하는 경우
- getStaticProps는 성능을 위해 CDN에서 캐시할 수 있는 HTML 및 JSON 파일을 생성함.
- 데이터를 공개적으로 캐싱할 수 있는지 여부

(user-specific X) 사용자별 데이터에는 적합하지 않음.

---

### getStaticPaths:

동적 경로를 위한 정적 경로 생성 함수. 동적으로 생성되는 페이지를 사전 렌더링할 때 사용
예를 들어, 하나의 FAQ 데이터(id: 1)가 존재한다고 했을 때, 
faqs/1라는 경로를 빌드 타임에 미리 사전 렌더링할 수 있음

```javascript
export async function getStaticPaths() {
const paths = await fetchDynamicPaths(); // 동적 경로 생성 함수
    return {
        paths,
        fallback: false, // 없는 경로는 404 페이지로 처리
        };
    }
```

### 언제 getStaticPaths를 사용해야 할까?
- 특정 페이지의 경로(paths)가 외부 데이터에 의존할 때 getStaticPaths를 통해 사전 렌더링을 실행할 수 있음
예: Post 데이터 상세 페이지 (posts/1)와 같은 동적 경로를 사전에 렌더링

- getStaticPaths는 런타임이 아닌 빌드 타임(Next.js 빌드)에서만 실행되므로, 변동이 거의 없는 데이터 대상으로만 적합
(단, 개발 모드에서는 항상 호출됨)
- 동적 경로를 사용하는 페이지들을 사전 렌더링하고 싶을 때
    - 데이터가 Headless CMS나 파일 시스템에서 온 경우
    - 데이터가 데이터베이스에서 온 경우
    - 데이터를 공개적으로 캐시할 수 있는 경우 (user-specific X)
    - 페이지가 사전 렌더링 되어 SEO와 빠른 렌더링이 중요한 경우
  
---

### getServerSideProps:
서버 사이드 렌더링을 위한 데이터 가져오기 함수. 매 요청마다 데이터를 서버에서 가져옴 ssr사용가능

예를 들어, 자주 업데이트 되는 posts 데이터를 외부 API로부터 fetch해서 사전 렌더링 하고 싶을 때 사용


```ts
import type { InferGetServerSidePropsType, GetServerSideProps } from 'next';

type Repo = {
  name: string;
  stargazers_count: number;
};

export const getServerSideProps: GetServerSideProps<{ repo: Repo }> = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const repo = await res.json();
  return { props: { repo } };
};

export default function Page({
  repo,
}: InferGetServerSidePropsType<typeof getServerSideProps>) {
  return <div>{repo.stargazers_count}</div>;
}

```
### 언제 getServerSideProps를 사용해야 할까?

#### **getServerSideProps**는 getStaticProps와 비슷하지만 서버 사이드 렌더링을 위한 함수

- getStaticProps처럼 컴포넌트에 props를 넘겨준다는 공통점이 있지만, 빌드 시가 아닌 매 request마다 실행된다는 차이

예) 자주 업데이트 되는 데이터를 외부 API로부터 fetch해서 사전 렌더링 하고 싶을 때

#### 사용해야 하는 경우
- 매 요청마다 데이터를 가져와서 페이지를 렌더링해야 하는 경우 getServerSideProps를 사용
- 요청 시 서버 측에서 렌더링 해당 페이지는 cache-control 헤더가 구성된 경우에만 캐싱됨

#### 추천하지 않는 경우
만약 요청 중에 데이터를 렌더링할 필요가 없는 경우:
클라이언트 측에서 데이터를 가져오거나 getStaticProps를 통해 가져오는 것 권장

```