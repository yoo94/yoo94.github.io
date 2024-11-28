---
layout: post
title: "next-api-routes"
summary: "서버리스 백엔드 역할 수행"
author: yoo94
date: '2024-11-13 18:32:23 +0530'
category: ['nextJs']
tags:
  - nextJs
  - next-api-routes
  - react
thumbnail: 
permalink: blog/next-api-routes/
---

## Next.js API Routes

##### Next.js 애플리케이션 내에서 서버리스 백엔드 역할을 수행하는 기능

#### 제공 기능

- 서버리스 백엔드: 서버를 구축하지 않고도 서버리스 백엔드 기능을 제공
- API 엔드포인트: API Routes를 사용하여 서버에 엔드포인트를 생성하고, 클라이언트에서 데이터를 요청하거나 전달할 수 있음 (예: /pages/api 디렉터리에 파일 생성 후 API 함수 작업)
- HTTP 요청 처리: HTTP GET, POST, PUT, DELETE 등의 요청을 처리하고 응답을 생성 
- 파라미터 처리: 동적 라우팅을 통해 URL 파라미터를 추출하고 사용
- 미들웨어 사용: 요청과 응답에 대한 미들웨어 함수를 적용하여 요청 전처리 및 인증을 처리
- 클라이언트 호출: 클라이언트에서 API Routes에 HTTP 요청을 보내 데이터를 요청하고 업데이트


---

### 생성 과정
1. pages/api 디렉토리에 엔드포인트 파일 생성: 이 디렉토리 내의 파일들이 자동으로 API 엔드포인트로 매핑됩니다.

2. 엔드포인트 파일 내에서 요청 메서드에 맞는 로직 작성: 요청 메서드(GET, POST 등)에 맞춰 조건을 작성하여 처리합니다.

3. req 객체에서 요청 데이터를 가져오고 res 객체로 응답을 보내기:

4. 
- req: 클라이언트로부터 들어온 요청 데이터(쿼리 파라미터, 바디 데이터 등).
- res: 응답을 클라이언트에 반환하기 위해 사용됩니다(예: res.status(200).json()으로 JSON 응답을 보냄).

```ts
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

---

#### HTTP 메서드에 따른 Next.js API Routes 사용
- 요청 핸들러에서 req.method를 사용해 HTTP 메서드에 따라 API를 분리해서 적용할 수 있음
- 아래와 같이 HTTP 요청의 메서드(GET, POST, PUT, DELETE 등)에 따라 다른 코드 블록이 실행됨
- 파라미터를 사용하여 동적 엔드포인트를 생성할 수 있으며, 간단한 미들웨어를 적용하여 요청을 가로채고 처리할 수 있음

```ts
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    // Process a POST request
  } else {
    // Handle any other HTTP method
  }
}

```

#### Next.js API Routes 장단점
- 간편한 백엔드 구축: 서버를 별도로 설정하거나 관리하지 않고도 서비스 백엔드 엔드포인트를 쉽게 만들 수 있음
- 통합된 개발: 프론트엔드 및 백엔드를 동시에 개발하고 관리할 수 있어 개발 생산성이 향상
- 동적 라우팅: 동적 엔드포인트를 생성하고 파라미터를 활용하여 유연한 라우팅을 구현
- HTTP 메서드 처리: 다양한 HTTP 요청 메서드(GET, POST, PUT, DELETE 등)에 따른 로직 작성
- 다양한 응답 도우미 함수: res.json(), res.send(), res.status() 등과 같은 여러 함수 제공
- 복잡한 로직 제한: 복잡한 백엔드 로직이나 데이터 처리를 위해서는 외부 서버나 클라우드 함수가 필요
- 고급 기능 제한: 복잡한 인증, 보안, 데이터베이스 연결과 같은 고급 기능을 구현하기에는 한계