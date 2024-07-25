---
layout: post
title:  "RESTful API란?"
summary: ""
author: yoo94
date: '2023-12-14 17:35:23 +0530'
category: ['myconfused','webetc']
tags: webetc
keywords: 
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: blog/RESTful-API/
---
## 먼저 REST API 란무엇인가
RESPT API란 REST의 원리를 따르는 API를 의미합니다.
REST API 에서 REST는 Representational State Transfer 의 약자로 소프트웨어 프로그램 아키텍처의 한 형식.

즉, 자원을 이름 (자원의 표현) 으로 구분하여 해당 자원의 상태 (정보)를 주고 받는 모든 것을 의미.

월드 와이드 웹 (WWW) 과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식
REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다.

#### HTTP URI를 통해 자원을 명시하고, HTTP Method (POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD OPERATION을 적용하는 것을 의미한다.

REST는 자원 기반의 구조 (ROA: Resource Oriented Architecture) 설계의 중심에 Resoure가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.
웹의 모든 자원에 고유한 ID인 HTTP URI 를 부여한다.

#### 필요성
플랫폼에 맞추어 새로운 서버를 만드는 수고를 들이지 않기 위해 범용적으로 사용성을 보장하는 서버 디자인이 필요하게 되었다.
- RESTful APIs 개발하는 가장 큰 이유는 Client Side를 정형화된 플랫폼이 아닌 모바일, PC, 어플리케이션 등 플랫폼에 제약을 두지 않는 것을 목표로 했기 때문 이다.
- TV, 스마트 폰, 테블릿 등 Client 프로그램이 다양화 되고 그에 맞춰 Server를 일일이 만다는 것이 꽤 비효율적인 일이 되어 버렸다.

#### 주의사항
REST API를 개발하다보면 HTTP의 Response 규약을 지키지 않고 본인들이 만들어낸
JSON 컨벤션으로 응답하는 경우를 많이 확인 할 수 있는데 그것은 옳지 않은 개발 방향이다.
왜냐하면 Client Side가 정형화 되어있지 않은 환경에서 개발 속도를 저하하는 가장 큰 이유는 표준을 지키지 않았기 때문이다.

### REST의 구성
자원(Resource) : HTTP URI
자원에 대한 행위(Verb) : HTTP Method
자원에 대한 행위의 내용 (Representations) : HTTP Message Pay Load

###REST의 장단점
##### 장점
- HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구출할 필요가 없다.
- HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해 준다.
- HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.
- Hypermedia API의 기본을 충실히 지키면서 범용성을 보장한다.
- REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.
- 여러 가지 서비스 디자인에서 생길 수 있는 문제를 최소화한다.
- 서버와 클라이언트의 역할을 명확하게 분리한다.
##### 단점
- 표준이 자체가 존재하지 않아 정의가 필요하다.
- HTTP Method 형태가 제한적이다.
- 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 정보의 값을 처리해야 하므로 전문성이 요구된다.
- 구형 브라우저에서 호환이 되지 않아 지원해주지 못하는 동작이 많다.(익스폴로어)

# RESTful API를 설계하기 위해서는 몇 가지 중요한 원칙을 따라야한다.
## REST API 설계 예시
1. URI는 동사보다는 명사를, 대문자보다는 소문자를 사용하여야 한다.
2. 마지막에 슬래시 (/)를 포함하지 않는다.
3. 언더바 대신 하이폰을 사용한다.
4. 파일확장자는 URI에 포함하지 않는다.
5. 행위를 포함하지 않는다. (.../delete-post) <- x
