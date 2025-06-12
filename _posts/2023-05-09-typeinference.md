---
layout: post
title:  "타입 추론 호환 단언"
summary: "타입 추론이란 타입스크립트가 코드를 해석해 나가는 동작"
author: yoo94
date: '2023-05-09 14:35:23 +0530'
category: typeScript
tags: typeScript
keywords: typeScript
thumbnail: https://i.namu.wiki/i/EY559r31H-um8uTtptPIbCZoBGxsumSlwEH0T_rA6WmxQq1UwqyAf3cJQJXN7Fv5CoEz0kv5CBXzjkkPU_XWig.svg
permalink: blog/typeinference/
---

#### 타입의 추론!
타입 추론이란 타입스크립트가 코드를 해석해 나가는 동작을 의미합니다.

타입스크립트가 타입 추론을 해나가는 과정은 다음과 같습니다.

```typescript
let x = 3;
```

위와 같이 `x`에 대한 타입을 따로 지정하지 않더라도 일단 `x`는 `number`로 간주됩니다. 이렇게 변수를 선언하거나 초기화 할 때 타입이 추론됩니다. 이외에도 변수, 속성, 인자의 기본 값, 함수의 반환 값 등을 설정할 때 타입 추론이 일어납니다.

#### 가장 적절한 타입(Best Common Type)
타입은 보통 몇 개의 표현식(코드)을 바탕으로 타입을 추론합니다. 그리고 그 표현식을 이용하여 가장 근접한 타입을 추론하게 되는데 이 가장 근접한 타입을 Best Common Type이라고 합니다.

잠깐 예제를 보겠습니다.

```typescript
let arr = [0, 1, null];
```

위 변수 `arr`의 타입을 추론하기 위해서는 배열의 각 아이템을 살펴봐야 합니다. 배열의 각 아이템의 타입은 크게 `number`와 `null`로 구분됩니다. 이 때 Best Common Type 알고리즘으로 다른 타입들과 가장 잘 호환되는 타입을 선정합니다.

#### 문맥상의 타이핑(Contextual Typing)

타입스크립트에서 타입을 추론하는 또 하나의 방식은 바로 문맥상으로 타입을 결정하는 것입니다. 이 문맥상의 타이핑(타입 결정)은 코드의 위치(문맥)를 기준으로 일어납니다.

##### 예시 코드 1

예시 코드를 보겠습니다.

```typescript
window.onmousedown = function(mouseEvent) {
  console.log(mouseEvent.button);   //<- OK
  console.log(mouseEvent.kangaroo); //<- Error!
};
```

위 코드를 타입스크립트 검사기 관점에서 보면 `window.onmousedown`에 할당되는 함수의 타입을 추론하기 위해 `window.onmousedown` 타입을 검사합니다. 타입 검사가 끝나고 나면 함수의 타입이 마우스 이벤트와 연관이 있다고 추론하기 때문에 `mouseEvent` 인자에 `button` 속성은 있지만 `kangaroo` 속성은 없다고 결론을 내립니다.

##### 예시 코드 2

다른 예제를 보겠습니다.

```typescript
window.onscroll = function(uiEvent) {
  console.log(uiEvent.button); //<- Error!
}
```

앞의 예제와 마찬가지로 오른쪽의 함수는 `window.onscroll`에 할당되었기 때문에 함수의 인자 `uiEvent`는 UIEvent으로 간주됩니다. 그래서 앞에서 봤던 MouseEvent와는 다르게 `button` 속성이 없다고 추론합니다. 그러므로 `uiEvent.button`에서 에러가 나죠.

여기서 만약 문맥상 타이핑을 좀 더 이해하고자 한다면 아래와 같이 코드를 바꿔볼 수도 있습니다.

```typescript
const handler = function(uiEvent) {
  console.log(uiEvent.button); //<- OK
}
```

오른쪽 함수 표현식이 앞의 예제와 동일하지만 함수가 할당되는 변수만으로는 타입을 추정하기 어렵기 때문에 아무 에러가 나지 않습니다.

WARNING

위 코드에서 `--noImplicitAny` 옵션을 사용하면 에러납니다 😄

#### 타입스크립트의 타입 체킹

타입 체킹에 있어서 타입스크립트의 지향점은 타입 체크는 값의 형태에 기반하여 이루어져야 한다는 점입니다. 이걸 Duck Typing 또는 Structural Subtyping 이라고 합니다.

TIP

Duck Typing : 객체의 변수 및 메서드의 집합이 객체의 타입을 결정하는 것을 의미. 동적 타이핑의 한 종류 Structural Subtyping : 객체의 실제 구조나 정의에 따라 타입을 결정하는 것을 의미

---

#### 타입의 호환!
타입 호환이란 타입스크립트 코드에서 특정 타입이 다른 타입에 잘 맞는지를 의미합니다. 예를 들면 아래와 같은 코드를 의미합니다.
```typescript
interface Ironman {
  name: string;
}

class Avengers {
  name: string;
}

let i: Ironman;
i = new Avengers(); // OK, because of structural typing
```

C#이나 Java였다면 위 코드에서 에러가 날겁니다. 왜냐하면 `Avengers` 클래스가 명시적으로 `Ironman` 인터페이스를 상속받아 구현하지 않았기 때문입니다.

하지만 위와 같은 코드가 타입스크립트에서 정상적으로 동작하는 이유는 자바스크립트의 작동 방식과 관련이 있습니다. 기본적으로 자바스크립트는 객체 리터럴이나 익명 함수 등을 사용하기 때문에 명시적으로 타입을 지정하는 것보다는 코드의 구조 관점에서 타입을 지정하는 것이 더 잘 어울립니다.\

#### 구조적 타이핑 예시

구조적 타이핑(structural typing)이란 코드 구조 관점에서 타입이 서로 호환되는지의 여부를 판단하는 것입니다. 아래 코드를 보겠습니다.

```typescript
interface Avengers {
  name: string;
}

let hero: Avengers;
// 타입스크립트가 추론한 y의 타입은 { name: string; location: string; } 입니다.
let capt = { name: "Captain", location: "Pangyo" };
hero = capt;
```

위 코드에서 `capt`가 `hero` 타입에 호환될 수 있는 이유는 `capt`의 속성 중에 `name`이 있기 때문입니다. `Avengers` 인터페이스에서 `name` 속성을 갖고 있기 때문에 `capt`는 `Avengers` 타입에 호환될 수 있죠.

함수를 호출할 때도 마찬가지입니다.

```typescript
function assemble(a: Avengers) {
  console.log("어벤져스 모여라", a.name);
}
// 위에서 정의한 capt 변수. 타입은 { name: string; location: string; }
assemble(capt);
```

`capt` 변수에 이미 `name` 속성 뿐만 아니라 `location` 속성도 있기 때문에 `assemble` 함수의 호출 인자로 넘길 수 있습니다.

#### Soundness란?

타입스크립트는 컴파일 시점에 타입을 추론할 수 없는 특정 타입에 대해서 일단 안전하다고 보는 특성이 있습니다. 이걸 "들리지 않는다(it is said to not be sound)"라고 표현합니다.

#### Enum 타입 호환 주의 사항

이넘 타입은 `number` 타입과 호환되지만이넘 타입끼리는 호환되지 않습니다.

```typescript
enum Status { Ready, Waiting };
enum Color { Red, Blue, Green };

let status = Status.Ready;
status = Color.Green;  // Error
```

#### Class 타입 호환 주의 사항

클래스 타입은 클래스 타입끼리 비교할 때 스태틱 멤버(static member)와 생성자(constructor)를 제외하고 속성만 비교합니다.

```typescript
class Hulk {
  handSize: number;
  constructor(name: string, numHand: number) { }
}

class Captain {
  handSize: number;
  constructor(numHand: number) { }
}

let a: Hulk;
let s: Captain;

a = s;  // OK
s = a;  // OK
```

#### Generics

제네릭은 제네릭 타입 간의 호환 여부를 판단할 때 타입 인자 `<T>`가 속성에 할당 되었는지를 기준으로 합니다. 예시 코드를 보겠습니다.

```typescript
interface Empty<T> {
}
let x: Empty<number>;
let y: Empty<string>;

x = y;  // OK, because y matches structure of x
```

위 인터페이스는 일단 속성(member 변수)이 없기 때문에 `x`와 `y`는 같은 타입으로 간주됩니다. 그런데 만약 아래와 같이 인터페이스에 속성이 있어서 제네릭의 타입 인자가 속성에 할당된다면 얘기는 다릅니다.

```typescript
interface NotEmpty<T> {
  data: T;
}
let x: NotEmpty<number>;
let y: NotEmpty<string>;

x = y;  // Error, because x and y are not compatible
```

인터페이스 `NotEmpty`에 넘긴 제네릭 타입`<T>`이 `data` 속성에 할당되었으므로 `x`와 `y`는 서로 다른 타입으로 간주됩니다.

---

#### 타입 단언
타입 단언은 개발자가 해당 타입에 대해 확신이 있을 때 사용하는 타입 지정 방식입니다. 다른 언어의 타입 캐스팅과 비슷한 개념이며 타입스크립트를 컴파일 할 때 특별히 타입을 체크하지 않고, 데이터의 구조도 신경쓰지 않습니다.

#### 타입 단언 기본 - as

타입 단언은 기본적으로 `as` 키워드를 이용해서 정의할 수 있습니다. 아래와 같은 코드가 있다고 합시다.

```typescript
const name: string = 'Capt';
```

이 코드는 타입 표기 방식을 이용해 `name` 이라는 변수의 타입은 `string` 이라고 정의한 코드입니다. 이 코드에 타입 단언을 적용하면 다음과 같습니다.

```typescript
const name = 'Capt' as string;
```

비주얼 스튜디오 코드에서 `name` 변수의 정보를 확인해 보면 동일하게 `string`으로 추론되는 것을 확인할 수 있습니다.

#### 타입 단언은 언제 쓰는가?

타입 단언은 타입스크립트 컴파일러보다 개발자가 더 해당 타입을 잘 알고 있을 때 사용해야 합니다. 혹은, 자바스크립트 기반 코드에 점진적으로 타입스크립트를 적용할 때도 자주 사용됩니다. 예를 들어, 다음과 같은 자바스크립트 코드가 있다고 합시다.

```typescript
// app.js
const capt = {};
capt.name = '캡틴';
capt.age = 100;
```

이 객체에 타입 표기 방식으로 타입을 정의하려고 하면 에러가 발생합니다.

```typescript
interface Hero {
  name: string;
  age: number;
}

const capt: Hero = {}; // X. 오류 발생
capt.name = '캡틴';
capt.age = 100;
```

왜냐하면 `capt` 변수가 정의되는 시점에서 `name`, `age` 등의 속성이 정의되지 않았기 때문입니다. 기존에 운영하던 서비스의 코드가 위와 같다면 아래와 같이 코드를 변경하여 타입 오류를 해결할 수도 있습니다.

```typescript
interface Hero {
  name: string;
  age: number;
}

const capt: Hero = {
  name: '캡틴',
  age: 100
};
```

하지만, 기존 코드의 변경 없이 `as` 키워드로 타입 문제를 해결할 수 있습니다.


```typescript
interface Hero {
  name: string;
  age: number;
}

const capt = {} as Hero; // 오류 없음
capt.name = '캡틴';
capt.age = 100;
```



