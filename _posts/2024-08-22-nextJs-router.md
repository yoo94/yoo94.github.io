---
layout: post
title:  "page Router"
summary: "page Router -> App Router"
author: yoo94
date: '2024-08-22 13:35:23 +0530'
category: ['nextJs']
tags: react,nextJs
thumbnail: 
permalink: blog/nextJs-router/
---

## page Router

### pages디렉토리가 root

### pages 디렉토리 하위로 

index.js -> ~/
about.js -> ~/about
이렇게 파일 이름 기준으로 알아서 라우팅 해준다. 

### 폴더로도 가능하다.

page디렉토리 안에
index.js -> /
about/index.js -> /about
item/index.js -> /item

### 쿼리 스트링(?val=value)
##### useRouter
- useRouter훅은 이름 그대로 라우터객체를 컴포넌트에서 사용할수있게 객체를 반환해주는 훅이다.

```tsx
//url:3000/search?val=유재석
const router = useRouter();
const {val} = router.query; //<-val = 유재석
```

### 동적 경로 (urlParameter)
- url:3000/book/1
- url:3000/book/2
이런식으로 url에 쓰이는 가변적인 값들을 urlParameter라고 부른다.

 book디렉토리를 만들고 그 하위에 [id].tsx를 만들어준다.
 그럼 next는 파일명이 [] 로 감싸져 있으면 가변적인 페이지라고 판단한다.
id값을 꺼내 쓰는 법은 위에와 같다

```tsx
const router = useRouter();
const {id} = router.query
```

그렇다면 - url:3000/book/2/3/5/1/6 이렇게 하고싶으면?

###### catch All segment라고 한다.

[...id].tsx 이렇게 하면된다.

##### optional catch All segment 라고한다.
###### 근데 url:3000/book 이렇게하면 404뜬다. index.tsx 를 만들어도 되지만 
###### [[...id]].tsx 라고 하면된다.


### 404는?

루트에 404.tsx 만들면 끝임 ㅎ_ㅎ


