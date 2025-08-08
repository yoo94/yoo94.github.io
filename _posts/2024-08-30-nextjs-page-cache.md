---
layout: post
title: "next app 라우터의 full router cache"
summary: "페이지 캐싱을 해준다."
author: yoo94
date: "2024-08-30 13:35:23 +0530"
category: Frontend2
tags: react,nextJs
thumbnail:
permalink: blog/next-full-router-cache/
---

## full route cache란?

next 서버에서 빌드 타임에 특정 페이지의 렌더링 결과를 캐싱하는 기능

<img src="/blog/postImg/next083001.png" alt="next083001.png" style="max-width:100%;">

위 이미지처럼, 페이지 경로가 /a라는 페이지가 있을때 ,
빌드를 하게되면 사전렌더링 -> 메모이제이션 -> 데이터 fetch 및 캐시 -> 백엔드서버
로 빋르하게 되고 렌더를 할 html을 반환하게 된다. 그 데이터들을 풀 라우트 캐시로 설정을 하게 되면
나중에 클라이언트가 /a를 요청하게 될때 캐싱된 html을 반환하는 것이다.

### 즉 ssg와 유사하다고 볼 수 있다.

그렇다면 어떤 페이지가 풀라우트 캐시로 설정 해야할까

next js는 정적페이지와 동적페이지 두가지로 나뉜다.

정적인 static한 페이지에는 풀라우트 캐시가 적용된다.

### dynamic 페이지 기준?

- 특정 페이지가 접속 요청을 받을 때 마다 변화가 생기거나 데이터가 달라지면 다이나믹 페이지다
- 캐시 되지 않는 data fetching을 사용하는 경우
- 동적 함수 (쿠키,헤더,쿼리스트링) 을 사용하는 컴포넌트가 있을 때

### static 페이지 기준?

- 동적인거 제외한거 모두!
- 동적함수를 사용하지 않고 데이터캐시를 사용하게 되면 정적인 것이다.

#### revalidate도 가능하다. 즉 특정 시간마다 업데이트를 할 수 있다는 것이다.

<img src="/blog/postImg/next083002.png" alt="next083002.png" style="max-width:100%;">

- 3초를 설정해 놓게되면 3초 뒤에 요청이 들어왔을 때에 풀라우트 캐시에서 현재 페이지는
  html을 반환하지만 캐싱된 페이지는 상했다고 세팅을한다. 일단 상한 html을 보내면서 서버로 새로운 페이지를 요처하고
  새로운 html을 받아와서 다음 요청에 새로운 것을 보내준다.

#### 설정은 data fetch를 할때 revalidate 설정을 해주면 페이지도 같이 그시간에 맞춰 업데이트 된다.
