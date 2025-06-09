---
layout: post
title: "프론트엔드 최적화 1. lighthouse "
summary: "lighthouse 패널을 사용하자"
author: yoo94
date: '2025-01-05 10:32:23 +0530'
category: ['FEoptimize']
tags:
  - lighthouse
  - 프론트엔드
  - 최적화
  - front end optimization
thumbnail: 
permalink: blog/optimization_1/lighthouse/
---

# Lighthouse 사용법

개발자도구에 있음

### Mode

- Navigation
    - 기본값, 초기 페이지 로딩 시 발생하는 성능 분석
- Timespan
    - 사용자가 정의한 시간 동안 발생한 성능 분석
- Snapshot
    - 현재 상태의 성능 문제를 분석

### Categories

- Performance
    - 로딩 과정에서 발생하는 문제 분석
- Accessibility
    - 서비스의 사용자 접근석 문제 분석
- Best practices
    - 웹사이트의 보안 측면과 최신 표준으로 분석
- SEO
    - 검색엔진 분석
- PWA
    - 서비스 워커와 오프라인 동장 등, pwa관련 분석

---

## 웹 바이탈

종합 점수 : 64점

<img src="/blog/postImg/bital1.png" alt="bital1.png" style="max-width:100%;">

<img src="/blog/postImg/bital2.png" alt="bital2.png" style="max-width:100%;">


### FCP ( First Conentful Paint) - 가중치 : 10%

- 페이지가 로드 될 때 브라우저가 DOM 콘텐츠의 첫 번째 부분을 렌더링 하는 데 걸리는 시간에 관한 지표이다.

### SI ( Speed Index) - 가중치 : 10%

- 페이지 로드 중에 콘텐츠가 시각적으로 표시되는 속도

- 전체가 다 보이는것도 중요하지만, 일부 콘텐츠가 더 빨리 보이는 등에 대한 요소도 계산됨

### LCP ( Largest Contentful Paint) - 가중치 25%

- 페이지가 로드 될 때 화면 내에 있는 가장 큰 이미지나 텍스트요소가 렌더링 되기까지의 시간을 나타냄.

### TBT( Total Blocking Time ) - 가중치 30%

- 페이지가 사용자와 상호작용을 못하게 차단된 시간의 총합

### CLS ( Cumulative Layout Shift ) - 가중치 15%

- 페이지 로드 과정에서 발생하는 레이아웃 이동을 측정, 화면상에서 요소의 위치나 크기가 순간적으로 변하는 등에 대한 지표

### TTI ( Time to Interactive) - 가중치 10% (현재 사용안함)

- 사용자가 페이지와 상호작용이 가능한 시점까지의 시간 ( 클릭 또는 키보드 누름)

<img src="/blog/postImg/TTI1.png" alt="TTI.png" style="max-width:100%;">

## **Diagnostics**

- 로드 속도와 직접적인 관계는 없지만 성능과 관련된 기타 정보

<img src="/blog/postImg/Diagnostics.png" alt="Diagnostics.png" style="max-width:100%;">

- Emulated Desktop with Lighthouse 12.2.1 - CPU 성능에 제한을 뒀는지 1x(제한안둠) 4x(제한둠 보통 모바일)
