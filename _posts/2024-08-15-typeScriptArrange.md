---
layout: post
title: "헷갈리는 타입스크립트들 정리1"
summary: "인터페이스 부터 컨디셔널타입까지"
author: yoo94
date: "2024-08-15 09:32:23 +0530"
category: ["myconfused", "javaScript", "typeScript"]
tags:
  - javaScript
  - typeScript
thumbnail:
permalink: blog/typeScriptArrange/
---

### 타입스크립트 공부를 하다보니.. 어떤게 어떻게 써야하는지 제대로 정리가 안돼서 여기다가 한번 정리하고자 한다.

### 1. 인터페이스 (Interface)

인터페이스는 객체의 구조를 정의할 때 사용 객체가 가져야 할 속성과 메서드의 타입을 지정할 수 있다.

#### 언제 사용하는가?

인터페이스는 특정 객체가 가져야 할 구조를 미리 정의하고, 그 구조를 따르는 객체만 사용하고 싶을 때 사용합니다.

####주의할 점:

인터페이스는 구조적으로 유사한 객체를 관리하기에 좋지만, 너무 복잡한 구조를 정의하면 유지보수가 어려울 수 있습니다.

```typescript
interface Person {
  name: string;
  age: number;
  greet(): void;
}

const person: Person = {
  name: "John",
  age: 30,
  greet() {
    console.log(`Hello, my name is ${this.name}`);
  },
};
```

---

### 2. 타입 별칭 (Type Alias)

타입 별칭은 특정 타입에 이름을 붙여 재사용할 수 있게 한다.

#### 언제 사용하는가?

유니언 타입, 튜플 등 복잡한 타입에 이름을 붙여 가독성을 높이고 싶을 때 사용

####주의할 점:

타입 별칭은 인터페이스와 달리 병합되지 않기 때문에, 확장이 필요한 경우 인터페이스가 더 적합

```typescript
type ID = string | number;

let userId: ID;
userId = 123;
userId = "abc";
```

---

### 3. 리터럴 타입 (Literal Type)

리터럴 타입은 특정 값 자체를 타입으로 사용할 수 있게 한다.

#### 언제 사용하는가?

정해진 값들만 허용해야 하는 경우(예: 방향, 상태 등)에 사용.

####주의할 점:

리터럴 타입을 너무 많이 사용하면 코드의 유연성이 떨어질 수 있다.

```typescript
type Direction = "up" | "down" | "left" | "right";

function move(direction: Direction) {
  console.log(`Moving ${direction}`);
}

move("up"); // OK
move("sideways"); // Error
```

---

### 4. 튜플 (Tuple)

튜플은 고정된 수의 요소를 가지며, 각 요소가 특정 타입을 가지는 배열

#### 언제 사용하는가?

서로 다른 타입의 값들을 함께 다뤄야 할 때 사용.

####주의할 점:

튜플의 길이가 길어지면 관리가 어려워질 수 있다

```typescript
let person: [string, number];
person = ["John", 30]; // OK
person = [30, "John"]; // Error
```

---

### 5. 네임스페이스 (Namespace)

네임스페이스는 코드를 모듈화하여 동일한 이름을 가진 변수를 충돌 없이 사용할 수 있게 한다.

#### 언제 사용하는가?

대규모 애플리케이션에서 이름 충돌을 피하면서 모듈화를 할 때 사용

####주의할 점:

네임스페이스는 모듈 시스템과 함께 사용할 때 혼란을 줄 수 있으므로, 모듈 시스템을 사용하는 경우에는 네임스페이스를 피하는 것이 좋다.

```typescript
namespace Animals {
  export class Dog {
    bark() {
      console.log("Woof!");
    }
  }
}

namespace Vehicles {
  export class Dog {
    honk() {
      console.log("Beep!");
    }
  }
}

let pet = new Animals.Dog();
pet.bark();

let car = new Vehicles.Dog();
car.honk();
```

---

### 6. 인덱스 접근 타입 (Indexed Access Type)

인덱스 접근 타입은 객체 타입의 특정 속성 타입을 가져올 수 있게한다.

#### 언제 사용하는가?

객체 타입에서 특정 속성의 타입을 재사용하고 싶을 때 유용

####주의할 점:

잘못된 속성명을 사용하면 컴파일 오류가 발생하므로 주의

```typescript
interface Person {
  name: string;
  age: number;
}

type NameType = Person["name"]; // string 타입
```

---

### 7. 매핑된 객체 타입 (Mapped Type)

매핑된 타입은 기존 타입을 변형하여 새로운 타입을 생성할 때 사용.

#### 언제 사용하는가?

기존 타입의 모든 속성을 변형하여 새로운 타입을 만들어야 할 때 사용

####주의할 점:

매핑된 타입은 복잡할 수 있으므로, 필요 이상으로 사용하면 코드가 이해하기 어려워짐

```typescript
type ReadOnly<T> = {
  readonly [P in keyof T]: T[P];
};

interface Person {
  name: string;
  age: number;
}

const readonlyPerson: ReadOnly<Person> = {
  name: "John",
  age: 30,
};

readonlyPerson.name = "Doe"; // Error
```

---

### 8. 유니언과 인터섹션 (Union & Intersection)

- 유니언 타입은 여러 타입 중 하나의 타입을 허용.
- 인터섹션 타입은 여러 타입을 모두 만족.

#### 언제 사용하는가?

유니언 타입은 다형성을 제공하며, 인터섹션 타입은 여러 타입의 결합된 기능이 필요할 때 사용

####주의할 점:

인터섹션 타입을 사용할 때 속성이 충돌하지 않도록 주의

```typescript
type A = { name: string };
type B = { age: number };

type AB = A & B; // { name: string; age: number }
type AorB = A | B;

let person1: AB = { name: "John", age: 30 }; // OK
let person2: AorB = { name: "Doe" }; // OK
```

---

### 9. 제네릭 (Generic)

제네릭은 타입을 변수처럼 다뤄서 다양한 타입에 대해 재사용 가능한 코드를 작성할 수 있게 해줌

#### 언제 사용하는가?

여러 타입에 대해 동일한 로직을 적용할 때 사용

####주의할 점:

제네릭을 남용하면 코드가 복잡해질 수 있습니다. 필요할 때만 사용

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let output = identity<string>("Hello");
```

---

### 10. 컨디셔널 타입 (Conditional Type)

컨디셔널 타입은 조건에 따라 타입을 선택할 수 있게 해줌

#### 언제 사용하는가?

조건에 따라 타입을 다르게 적용해야 할 때 유용합니다.

####주의할 점:

컨디셔널 타입은 복잡한 논리를 담을 수 있으므로, 지나치게 복잡하게 만들지 않도록 주의

```typescript
type IsString<T> = T extends string ? true : false;

type A = IsString<string>; // true
type B = IsString<number>; // false
```
