---
layout: post
title:  "next streaming"
summary: "스트리밍을 가능케한다."
author: yoo94
date: '2024-09-02 13:35:23 +0530'
category: ['nextJs','react']
tags: react,nextJs
thumbnail: 
permalink: blog/next-streaming/
---

##  streaming

next는 비동기처리를 하여 렌더링이 오래걸리는 컴포넌트에 대해서, 페이지에 빨리 렌더링 할수 있는 부분부터 주고 
오래 걸리는 컴포넌트는 준비가 되면 주는 방식인 스트리밍을 가능하게 해준다.

### loading.tsx
page.tsx 와 같은 경로에 loading.tsx를 만들고 그 안에
Loading 할때 보여줄 컴포넌트를 만들면 자동 설정 된다.

#### 주의사항
- loading.tsx는 하위 모든 페이지에서 다 동일하게 스트리밍되게 적용됨
- async가 붙어서 비동기로 제공되는 컴포는터에서만 적용된다.
- 페이지 컴포넌트에서만 적용된다.


## 페이지 말고 그냥 일반 컴포넌트에서도 스트리밍 하고싶다면?
### suspense를 사용하면 된다.

이런 suspense는 스켈레톤 ui와 함께 사용하면 참 좋다.

<img src="/blog/postImg/next-streaming.png" alt="next-streaming.png" style="max-width:100%;">

위 이미지처럼 뭔가 불러올때 스켈레톤 ui를 적용해주면 된다.

react-loading-skeleton 이라는 npm 라이브러리도 좋다고한다.