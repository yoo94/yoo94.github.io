---
layout: post
title: "react query"
summary: "비동기 작업을 위한 라이브러리"
author: yoo94
date: '2024-11-16 18:32:23 +0530'
category: ['nextJs']
tags:
  - nextJs
  - react-query
  - react
thumbnail: 
permalink: blog/react-query/
---

## React-Query

##### React 앱에서 데이터를 관리하고 비동기 작업을 처리하기 위한 강력한 라이브러리

#### 제공 기능

- 데이터 관리: 서버에서 데이터를 가져와 컴포넌트에서 사용할 수 있게 함
- 비동기 작업: 비동기 작업을 수행하고, 데이터를 로딩하며, 캐시하고, 에러 처리를 단순화

- 데이터 캐싱: 불필요한 데이터 요청을 피하기 위해 자동으로 데이터를 캐싱
- 상태 관리: 컴포넌트에서 데이터 로딩 상태, 에러 상태 및 데이터를 관리하고 업데이트할 수 있음
- 비동기 데이터 가져오기: useQuery 훅을 사용하여 서버에서 데이터를 비동기적으로 가져올 수 있음
- 뮤테이션: useMutation 훅을 사용하여 데이터 업데이트, 생성 및 삭제를 처리할 수 있음
- 상태 유지: 컴포넌트 간에 데이터를 공유하고 동기화할 수 있으며, 페이지 간에 데이터를 유지할 수 있음

#### 장점

- 데이터 관리 용이성
- 성능 향상
- 개발 생산성
- 서버 상태 관리
- 테스트 용이성

---

### 기능

1. 데이터 가져오기와 캐싱

useQuery 함수를 사용하여 데이터 불러오기, 자동 캐싱, 중복 요청 방지 가능

```ts
import { useQuery } from 'react-query';

function MyComponent() {
  const { data } = useQuery('querykey', fetchDataFunction);
  // 쿼리 키를 기준으로 캐싱되기 때문에 여러개 사용하면 데이터마다 각각 쿼리키를 다르게 줘야한다.
}
```

2. 자동 리페치

데이터를 주기적으로 업데이트해야 하는 경우, refetchInterval 옵션을 사용하여 설정 가능
```ts
const { data } = useQuery('myData', fetchDataFunction, {
  refetchInterval: 10000, // 10 seconds
});

```

3. 뮤테이션

데이터 변경 작업(생성, 수정, 삭제)을 간단하게 수행할 때 사용 가능
```ts
import { useMutation } from 'react-query';

function MyComponent() {
  const { mutation } = useMutation(createDataFunction);
  // ...
}

```

---

### React Query 캐싱

데이터를 가져와서 처음 한 번 캐싱하면, 이후 동일한 데이터에 대한 요청은 네트워크 요청을 보내지 않고 캐시된 데이터를 사용,
fetch만을 사용한다 했을 때, 새로고침이나 앞뒤로 왓다갔다할때마다 api를 새로 호출하기 때문에 비효율적이다.

#### staleTime 옵션

React Query에서 사용되는 중요한 옵션 중 하나로, 캐시된 데이터의 "잘못된" 상태(stale state)를 얼마 동안 허용할지 설정하는 데 사용

```ts
import { useQuery } from 'react-query';

function MyComponent() {
  const { data } = useQuery('myData', fetchDataFunction, {
    staleTime: 60000, // 60 seconds
  });
  // ...
}
```

#### 잘못된 상태란?

데이터가 업데이트되었지만, 이전에 캐싱된 데이터가 여전히 사용 가능한 상태
staleTime은 기본적으로 0으로, 데이터가 한 번 불러와지면 다음 요청 시에는 항상 새로운 데이터를 가져옴

---

## React Query 주요 함수

#### useQuery: 데이터를 가져올 때 사용하는 함수.

데이터를 캐싱하고 자동으로 리패칭 관리. 로딩, 에러, 데이터 등을 처리할 수 있는 옵션 제공.

- isLoading: 데이터 가져오는 중인지 여부
- isError: 데이터 가져오는 중 에러 발생 여부
- data: 성공적으로 데이터를 가져온 경우, 데이터 반환
- error: 데이터 가져오는 중 발생한 에러 정보

```tsx
const { isLoading, isError, data, error } = useQuery('profile', fetchData);

if (isLoading) {
  return <p>Loading...</p>;
}

if (isError) {
  return <p>Error: {error.message}</p>;
}
```

#### useQueryClient: 리액트 쿼리 클라이언트에 접근해서 다양한 작업 수행 가능 (캐시 조작, 캐시 데이터 작업 등).

```tsx
const queryClient = useQueryClient();

// Todo 목록 가져오기
const { data: todos } = useQuery('todos', fetchTodos);

const handleUpdateTodo = (id, text) => {
  // Todo 업데이트 API 호출

  // 다른 쿼리 캐시 갱신: 'todos' 쿼리 다시 로드
  queryClient.invalidateQueries('todos');
};
```

### useMutation: 데이터 변경 작업 수행에 사용

- useMutation 호출하여 mutation 객체 생성. 해당 객체에 함께 사용할 함수 정의.
- 성공 / 실패 여부 처리 가능. 데이터 업데이트 후 리패치 관리.

```tsx
const mutation = useMutation({
  mutationFn: postTodo,
  onSuccess: () => {
    // Invalidate and refetch
    queryClient.invalidateQueries({ queryKey: ['todos'] });
  },
});

return (
  <button onClick={() => {
    mutation.mutate({
      id: Date.now(),
      title: 'Do Laundry',
    });
  }}>
    Add Todo
  </button>
);
```
---

## 세팅방법
#### 최상단 파일(_app.tsx)에 QueryClientProvider로 애플리케이션을 감싸고, queryClient 설정

```tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

// Create a client
const queryClient = new QueryClient()

function App() {
  return (
    // Provide the client to your App
    <QueryClientProvider client={queryClient}>
      <Todos />
    </QueryClientProvider>
  )
}
```

---

### React Query와 Next.js

- React Query는 Next.js 프로젝트에도 유용하게 적용할 수 있음
- SSR을 사용하는 경우, getServerSideProps 혹은 SSG를 사용하는 경우, getStaticProps와 함께 리액트 쿼리를 사용할 수 있음
- React Query로 데이터를 미리 가져와 페이지를 서버에서 렌더링 가능

```tsx
export async function getStaticProps() {
  const posts = await getPosts()
  return { props: { posts } }
}

function Posts(props) {
  const { data } = useQuery({
    queryKey: ['posts'],
    queryFn: getPosts,
    initialData: props.posts,
  })

  // ...
}```