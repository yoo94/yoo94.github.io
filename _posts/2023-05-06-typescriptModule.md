---
layout: post
title:  "타입스크립트 모듈"
summary: "타입스크립트에서 가리키는 모듈이라는 개념은 ES6+의 Modules개념과 유사"
author: yoo94
date: '2023-05-06 14:35:23 +0530'
category: Frontend2
tags: typeScript
keywords: typeScript
thumbnail: https://i.namu.wiki/i/EY559r31H-um8uTtptPIbCZoBGxsumSlwEH0T_rA6WmxQq1UwqyAf3cJQJXN7Fv5CoEz0kv5CBXzjkkPU_XWig.svg
permalink: blog/typescriptModule/
---
타입스크립트에서 가리키는 모듈이라는 개념은 ES6+의 Modules개념과 유사합니다. 모듈은 전역 변수와 구분되는 자체 유효 범위를 가지며 `export`, `import`와 같은 키워드를 사용하지 않으면 다른 파일에서 접근할 수 없습니다.

#### Export

ES6의 `export`와 같은 방식으로 변수, 함수, 타입, 인터페이스 등에 붙여 사용합니다.

```typescript
// math.ts
export interface Triangle {
    width: number;
    height: number;
}

// index.ts
import {Triangle} from './math.ts';

class SomeTriangle implements Triangle {
    height: number;
    width: number;
    // ...
}
```

#### Import

ES6의 `import`와 동일한 방식으로 사용합니다.

```typescript
import { WheatBeerClass } from './index.ts';

class Cloud extends WheatBeerClass {
  
}
```

#### 타입스크립트는 모듈 코드를 어떻게 변환해주는가?

`tsconfig.json` 파일에 설정한 컴파일러 모드에 따라 모듈 코드가 각기 다르게 변환됩니다.

```typescript
// SimpleModule.ts
import m = require("mod");
export let t = m.something + 1
```

```typescript
// AMD / RequireJS SimpleModule.js 
define(["require", "exports", "./mod"], function (require, exports, mod_1) {
  exports.t = mod_1.something + 1;
});
```

```typescript
// CommonJS / Node SimpleModule.js
var mod_1 = require("./mod");
exports.t = mod_1.something + 1;
```

```typescript
// UMD SimpleModule.js
(function (factory) {
  if (typeof module === "object" && typeof module.exports === "object") {
    var v = factory(require, exports); if (v !== undefined) module.exports = v;
  }
  else if (typeof define === "function" && define.amd) {
    define(["require", "exports", "./mod"], factory);
  }
})(function (require, exports) {
  var mod_1 = require("./mod");
  exports.t = mod_1.something + 1;
});
```

```typescript
// System SimpleModule.js
System.register(["./mod"], function(exports_1) {
  var mod_1;
  var t;
  return {
    setters:[
      function (mod_1_1) {
        mod_1 = mod_1_1;
      }],
    execute: function() {
      exports_1("t", t = mod_1.something + 1);
    }
  }
});
```

타입스크립트 컴파일 명령어를 칠 때 컴파일러 모드를 부여할 수 있습니다.

```powershell
# commonjs 모드인 경우
tsc --module commonjs Test.ts

# amd 모드인 경우
tsc --module amd Test.ts
```

###### 선택적 모듈 로딩 방법과 고급 모듈 로딩 기법

