---
layout: post
title:  "react의 servercomponent"
summary: "servercomponent"
author: yoo94
date: '2024-08-24 13:35:23 +0530'
category: ['nextJs','react']
tags: react,nextJs
thumbnail: 
permalink: blog/react-servercomponent/
---

## server component 왜 나왔을까?

next js에서 hidration을 하기전에 jsBundle을 하여 브라우저에게 전달되고
hidration을 위해 한번더 실행되고 있었다.
 jsbundle안에는 모든 컴포넌트가 포함될 필요가 없다. react hooks나 이벤트 핸들러가 있어서 hidration이 필요한
컴포넌트들도 있지만 아닌 정적인 페이지들도 있었다.
 
#### 페이지 라우터는 이러한 js들도 다 bundling 해서 제공했기 때문에 쓸데없이 많은 용량을 차지했다.

그래서 번들링을 할때는 정적인 컴포넌트들만 bundle에서 빼면된다. 
즉, 서버측에서만 실행되는 정적인 컴포넌트는 react server component라고 판단해 번들링에서 뺀다.!!!


### 결론적으론 클라이언트 컴포넌트만 번들링에 포함한다.

## 즉, 처음 사전 렌더링을 하는 과정에서는 html을 만들기위해 무조건 한번씩 실행되고,이후 hidration을 위해 js를 모아서 번들링하는 과정에서는
## 서버컴포넌트(정적)는 제외하게 된다.

<img src="/blog/postImg/serverComponent.png" alt="serverComponent.png" style="max-width:100%;">

# nextJs에서는 페이지 대부분을 서버 컴포넌트로 구성할 것을 권장한다.

#### 그래서 어떤게 클라이언트 어떤게 서버 컴포넌트로 만들어야할까

간단하게 상호작용 여부로 판단하면 된다.