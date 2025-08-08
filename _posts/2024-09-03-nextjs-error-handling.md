---
layout: post
title: "next error 핸들링"
summary: "에러 실헝.."
author: yoo94
date: "2024-09-02 13:35:23 +0530"
category: Frontend2
tags: react,nextJs
thumbnail:
permalink: blog/next-error/
---

## try & catch 말고!

page.tsx에 error.tsx를 만들어서 에러페이지를 만들면 됨!

```tsx
"use client";
import { useEffect } from "react";
export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error.message);
  }, [error]);
  return (
    <div>
      에러발생!!
      <button onClick={() => reset()}>다시 시도</button>
    </div>
  );
}
```

여기서 reset함수도 넘어오게 되는데 이 reset은 다시한번 시도 할수 있게 해주는 함수이다.
서버측에 대한것을 시도하는 것은 아니고 클라이언트에서 발생한 오류만 처리한다.
그래서 그냥 window.loaction.reload()를 쓰는게 나을수도 있다.

```tsx
"use client";
import { useEffect } from "react";
export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  const router = useRouter();
  useEffect(() => {
    console.error(error.message);
  }, [error]);
  return (
    <div>
      에러발생!!
      <button
        onClick={() => {
          startTransition(() => {
            router.refresh();
            reset();
          });
        }}
      >
        다시 시도
      </button>
    </div>
  );
}
```

router.refresh(); - 현재 페이지에 필요한 서버컴포넌트를 다시 불러옴
reset(); - 에러 상태를 초기화, 컴포넌트들을 다시 렌더링

이 두개를 같이쓰면 좋다.

#### startTransition

이건 리액트 18부터 추가된 기능으로
router.refresh(); <- 이게 비동기처리가 된다. 그래서 순서대로 실행하게 해야하는데
reset();

async await는 refresh에서 사용할 수 없다. 프라미스를 반환하지 않기 때문이다. 그래서 사용하게 된것이
startTransition이다. 이걸 쓰면 순서대로 일괄적으로 처리 된다.
