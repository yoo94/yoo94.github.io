---
layout: post
title:  "react hooks 종류"
summary: ""
author: yoo94
date: '2024-03-01 11:35:23 +0530'
category: ['react','myconfused']
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: /blog/react-hooks
---
## 1. useState
   설명: 컴포넌트의 상태를 관리할 수 있게 해준다.
   언제 사용하나요?: 컴포넌트 내에서 동적 상태를 관리할 때 사용합니다.
## 2. useEffect
   설명: 컴포넌트가 렌더링될 때와 업데이트될 때 부수 효과(side effects)를 실행할 수 있게 해준다.
   언제 사용하나요?: 데이터 페칭, 구독 설정, 타이머 설정 등 컴포넌트가 수행해야 하는 부수 효과를 처리할 때 사용합니다.
## 3. useContext
   설명: 컨텍스트(Context)를 사용하여 전역적인 상태를 쉽게 공유할 수 있게 해준다.
   언제 사용하나요?: 전역적으로 상태나 기능을 공유할 때 사용합니다.
## 4. useReducer
   설명: 복잡한 상태 로직을 컴포넌트에서 관리할 수 있게 해준다.
   언제 사용하나요?: 복잡한 상태 로직이나 여러 상태 값이 상호작용할 때 사용합니다.
## 5. useRef
   설명: 변수를 유지하거나 DOM 요소에 접근할 수 있게 해준다.
   언제 사용하나요?: DOM 요소에 접근하거나 상태 변화와 무관하게 유지되어야 하는 값을 관리할 때 사용
## 6. useMemo
   설명: 값의 재계산을 최적화할 수 있게 해준다.
   언제 사용하나요?: 성능 최적화를 위해 비용이 많이 드는 계산의 결과를 재사용할 때 사용
## 7. useCallback
   설명: 함수의 재생성을 최적화할 수 있게 해줍니다.
   언제 사용하나요?: 컴포넌트가 불필요하게 다시 렌더링되는 것을 방지하고 성능을 최적화할 때 사용.
