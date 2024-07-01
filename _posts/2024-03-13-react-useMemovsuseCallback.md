---
layout: post
title:  "react useMemo vs useCallback"
summary: "useMemo와 useCallback"
author: yoo94
date: '2024-03-13 04:35:23 +0530'
category: react
tags: react
thumbnail: /assets/postImg/Pasted image 20240114133527.png
permalink: /blog/useMemo-useCallback/
---
#### ❌ useMemo와 useCallback을 사용하지 말아야 할 경우

- 연산이 복잡하지 않은 함수에 useCallback을 사용하는 것은 메모리 낭비이므로, 간단한 일반 함수들에는 useCallback을 사용하지 않는게 좋다.

- 특히, 단순히 함수 내부에서 setState나 dispatch 함수등을 호출하는 경우에는 useCallback을 사용하지 않는게 좋다. 이미 리액트 자체에서 useState 와 useDispatch에 대한 성능 최적화가 보장되기 때문에, 렌더링이 새로 되어도 해당 함수는 재생성되지 않는다.
- 의도적으로 매번 새로운 함수나 값을 계산해야 한다면 굳이 useCallback이나 useMemo를 사용할 필요가 없다.

- DOM에서 다른 컴포넌트를 렌더링하지 않는 컴포넌트 (html 태그만 렌더링하는 컴포넌트)에서는 useMemo를 사용할 필요가 없다.

- div, span, a, img와 같이 호스트 환경 (브라우저 / 모바일)에 속하는 플랫폰 컴포넌트에 전달하는 항목에는 useMemo와 useCallback을 사용할 필요가 없다. 리액트는 해당 컴포넌트들에 함수 참조가 변경되었는지 신경 쓰지 않기 때문이다. (ref는 제외)

#### 🟢 useMemo와 useCallback을 사용해야 하는 경우

- 연산 혹은 처리량이 매우 많아서 렌더링의 문제가 되는 경우, 리렌더시 비용 절감을 위해서 useMemo를 사용하자

- 자식 컴포넌트에서 useEffect가 반복적으로 트리거 되거나, 무한 루프에 빠질 위험이 있을 때 useMemo, useCallback을 사용하자

- 자식 컴포넌트에 함수를 props로 넘길 때, 불필요한 렌더링이 일어난다고 판단된다면 useCallback으로 함수 동등성을 유지해주자.

- 함수 자체가 매우 복잡하거나, 다시 계산하는데 비용이 많이 드는 경우에 useCallback을 사용하자.

- 사용자의 입력값이 `map` 혹은 `filter` 등을 사용하여 이후 렌더링에서도 동일한 참조를 사용할 가능성이 높을 경우 useMemo를 사용해서 메모이제이션을 적용하자

- 리액트 상위 트리에서, 부모가 리렌더링 될 때 자식 컴포넌트까지의 렌더링 전파를 막고 싶을 때 useMemo를 사용하자. 자식 컴포넌트가 useMemo로 메모이제이션 컴포넌트일 경우, 메모이제이션된 props를 사용해 필요한 부분만 리렌더링 할 수 있다.

- ref 함수를 부수작용(side effect)와 함께 전달하거나, ref로 wrapper 함수를 만들 때 useMemo를 사용하자. 리액트는 ref 함수가 변경될 때 마다 과거 값을 null로 호출하고 새로운 함수를 호출하기 때문인데, 이 경우 ref 함수의 이벤트 리스터가 변경되는 등의 불필요한 작업이 일어날 수 있다.
