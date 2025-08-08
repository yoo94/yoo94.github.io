---
layout: post
title: "react axios fetch"
summary: "axios는 fetch API"
author: yoo94
date: "2024-04-08 08:35:23 +0530"
category: Frontend1
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-axios-fetch/
---

## axios

axios는 fetch API와 유사한 Promise 기반 HTTP 클라이언트 라이브러리로 데이터를 동적으로 받아올 수 있습니다. fetch API와 달리 third-party 라이브러리로 **1) 별도의 설치 후 import 하거나** 또는 **2) html 파일에 jsDeliver CDN**을 이용해 사용 가능합니다.

```shell
-----------------
npm install axios
-----------------
```

```jsx
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function News() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await axios.get("https://jsonplaceholder.typicode.com/news");
      return res.data;
    };

    fetchData().then((res) => setData(res));
  }, []);

  return (
    <div>
      {data.map((d) => (
        <Link key={d.id} to={`${d.id}`}>
          {d.title}
        </Link>
      ))}
    </div>
  );
}
```

axios는 fetch API와 달리 json 객체로 변환해주는 과정을 자동으로 해줍니다. 그리고 위의 코드에서 `axios.get` 메서드를 활용해 데이터를 비동기적으로 받아올 수 있습니다. 단, 응답 받은 객체에 data key에 접근하여 접근한 값(`res.data`)을 반환해야 데이터를 활용 가능합니다.

---

## 비동기 fetch

```jsx
const getData = async () => {
  const res = await fetch("url").then((res) => res.json());
};
```

```jsx
//api

const getData = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/comments").then(
    (res) => res.json()
  );

  const initData = res.slice(0, 20).map((itm) => {
    return {
      author: itm.email,
      content: itm.body,
      emotion: Math.floor(Math.random() * 5) + 1,
      create_date: new Date().getTime,
      id: dataId.current++,
    };
  });
  setData(initData);
};

useEffect(() => {
  getData();
}, []);
```

이렇게 useEffect에 빈배열을 넣어두면 렌더링 할 때 자동으로 타게된다.

---

## useEffect + Promise 기반 API 호출 메서드 2가지 활용법

useEffect Hook을 활용하여, 컴포넌트가 최초 렌더링 후 mount될 때 한 번만 데이터를 동적으로 받아올 수 있도록 할 수 있습니다. 이 때, fetch 또는 axios를 이요해서 데이터를 받아옵니다.

> 서버 구축을 통한 데이터를 받아오기 어려운 상황에서, 다음의 사이트에서 fake API를 활용해 화면에 뿌려볼 수 있습니다.

### 01 fetch

```jsx
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

function News() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch("https://jsonplaceholder.typicode.com/news");
      const result = res.json();
      return result;
    };

    fetchData().then((res) => setData(res));
  }, []);

  return (
    <div>
      {data.map((d) => (
        <Link key={d.id} to={`${d.id}`}>
          {d.title}
        </Link>
      ))}
    </div>
  );
}
```
