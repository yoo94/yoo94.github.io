---
layout: post
title:  "nextJs 페이지 라우터 pre-rendering"
summary: "nextJs-pre-rendering"
author: yoo94
date: '2024-08-23 13:35:23 +0530'
category: ['nextJs']
tags: react,nextJs
thumbnail: 
permalink: blog/nextJs-pre-rendering/
---

# 페이지 라우터에서의 

## 사전 렌더링 함수

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

### getServerSideProps:
서버 사이드 렌더링을 위한 데이터 가져오기 함수. 매 요청마다 데이터를 서버에서 가져옴 ssr사용가능

예를 들어, 자주 업데이트 되는 posts 데이터를 외부 API로부터 fetch해서 사전 렌더링 하고 싶을 때 사용

```javascript
export async function getServerSideProps() {
const data = await fetchData(); // 서버에서 데이터 가져오기
return {
    props: {
        data,
        },
    };
}
```