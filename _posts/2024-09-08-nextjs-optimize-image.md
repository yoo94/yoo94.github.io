---
layout: post title:  "next optimize image"
summary: "next 이미지 최적화"
author: yoo94 date: '2024-09-08 14:35:23 +0530' category: ['nextJs','react']
tags: react,nextJs
permalink: blog/next-optimize-image/
---

## Image 라는 컴포넌트를 사용하면 거의 대부분 최적화를 해준다 
 참고로 외부에서 불러오는 이미지에대한 안전성을 부여하려면
next.config.mjs에서
images:{
    domains:["도메인""]
}
을 넣어주면 된다.
