---
layout: post
title:  "react redux를 쓰는이유"
summary: ""
author: yoo94
date: '2023-08-11 11:35:23 +0530'
category: ['react','myconfused']
tags: react,redux
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/react-redux/
---

본래 React를 쓰면서 'state 끌어올리기'에 부담을 느끼거나, 
불필요한 props drilling 등이 이슈가 되면서 전역적인 state 관리법이 필요해졌고, context api기능을 제공했다.
그러나 간단한 상태 공유에는 적합하지만, 상태 관리가 복잡해지면 코드가 관리하기 어려워졌고
Redux는 상태를 중앙 집중식으로 관리하고, 상태 변화의 예측 가능성을 높일수 있게 되었다.

## 리덕스 개념

### action
상태의 변화가 필요할 때, 발생시키는 객체를 action이라 한다.
추가, 삭제, 수정 등 각각의 액션에 대한 타입정의가 있어야한다.

**즉, 컴포넌트에서 상태를 변화하는게 아니라 리덕스에게 상태를 변경시켜달라고 요청을 하는 것이고, 그 요청을 액션이라한다. **
** 그래서 리덕스는 그 액션에 대한 api(?)를 정해놓고 상태를 변경 시켜주면 된다. 결론 적으론 모든 전역상태 변화는 리덕스에서 하는 것이다. **

```text
{
  type: "ADD",
  data: {
    id: 0,
    text: "redux"
  }
}
```
액션은 Type이 필수적이다.

### Action Creator
액션 생성함수라 불리는 Action Creator는 액션을 만드는 **함수**이다.
파라미터를 입력받아, 액션 객체 형태로 만들어준다.
```javascript
function addTodo(data) {
  return {
    type: "ADD",
    data
  };
}
```
이 함수는 data라는 파라미터를 입력받아, 액션을 객체 형태로 반환하는 역할을 한다.

### Reducer

리듀서는 변화를 일으키는 함수입니다. 이 함수는 이전 상태와 액션을 파라미터로 입력받는다.

```javascript
function reducer(state, action) {
...
return alteredState;
}
```
반환값은 로직에 의해 변화된 상태 값을 반환합니다.

### Store
스토어는 컴포넌트 외부에 있는 상태 저장소다. 
스토어 안에는 현재 상태들, 리듀서, 그리고 몇 가지의 내장 함수를 포함하고 있다.

### Dispatch
디스패치는 스토어의 내장함수 중 하나로, 액션을 발생시키는 역할을 한다.
이 카테고리의 해더에 있는 '스토어는 상태 변화의 필요를 어떻게 캐치해?'.
바로 디스패치가 액션을 발생시켜 스토어에게 상태 변화가 필요하다는 것을 알린다.


## 유의사항
- 단일 스토어 사용을 권장한다.
- 상태는 읽기 전용이여야 한다.
    - 배열 형태의 상태가 있는데, 로직에 의해 배열에 새로운 값을 넣어주어야 한다면, 
    - 기존 상태에 새로운 값을 직접 push하는 것이 아니라, 
    - concat과 같은 함수를 통해 새로운 값을 이어붙여 생성한 새로운 배열로 교체하여 업데이트해야 한다
    - 이러한 업데이트 방식을 사용하면 불변성이 유지된다.
- 리듀서는 순수한 함수이여야 한다.
    - 동일한 입력을 받았을 때 언제나 동일한 출력을 내는 함수


```shell
npx create-react-app redux-counter
cd redux-counter
npm install redux react-redux
```
