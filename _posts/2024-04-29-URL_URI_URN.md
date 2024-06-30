---
layout: post
title:  "URL URI URN"
summary: ""
author: yoo94
date: '2023-10-29 17:35:23 +0530'
category: webetc
tags: webetc
thumbnail: https://miro.medium.com/v2/resize:fit:1100/format:webp/1*7s4zgKH2ffUBQnZgOH4FQQ.png
permalink: /blog/URL_URI_URN/
---

### 😅 URI, URL, URN
URI와 URL이 혼동되기 쉽다. 결론부터 말하자면 URI는 URL의 상위 개념이다.


### URI란?

- URI는 Uniform Resource Identifier, 통합 자원 식별자의 줄임말이다.
- 즉, URI는 인터넷의 자원을 식별할 수 있는 문자열을 의미한다.
- URI의 하위 개념으로 URL과 URN이 있다.
- URI 중 URL이라는, URN이라는 하위 개념을 만들어서 특별히 어떤 표준을 지켜서 자원을 식별하는 것이다.
- 결론은 URI라는 개념은 어떤 형식이 있다기 보다는 특정 자원을 식별하는 문자열을 의미한다. 그래서 URL이 아니고 URN도 아니면 그냥 URI가 되는 것이다.



### URL이란?

- URL은 Uniform Resource Locator의 줄임말이다.
- URL은 네트워크 상에서 리소스(웹 페이지, 이미지, 동영상 등의 파일) 위치한 정보를 나타낸다.
- URL은 HTTP 프로토콜 뿐만아니라 FTP, SMTP 등 다른 프로토콜에서도 사용할 수 있다.
- URL은 웹 상의 주소를 나타내는 문자열이기 때문에 더 효율적으로 리소스에 접근하기 위해 클린한 URL 작성을 위한 방법론이다.



### URL구조

```
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

1. scheme : 사용할 프로토콜을 뜻하며 웹에서는 http 또는 https를 사용
2. user와 password : (서버에 있는) 데이터에 접근하기 위한 사용자의 이름과 비밀번호
3. host와 port : 접근할 대상(서버)의 호스트명과 포트번호
4. path : 접근할 대상(서버)의 경로에 대한 상세 정보
5. query : 접근할 대상에 전달하는 추가적인 정보 (파라미터)
6. fragment : 메인 리소스 내에 존재하는 서브 리소스에 접근할 때 이를 식별하기 위한 정보



### URN이란?

- URN은 Uniform Resource Name의 줄임말이다.
- URN은 URI의 표준 포맷 중 하나로, 이름으로 리소스를 특정하는 URI이다.
- http와 같은 프로토콜을 제외하고 리소스의 name을 가리키는데 사용된다.
- URN에는 리소스 접근방법과, 웹 상의 위치가 표기되지 않는다.
- 실제 자원을 찾기 위해서는 URN을 URL로 변환하여 이용한다.



### URL과 URN의 차이점

- **URL**은 **어떻게 리소스를 얻을 것**이고 **어디에서 가져와야하는지 명시**하는 URI이다.
- **URN**은 리소스를 어떻게 접근할 것인지 명시하지 않고 **경로와 리소스 자체를 특정**하는 것을 목표로하는 URI이다.