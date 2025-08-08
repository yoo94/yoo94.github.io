---
layout: post
title: "프론트엔드 최적화 2. 병목코드 퇴치 "
summary: "코드분할과 지연로딩"
author: yoo94
date: "2025-01-10 10:32:23 +0530"
category: Frontend3
tags:
  - 병목코드
  - 코드분할
  - 지연로딩
  - 프론트엔드
  - 최적화
  - front end optimization
thumbnail:
permalink: blog/optimization_1/bottleneck/
---

# 병목코드 개발자 도구로 분석

### Performance 패널 살펴보기

**Diagnostics 에서** Reduce JavaScript execution time

<img src="/blog/postImg/bottleneck1.png" alt="bottleneck1.png" style="max-width:100%;">

…chunks/framework-e651e4d700632ed4.js 이게 오랫동안 실행되었고 느려진 원인이라는것은 알겠다.

<img src="/blog/postImg/bottleneck2.png" alt="bottleneck2.png" style="max-width:100%;">

퍼포먼스 패널로가서 새로고침을 누르면 다음과 같이 결과가 나온다.

<img src="/blog/postImg/bottleneck3.png" alt="bottleneck3.png" style="max-width:100%;">

<img src="/blog/postImg/bottleneck4.png" alt="bottleneck4.png" style="max-width:100%;">

---

## 1. CPU, Network, 스크린샷 차트

### CPU

시간에 따라 cpu가 어떤 작업에 리소스를 사용하고 있는지 비율

- js사용 : 노란색
- 렌더링 레이아웃 : 보라색
- 페인팅 : 초록색
- 기타 : 회색

빨간색 부분들은 병목이 발생하고 있는 지점. 즉 특정 작업이 메인 스레드를 오랫동안 잡아 두고 있다 라는 뜻.

<img src="/blog/postImg/bottleneck5.png" alt="bottleneck5.png" style="max-width:100%;">

### Network

대략적인 네트워크 상태 표시

네트워크 타임라인은 서비스 로드 과정에서의 요청을 시간 순서에 따라 보여준다.

- 왼쪽회색 선 : 초기 연결시간
- 막대에 옅은색 영역 : 요청을 보낸 시점부터 응담을 기다리는 시점까지의 시간 TTFB time to first byte
- 막대에 짙은 영역 : 콘텐츠 다운로드 시간
- 오른쪽 회색 선: 해당 요청에 대한 메인 스레드의 작업 시간

---

<img src="/blog/postImg/bottleneck6.png" alt="bottleneck6.png" style="max-width:100%;">

### frames, timings, main

- frames 섹션은 화면의 변화가 있을 때마다 스샷을 찍어 보여준다.
- timings 섹션은 user timing api롤 통해 기록된 정보를 기록한다. 여기 표시된 막대들은 컴포넌트의 렌더링 시간을 측정
- main 섹션은 브라우저의 메인 스레드에서 실행되는 작업을 플레임 차트로 보여줌, 어떤 작업이 오래걸리는지 파악 할 수 있다.

## 하단탭

<img src="/blog/postImg/bottleneck7.png" alt="bottleneck7.png" style="max-width:100%;">

- summary : 선택 영역에서 발생한 작업시간의 총합과 각 작업이 차지하는 비중
- bottom-up : 가장 최하위에 있는 작업부터 상위 작업까지 역순으로
- call tree : 가장 최상위부터 하위로
- event log : 발생한 이벤트 - loading, experience, scripting, rendering, painting

---

<img src="/blog/postImg/bottleneck7.png" alt="bottleneck7.png" style="max-width:100%;">

네트워크, 타이밍, 메인 탭을 눌러보면서 어떤 실행에서 얼만큼 걸리는지 파악하고

제일 오래 걸리는 부분이나 빨간색 표시된 부분을 확인하면서 처리를 해야한다.

<img src="/blog/postImg/bottleneck8.png" alt="bottleneck8.png" style="max-width:100%;">

현재는 app.js가 가장 오래 걸린다.
