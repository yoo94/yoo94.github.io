---
layout: post
title:  "js에서 module을 쓰는 이유? "
summary: "자바스크립트 모듈 시스템을 사용하는 이유?"
author: yoo94
date: '2024-05-26 19:35:23 +0530'
category: ['myconfused','javaScript']
tags: myconfused, js, module, requirejs, amd,umd
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: /blog/float/
---
## 왜 모듈을 사용할까?
	유지보수성 : 기능들이 모듈화가 잘 되어있다면, 의존성을 그만큼 줄일 수 있기 때문에 어떤 기능을 개선한다거나 수정할 때 훨씬 편하게 할 수 있다.
	네임스페이스화 : 자바스크립트에서 전역변수는 전역공간을 가지기 때문에 코드의 양이 많아질수록 겹치는 네임스페이스가 많아질 수 있다. 그러나 모듈로 분리하면 모듈만의 네임스페이스를 갖기 때문에 그 문제가 해결된다.
	재사용성 : 똑같은 코드를 반복하지 않고 모듈로 분리시켜서 필요할 때마다 사용할 수 있다.

스크립트의 크기가 점차 커지고 기능이 복잡해짐에 따라 라이브러리를 만들어서 
필요한 모듈을 언제든지 볼러올 수 있도록 하거나 모듈로 쉽게 분리 할 수 있는 방법을 제시했다.

### AMD , common JS , UMD가 있다.

- Amd는 requireJs를 필두로 가장 오래된 모듈 시스템중 하나이다. Define과 require를 사용한다.

- Common Js 는 서버사이드를 위해 만들어진 것으로, 범용적인 사용을 위해 모듈화의 개념을 적용했다. Require와 module.exports를 사용한다.

- UMD는 CommonJS 와 AMD로 나뉘기 때문에 그걸 통합

- ES6(ES2015) 방식은 import와 export 구문을 사용하는 방식으로 모든 브라우저에서 지원하는건 아니기 때문에 babel을 통해 변환시켜서 사용한다.
