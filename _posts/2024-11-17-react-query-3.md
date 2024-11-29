---
layout: post
title: "react query iniginiteQuery"
summary: "무한스크롤 해보자"
author: yoo94
date: '2024-11-17 11:32:23 +0530'
category: ['nextJs']
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
  queryKey: ['projects'],
  queryFn: fetchProjects,
  getNextPageParam: (lastPage, pages) => lastPage.nextCursor,
});

```


### React Query의 infiniteQuery 기능

- React Query가 설치된 프로젝트에서, 아래와 같이 React Query를 사용하여 Infinite Query를 생성
- fetchPosts: 페이지별로 데이터를 가져오는 역할
- getNextPageParam: 콜백 함수를 사용해서 다음 페이지를 정의

```tsx
import { useInfiniteQuery } from 'react-query';

const fetchPosts = async ({ pageParam = 1 }) => {
  const response = await fetch(`/api/posts?page=${pageParam}`);
  return response.json();
};

const { data, fetchNextPage, hasNextPage } = useInfiniteQuery(
  'posts', // 고유한 쿼리 키
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
        {isFetching ? '로딩 중...' : '더 불러오기'}
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
import useIntersectionObserver from '@hooks/useIntersectionObserver';
import { useInfiniteQuery } from 'react-query';

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