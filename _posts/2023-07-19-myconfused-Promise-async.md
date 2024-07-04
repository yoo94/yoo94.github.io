---
layout: post
title:  "js Promise와 async/await"
summary: "차이점과 주의점, 비동기의 필요이유?"
author: yoo94
date: '2024-07-19 15:35:23 +0530'
category: ['myconfused','javaScript']
tags: Promise,async,await
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Fxemoji_u2049.svg/255px-Fxemoji_u2049.svg.png
permalink: /blog/Promise-async-await/
---
### 비덩기 처리가 필요한 이유?

Js는 싱글스레드 언어이기 대문에 한번에 하나만 처리할 수 있다.
그렇기 때문에 특정 코드의 실행이 완료될 때까지 기다리지 않고 다음 코드를 실행하는 비동기 처리는 필수적이다.
예를 들어 서버에서 데이터를 가져오는 작업시간이 오래걸리는데 이때 비동기가 아니라면 모든 데이터가 다 들어올때가지 다른작업을 수행 할 수 없게된다.

#### 등장 전에는?
콜백패턴을 이용하여 비동기 처리를 하였고, 콜백지옥을 만들었다.

## Promise
Promise는 비동기 작업의 완료 또는 실패를 나타내는 객체
.then(), .catch(), .finally() 메서드를 사용

```javascript

const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data received');
    }, 2000);
  });
};

fetchData()
  .then(data => {
    console.log(data); // "Data received" (2초 후 출력)
  })
  .catch(error => {
    console.error(error);
  });
```

## async/await
async/await는 Promise를 더 쉽게 사용할 수 있도록 하는 문법
async 키워드를 함수 앞에 붙이면 그 함수는 항상 Promise를 반환
await 키워드는 Promise가 처리될 때까지 기다렸다가 결과를 반환

```javascript
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data received');
    }, 2000);
  });
};

const getData = async () => {
  try {
    const data = await fetchData();
    console.log(data); // "Data received" (2초 후 출력)
  } catch (error) {
    console.error(error);
  }
};

getData();
```

## 주요 차이점

### 가독성:
- Promise 체이닝은 .then(), .catch() 메서드를 사용해 비동기 작업을 처리.
- async/await는 동기 코드처럼 보이도록 작성할 수 있어 가독성이 좋아요.

### 에러 처리:
- Promise에서는 .catch()를 사용해 에러를 처리
- async/await에서는 try/catch 블록을 사용해 에러를 처리

## async/await 주의점
1. 비동기 함수는 항상 프로미스를 반환한다.
2. await는 async 안에서만 사용 가능하다.
3. 에러 핸들링을 try catch문으로 해야한다.
4. 여러 비동기 작업을 병렬로 실행하려면 Promise.all을 사용하여 최적화할수있다.
5. await는 함수의 실행을 일시 중지하고 실행되므로, 긴 작업에서 코드가 블로킹 되지않도록 해야한다.
   동기 처리를 하였고, 콜백지옥을 만들었다.

###