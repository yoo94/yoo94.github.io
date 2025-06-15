---
layout: post
title: "next page router layout"
summary: "스타일링"
author: yoo94
date: "2024-08-24 13:35:23 +0530"
category: ["nextJs"]
tags: react,nextJs
thumbnail:
permalink: blog/nextJs-layout/
---

## css 스타일링

nextjs에서는 css파일을 import해주지 않는다 컴포넌트끼리 겹칠 수 도 있기 때무니다.
그래서 기본으로 css모듈을 제공한다.
index.css -> index.module.css 로 이름을 바꿔서 import하게되면
브라우저에 넘길때 자동으로 파일마다 유니크한 이름들로 바꿔서 넘겨준다.

```text
import style from "index.module.css"
<h1 className="style.h1"/>
```
