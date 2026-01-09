---
layout: post
title: "알고리즘 : DP Dynamic Programming"
summary: "복잡한 문제를 더 작은 부분 문제로 나누어 해결하는 알고리즘 기법"
author: yoo94
date: "2025-10-01 18:30:23 +0530"
category: Algorithm
keywords: 알고리즘,DP,Dynamic Programming,코딩테스트,문제풀이,프로그래밍
tags:
  - 알고리즘
  - DP
  - DynamicProgramming
  - 코딩테스트
  - 문제풀이
  - 자료구조
  - 프로그래밍
  - JavaScript
  - Python
  - 개발자
thumbnail: /blog/postImg/dp.png
permalink: blog/dp-dynamic-programming/
---

![/blog/postImg/dp.png](/blog/postImg/dp.png)

## 다이나믹 프로그래밍에 대하여

나만 이해하면 돼서, 대충 쓰지만 읽는 사람도 이해했으면 하는 마음도 담아서 작성한다.

### 목차
1. [다이나믹 프로그래밍이란?](#1-다이나믹-프로그래밍이란)
2. [다이나믹 프로그래밍 말고 비슷한게 있던거같은데..?](#2-다이나믹-프로그래밍-말고-비슷한게-있던거같은데)
3. [다이나믹 프로그래밍은 언제 쓸까](#3-다이나믹-프로그래밍은-언제-쓸까)
4. [내가 이해하기 위한 다이나믹 프로그래밍](#4-내가-이해하기-위한-다이나믹-프로그래밍)

---

## 1-다이나믹 프로그래밍이란?

다이나믹 프로그래밍(Dynamic Programming, DP)은 **큰 문제를 작은 부분 문제로 나누어 해결**하는 알고리즘 기법이다.

핵심은 **한 번 계산한 결과를 저장해두고 재사용**하는 것이다. 이를 통해 불필요한 중복 계산을 피하고 효율성을 높일 수 있다.

### DP의 핵심 원리

1. **메모이제이션(Memoization)**: 계산한 결과를 메모리에 저장
2. **최적 부분 구조(Optimal Substructure)**: 큰 문제의 최적해가 작은 문제의 최적해로 구성됨
3. **중복되는 부분 문제(Overlapping Subproblems)**: 같은 작은 문제들이 반복해서 나타남

간단한 예로 [피보나치 수열](https://ko.wikipedia.org/wiki/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98_%EC%88%98)을 생각해보자:

```javascript
// 일반 재귀 (비효율적)
function fib(n) {
  if (n <= 1) return n;
  return fib(n-1) + fib(n-2); // 같은 계산을 반복
}

// DP 적용 (효율적)
function fibDP(n) {
  const memo = [0, 1];
  for (let i = 2; i <= n; i++) {
    memo[i] = memo[i-1] + memo[i-2];
  }
  return memo[n];
}
```

---

## 2-다이나믹 프로그래밍 말고 비슷한게 있던거같은데..?

맞다! **재귀(Recursion)** 가 떠올랐을 것이다.

사실 DP는 재귀의 개선 버전이라고 볼 수 있다. 둘 다 "큰 문제를 작은 문제로 나눈다"는 점에서 같지만, 중요한 차이가 있다.

### 일반 재귀 vs DP

같은 피보나치 문제를 두 방식으로 보자:

```javascript
// 일반 재귀 (비효율적)
function fibRecursive(n) {
  if (n <= 1) return n;
  return fibRecursive(n-1) + fibRecursive(n-2);
}

// 문제점: fib(5)를 구할 때
// fib(3)을 2번, fib(2)를 3번, fib(1)을 5번 계산!
```

```javascript
// DP (메모이제이션)
function fibDP(n, memo = {}) {
  if (n in memo) return memo[n];  // 이미 계산했으면 바로 반환
  if (n <= 1) return n;
  
  memo[n] = fibDP(n-1, memo) + fibDP(n-2, memo);
  return memo[n];
}

// 각 값을 딱 한 번만 계산!
```

### 시간 복잡도 차이

| 구분 | 일반 재귀 | DP |
|------|----------|-----|
| **시간 복잡도** | O(2^n) 😱 | O(n) 😊 |
| **fib(40) 계산** | 약 10억 번 호출 | 40번 호출 |
| **특징** | 같은 계산 반복 | 한 번만 계산 후 저장 |

### 실제 성능 차이

```javascript
console.time('재귀');
fibRecursive(40);  // 수 초 소요
console.timeEnd('재귀');

console.time('DP');
fibDP(40);  // 즉시 완료
console.timeEnd('DP');
```

**핵심**: 재귀는 직관적이지만 중복 계산이 많고, DP는 메모이제이션으로 이를 해결한다!

---

## 3-다이나믹 프로그래밍은 언제 쓸까

DP를 사용하기 좋은 경우를 판단하는 기준:

### ✅ DP를 사용해야 하는 신호

1. **최적화 문제**: "최대", "최소", "최적"이라는 단어가 나올 때
   - 최소 비용, 최대 이익, 최단 경로 등

2. **경우의 수 세기**: "몇 가지 방법", "몇 개"
   - 계단 오르기 방법의 수, 조합의 수 등

3. **부분 문제가 중복**: 같은 계산을 여러 번 하는 경우

### 대표적인 DP 문제 유형

#### 1. 피보나치 수열
```javascript
// Top-down (재귀 + 메모이제이션)
function fib(n, memo = {}) {
  if (n in memo) return memo[n];
  if (n <= 1) return n;
  memo[n] = fib(n-1, memo) + fib(n-2, memo);
  return memo[n];
}
```

#### 2. 계단 오르기 ([LeetCode 문제](https://leetcode.com/problems/climbing-stairs/))
```javascript
function climbStairs(n) {
  if (n <= 2) return n;
  
  const dp = new Array(n + 1).fill(0);
  dp[1] = 1;
  dp[2] = 2;
  
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i-1] + dp[i-2];
  }
  
  return dp[n];
}
```

#### 3. 배낭 문제 (Knapsack)
무게 제한이 있는 가방에 최대 가치를 담는 문제

```javascript
function knapsack(weights, values, capacity) {
  const n = weights.length;
  const dp = Array(n + 1).fill(0).map(() => Array(capacity + 1).fill(0));
  
  for (let i = 1; i <= n; i++) {
    for (let w = 0; w <= capacity; w++) {
      if (weights[i-1] <= w) {
        dp[i][w] = Math.max(
          dp[i-1][w],
          dp[i-1][w - weights[i-1]] + values[i-1]
        );
      } else {
        dp[i][w] = dp[i-1][w];
      }
    }
  }
  
  return dp[n][capacity];
}
```

### 접근 방법

1. **Top-down (하향식)**: 재귀 + 메모이제이션
   - 직관적이고 이해하기 쉬움
   - 스택 오버플로우 위험

2. **Bottom-up (상향식)**: 반복문 + 테이블
   - 효율적이고 안전함
   - 초기 설정이 복잡할 수 있음

---

## 4- 내가 이해하기 위한 다이나믹 프로그래밍 

### 시작

##### DP의 핵심 전략: '기억하기'

DP를 적용하려면, 문제와 똑같이 생긴 빈 공간(저장소)을 하나 더 만들어야 한다.

### 점화식

##### DP가 똑똑해지는 원리

한 단계가 끝날 때마다, 그 줄까지 도달하는 최적의 답만 남긴다.
즉 다음단계로 갈때는 바로 윗 단계의 최적의 답만 참고하면 된다.

DP는 큐나 스택처럼 정형화된것이 아닌, 수행시간을 줄이는 기법이다.
그래서 정해진 구조는 없고 문제마다 사람마다 풀이가 다르다.ㅣ
가장 좋은건 dp적 사고 방식을 익히며 많은 문제를 풀어보는것이다.

### 마무리

진짜 거지같다 ㅎ_ㅎ