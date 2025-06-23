---
layout: post
title: "react query iniginiteQuery"
summary: "무한스크롤 해보자"
author: yoo94
date: "2024-11-17 11:32:23 +0530"
category: ["nextJs"]
tags:
  - nextJs
  - react-query
  - react
thumbnail:
permalink: blog/react-query3/
---

## 무한 스크롤이란?

무한 스크롤 (infinite scroll): 사용자 경험을 개선하기 위해 페이지 로딩 없이 스크롤을 통해 추가 데이터를 로드하는 기법

페이지의 하단에 도달할 때 새로운 데이터를 가져와서 보여 줌
사용자가 스크롤을 위아래로 움직일 때 이벤트를 감지하고 추가 데이터를 가져오는 로직을 수행
React Query의 Infinite Queries를 사용해서 무한 스크롤을 구현할 수 있음

공식 문서: tanstack.com/query/v4/docs/react/guides/infinite-queries

## React Query의 infiniteQuery란?

- 무한 스크롤: 웹 애플리케이션에서 여러 페이지의 데이터를 동적으로 로드하는 기술
- React Query의 Infinite Query: 무한 스크롤을 지원하고, 화면 스크롤을 통해 추가 데이터를 자동으로 로드할 수 있는 강력한 기능
- Pagination 작업을 간소화하고, 데이터를 무한으로 스크롤링할 때 필요한 다양한 도구와 기능을 제공
- 사용자 경험을 향상시키며, 데이터를 효율적으로 로딩할 수 있음

```tsx
const {
  data,
  error,
  fetchNextPage,
  hasNextPage,
  isFetching,
  isFetchingNextPage,
  status,
} = useInfiniteQuery({
  queryKey: ["projects"],
  queryFn: fetchProjects,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
});
```

### React Query의 infiniteQuery 기능

- React Query가 설치된 프로젝트에서, 아래와 같이 React Query를 사용하여 Infinite Query를 생성
- fetchPosts: 페이지별로 데이터를 가져오는 역할
- getNextPageParam: 콜백 함수를 사용해서 다음 페이지를 정의

```tsx
import { useInfiniteQuery } from "react-query";

const fetchPosts = async ({ pageParam = 1 }) => {
  const response = await fetch(`/api/posts?page=${pageParam}`);
  return response.json();
};

const { data, fetchNextPage, hasNextPage } = useInfiniteQuery(
  "posts", // 고유한 쿼리 키
  fetchPosts, // 데이터 가져오는 비동기 함수
  {
    getNextPageParam: (lastPage, pages) => lastPage.nextPage, // 다음 페이지 파라미터 추출
  }
);
```

### React Query의 infiniteQuery 사용법

- 아래 예시: 데이터를 사용해서 UI를 그리고, 무한 스크롤을 수동으로 제어할 수 있는 버튼 생성

- data.pages를 통해 페이지별로 데이터를 렌더링
- fetchNextPage 함수를 호출하여 다음 페이지의 데이터를 가져옴
- hasNextPage와 isFetching을 사용하여 무한 스크롤 버튼을 제어

```tsx
return (
  <div>
    {data.pages.map((page, pageIndex) => (
      <div key={pageIndex}>
        {page.posts.map((post) => (
          <div key={post.id}>{post.title}</div>
        ))}
      </div>
    ))}

    {hasNextPage ? (
      <button onClick={() => fetchNextPage()} disabled={isFetching}>
        {isFetching ? "로딩 중..." : "더 불러오기"}
      </button>
    ) : null}
  </div>
);
```

### React Query의 infiniteQuery 사용법 2

- Intersection Observer를 활용해서, 특정 영역에 도달했을 때 다음 페이지를 가져오는 무한 스크롤 구현
- useIntersectionObserver 훅을 생성해서 리스트 하단에 도달했는지 (isIntersecting) 확인
- 만약 페이지 하단에 도달하고, 다음 페이지가 있다면 리액트 쿼리의 fetchNextPage() 함수 호출
- 마지막 페이지에 다다를 때까지 위 단계를 반복

```tsx
import useIntersectionObserver from "@hooks/useIntersectionObserver";
import { useInfiniteQuery } from "react-query";

const listRef = useRef<HTMLDivElement | null>(null);
const listEnd = useIntersectionObserver(listRef, {});
const isEndPage = !listEnd?.isIntersecting;

useEffect(() => {
  if (isEndPage && hasNextPage) {
    fetchNextPage();
  }
}, [fetchNextPage, hasNextPage, isEndPage]);
```

#### Infinite Queries 주요 개념

- data: Infinite Query 결과와 데이터
- data.pages: 가져온 페이지들의 배열
- data.pageParams: 페이지를 가져오기 위한 페이지 매개 변수, 배열의 형태
- fetchNextPage, fetchPreviousPage: 다음 페이지 및 이전 페이지의 데이터를 가져오는 함수
- getNextPageParam, getPreviousPageParam: 다음 및 이전 페이지에 대한 매개 변수를 생성하는 함수
- hasNextPage, hasPreviousPage: 다음 페이지 및 이전 페이지가 있는지 여부를 나타내는 불리언 값
- isFetchingNextPage, isFetchingPreviousPage: 다음 페이지 또는 이전 페이지의 데이터를 가져오는 동안 로딩 상태를 나타내는 불리언 값

---

## Intersection Observer란?

- Intersection Observer: 브라우저의 viewport와 원하는 요소의 교차점을 관찰하며, 요소가 뷰포트에 포함되거나 아닌지 구별하는 기능
- 비동기적으로 실행되기 때문에, 메인 스레드에 영향을 주지 않으면서 요소들의 변동상황 관찰
- Scroll 및 getBoundingClientRect의 성능 문제를 해결
- 또한, IntersectionObserverEntry 등의 속성을 활용해서 요소들의 위치를 알 수 있음
- 여러 상황에서 Intersection Observer를 사용할 수 있음:

- 페이지 스크롤 되는 도중에 발생하는 이미지 지연 로딩
- 자동으로 페이지 하단에 스크롤 했을 때 무한스크롤 구현
- 광고 수익 계산을 위한 광고 및 가시성 보고

```tsx
// IntersectionObserver 등록
const io = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    // 관심 대상이 viewport 안에 들어온 경우 'active' 클래스 추가
    if (entry.intersectionRatio > 0) {
      entry.target.classList.add("active");
    } else {
      // 그 외의 경우 'active' 클래스 제거
      entry.target.classList.remove("active");
    }
  });
});

// 관찰할 대상을 선택하고, 해당 속성을 관찰
const boxList = document.querySelectorAll(".box");
boxList.forEach((el) => {
  io.observe(el);
});
```

### Intersection Observer Options 알아보기

- Intersection Observer는 Options를 통해 관찰이 시작되는 상황에 대한 옵션을 설정할 수 있음
- root: 대상 객체(target)의 가시성을 확인할 때 사용되는 뷰포트 요소
- rootMargin: root가 가진 바깥 여백(Margin). margin 값을 이용해 root 범위를 확장/축소할 수 있음
  예시: "10px 20px 30px 40px" (top, right, bottom, left). 기본값은 0
- threshold: observer의 콜백이 실행될 대상 요소(target)의 가시성이 얼마나 필요하거나 나타내는 값

```tsx
// Options를 설정하고 적용하는 예제
let options = {
  root: document.querySelector("#scrollArea"),
  rootMargin: "0px",
  threshold: 1.0,
};

let observer = new IntersectionObserver(callback, options);
```

### Intersection Observer 기본 문법

- Intersection Observer API는 다음과 같은 상황에 콜백 함수를 호출:

- 대상(target) 요소가 기기 뷰포트나 특정 요소(이 API에서 이를 root 요소 혹은 root로 칭함)와 교차할 때
- **관찰자(observer)**가 최초로 타겟을 관측하도록 요청할 때
- IntersectionObserver() 생성자는 두 개의 인수 (callback, options)를 받는다.

- callback: 관찰할 대상(target)이 등록되거나, 가시성에 변화가 생기면 실행된다. 두 개의 인수 (entries, observer)를 받는다.
- Options: 관찰이 시작되는 상황에 대한 옵션을 설정할 수 있음 (root, rootMargin, threshold)

```tsx
// observer 초기화
let io = new IntersectionObserver(callback, options);
io.observe(element); // 관찰 대상 등록
```

### Intersection Observer Callback: Entry 속성

- IntersectionObserverEntry는 읽기 전용의 여러 가지 속성들을 포함:
- boundingClientRect: 관찰 대상의 경계 사각형을 DOMRectReadOnly로 반환
- intersectionRect: 관찰 대상의 교차한 영역 정보를 DOMRectReadOnly로 반환
- intersectionRatio: 관찰 대상의 교차한 영역의 비율을 0.0과 1.0 사이의 숫자로 반환
- isIntersecting: 관찰 대상이 교차 상태인지 아닌지 반 (Boolean)
- rootBounds: 지정한 루트 요소의 사각형 정보를 DOMRectReadOnly로 반환
- target: 관찰 대상 요소 (Element) 반환
- time: 변경이 발생한 시간 정보 (DOMHighResTimeStamp) 반환

```tsx
let callback = (entries, observer) => {
  entries.forEach((entry) => {
    // Each entry describes an intersection change for one observed target element:
    entry.boundingClientRect;
    entry.intersectionRatio;
    entry.intersectionRect;
    entry.isIntersecting;
    entry.rootBounds;
    entry.target;
    entry.time;
  });
};
```

### Intersection Observer 메서드

- observe: 대상 요소(target)의 관찰을 시작할 때 사용
- unobserve: 대상 요소의 관찰을 중지할 때 사용. 관찰을 중지할 하나의 대상 요소를 인수로 지정해야 함
- disconnect: IntersectionObserver 인스턴스가 관찰하는 모든 요소의 관찰을 중지할 때 사용

```tsx
const io = new IntersectionObserver(callback, options);

const div = document.querySelector("div");
const li = document.querySelector("li");

io.observe(div); // div 요소 관찰 시작
io.observe(li); // li 요소 관찰 시작

io.unobserve(div); // div 요소 관찰 중지
io.unobserve(li); // li 요소 관찰 중지

io.disconnect(); // io가 관찰하는 모든 요소 (div, li) 관찰 중지
```

### Intersection Observer hook 예시

참고: https://usehooks-ts.com/
elementRef, options 두 개의 인수를 받아, Intersection Observer API를 사용하여 DOM 요소의 가시성을 감시하고 관찰 결과를 반환하는 훅

```tsx
import { RefObject, useEffect, useState } from "react";

function useIntersectionObserver(
  elementRef: RefObject<Element>,
  { threshold = 0.1, root = null, rootMargin = "0%" }: IntersectionObserverInit
) {
  const [entry, setEntry] = useState<IntersectionObserverEntry | undefined>();

  const updateEntry = (entry: IntersectionObserverEntry[]) => {
    setEntry(entry);
  };

  useEffect(() => {
    const node = elementRef?.current;
    const hasIOSupport = !!window.IntersectionObserver;

    if (!hasIOSupport || !node) return;

    const observerParams = { threshold, root, rootMargin };
    const observer = new IntersectionObserver(updateEntry, observerParams);

    observer.observe(node);

    return () => observer.disconnect();

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [elementRef?.current, JSON.stringify(threshold), root, rootMargin]);

  return entry;
}

export default useIntersectionObserver;
```

---

## js로 구현

Javascript에서 무한 스크롤 구현 방법: addEventListener()에 scroll 이벤트를 이용해서 구현
또한, getBoundingClientRect() 메서드로 원하는 특정 위치에서 다음 페이지를 가져오도록 구현
하지만, 위 코드들은 성능 문제를 발생시킴.
scroll 이벤트: 단시간에 수백번 호출되며 동기적으로 실행
getBoundingClientRect 메서드: 계산을 할 때마다 리플로우 현상이 일어나며 성능 저하
해결 방법: Intersection Observer를 사용해 비동기적으로 교차점 관찰

```js
// 빈 리스트 선택
const listElem = document.querySelector("#infinite-list");
let nextItem = 1;

// 20개의 아이템 추가 함수
const loadMore = function () {
  for (let i = 0; i < 20; i++) {
    let item = document.createElement("li");
    item.innerText = "List Item #" + nextItem++;
    listElem.appendChild(item);
  }
};

// ul 리스트 바닥까지 스크롤 했는지 확인
listElem.addEventListener("scroll", function () {
  if (listElem.scrollTop + listElem.clientHeight >= listElem.scrollHeight) {
    loadMore();
  }
});

// 아이템 20개씩 더 가져오는 loadMore 함수 실행
loadMore();
```
