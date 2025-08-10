---
layout: post
title: "react hook useMemo"
summary: "최적화: Memoization된 값을 반환"
author: yoo94
date: "2024-02-27 04:35:23 +0530"
category: Frontend2
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-hook-useMemo/
---

##### 컴포넌트가 리렌더링 될때 계산량이 많은 연산을 효율적으로 관리하여 불필요한 연산을 방지한다. 연산결과를 메모리에 저장하고,

##### 의존성 배열의 값이 변경 될때만 연산을 다시 수행한다.

- usecallback은 함수를 저장 이건 값을 저장

###### 언제 사용? : 이미 계산 해 본 연산 결과를 기억 해 두었다가 동일한 계산을 시키면, 다시 연산하지 않고 기억 해 두었던 데이터를 반환 시키게 하는 최적화 방법

![이미지](/blog/postImg/Pasted image 20240204155203.png)

#### useMemo

react 에서 제공하는 기본 메소드이다.

1.  첫 번째 인자로 함수를 넣는다. 이 함수에서 반환하는 return을 기억 하고 있게 된다.
2.  두 번째 인자로 배열을 넣는다. 배열에 있는 값 중에 상태나 값이 변하게 되면 함수를 다시 호출하게 된다.

##### 3. 즉 배열에 값이 변하지 않으면 계산하지 않고 처음 계산한 값을 그대로 다시 반환하게 된다.

#### 그리고 가장 중요한 것은 아래처럼 함수가 아니라 변수로 값을 가지고 오듯이 사용해야 한다.

```jsx
import "./List.css";
import TodoItem from "./TodoItem";
import { useState, useMemo } from "react";

const List = ({ todos, onUpdate, onDelete }) => {
  const [search, setSearch] = useState("");
  const onChangeSearch = (e) => {
    setSearch(e.target.value);
  };

  const getFilteredDAta = () => {
    if (search === "") return todos;
    return todos.filter((todo) => {
      return todo.content.toLowerCase().includes(search.toLowerCase());
    });
  };

  const filteredTodos = getFilteredDAta();

  // useMemo없이 사용 - list컴포넌트가 렌더링 될 때마다 계속 계산해서 렌더링됨, 단순히 list 갯수가 변할 때만 렌더링 하면 되기 떄문 search 같은 다른 state가 변경 됐을때는 굳이 다시 계산할 필요가 없음
  const getAnalyzedData = () => {
    const totalCount = todos.length ?? 0;
    const doneCount =
      todos.filter((todo) => {
        return todo.isDone;
      }).length ?? 0;
    const notDoneCount = Number(totalCount) - Number(doneCount) ?? 0;
    return { totalCount, doneCount, notDoneCount };
  };
  const { totalCount, doneCount, notDoneCount } = getAnalyzedData();
  //--------------------------------------
  //useMemo 사용하면 todos가 바뀔때만 하고 렌더링 할때는 실행을 안하고 메모이제이션 되어있는 상태값을 반환하여 계산을 다시 할 필요 없게 함
  const { totalCount, doneCount, notDoneCount } = useMemo(() => {
    const totalCount = todos.length ?? 0;
    const doneCount =
      todos.filter((todo) => {
        return todo.isDone;
      }).length ?? 0;
    const notDoneCount = Number(totalCount) - Number(doneCount) ?? 0;
    return { totalCount, doneCount, notDoneCount };
  }, [todos]);

  return (
    <div className="List">
      <h4>Todo List</h4>
      <div>total : {totalCount}</div>
      <div>done : {doneCount}</div>
      <div>notDone : {notDoneCount}</div>
      <input
        placeholder="검색어를 입력하세요"
        value={search}
        onChange={onChangeSearch}
      />
      <div className="todos_wrapper">
        {filteredTodos.map((todo) => {
          return (
            <TodoItem
              key={todo.id}
              {...todo}
              onUpdate={onUpdate}
              onDelete={onDelete}
            />
          );
        })}
      </div>
    </div>
  );
};

export default List;
```
