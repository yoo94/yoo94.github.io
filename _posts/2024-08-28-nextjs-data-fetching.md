---
layout: post
title:  "next app 라우터의 data fetching,caching,memo"
summary: "사전렌더링 과정 진행"
author: yoo94
date: '2024-08-28 13:35:23 +0530'
category: ['nextJs','react']
tags: react,nextJs
thumbnail: 
permalink: blog/next-data-fetching/
---
#페칭

## 페이지 라우터에서는 서버측에서만 실행되는 아래와같은 함수들을 이용했다. 

1. SSR - getServerSideProps()
2. SSG - getStaticProps()
3. Dynamic SSG - getStaticPaths()

#### 구조는 

<img src="/blog/postImg/next090801.png" alt="next090801.png" style="max-width:100%;">

<img src="/blog/postImg/next090802.png" alt="next090802.png" style="max-width:100%;">

위 이미지와 같이 실행하여 프롭스로 넘겨서 데이터를 사용했다.
그래서 최상단 page컴포넌트에서 받은 데이터를 자식 컴포넌트들에게 넘겨줘야하는 번거로움이있었다.

## 앱라우터에서는

<img src="/blog/postImg/next090803.png" alt="next090803.png" style="max-width:100%;">

이미지 처럼 asymc 키워드를 붙여서 서버 컴포넌트에 비동기 함수를 추가할수있다.

즉, 데이터가 필요한 컴포넌트가 있다면, 직접 호출해서 사용하는것이 원칙이 된 것이고
### 무려 next 공식문서에도 직접 호출을 권장한다.

---

# 캐싱

넥스트에서의 캐시는 fetch 메서드에서 옵션 설정할 수 있다.
참고로 무조건 fetch를 사용해야한다.

## no-store
```js

const response = await fetch('~/api',{cache:"no-store"})

```
데이터 페칭의 결과를 저장하지 않는 옵션, 즉 캐싱을 아예 하지 않는다. 옵션설정 안하면 이게 기본값이다.

## force-cache
```js

const response = await fetch('~/api',{cache:"force-cache"})

```
요청의 결과를 무조건 캐싱한, 한번 호출 된 이후에는 다시는 호출되지 않음


## revalidate
```js

const response = await fetch('~/api',{next:{revalidate : 10}})

```
특정 시간을 주기로 캐시를 업데이트함, 페이지 라우터의 ISR 방식과 유사

## tags
```js

const response = await fetch('~/api',{next:{tags : ['a']}})

```
요청이 들어왔을 때 데이터를 최신화함, on-demand Revalidate

---

## request 메모제이션

캐시와는 완전 다르다.
메모제이션은 하나의 페이지를 렌더링하는 동안에만 존재하는 캐시라고 생각하면된다.
즉, 렌더링 과정이 다 끝나면 소멸되어 캐시처럼 다음요청에 응답하지 않고
다시한번 서버로 요청을 하게된다.

그렇다면 이걸 굳이 왜 사용할까?

#### 서버컴포넌트가 도입되었기 때문이다.

이 옵션은 next에서 자동실행된다.

예를들어 같은 page.tsx에서 
first.tsx second.tsx 둘다 
특정 데이터가 필요해서 권장사항에 맞게 같은 api를 두곳에서 호출해도
실제로는 1번만 호출하게 해주는것이다.
렌더링 이후에는 소멸하여 새로고침하면 다시 호출된다.