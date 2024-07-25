---
layout: post
title:  "sass scss  무엇인가?"
summary: "sass-scss"
author: yoo94
date: '2024-02-21 13:35:23 +0530'
category: ['myconfused','javaScript','css']
tags: sass-scss
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Sass_Logo_Color.svg/220px-Sass_Logo_Color.svg.png
permalink: blog/sass-scss/
---
먼저 둘다 나중에는 컴파일러를 통해 css로 변환된다

차이점 요약
```markdown

| 항목       | CSS                                | SASS                                | SCSS                                |
|------------|------------------------------------|-------------------------------------|-------------------------------------|
| 문법       | 표준 CSS 문법                       | 인덴트 기반 문법                     | CSS와 유사한 문법                    |
| 중괄호     | 사용 (예: `{}`)                     | 사용하지 않음                        | 사용 (예: `{}`)                       |
| 세미콜론   | 사용 (예: `;`)                      | 사용하지 않음                        | 사용 (예: `;`)                        |
| 변수       | 지원하지 않음                       | 지원 (예: `$variable`)               | 지원 (예: `$variable`)               |
| 중첩       | 지원하지 않음                       | 지원                                | 지원                                |
| 믹스인     | 지원하지 않음                       | 지원 (예: `@mixin` 및 `@include`)   | 지원 (예: `@mixin` 및 `@include`)   |
| 상속       | 지원하지 않음                       | 지원 (예: `@extend`)                | 지원 (예: `@extend`)                |
| 사용 용이성 | 기본적인 스타일 정의에 적합          | 더 간결한 문법, 높은 러닝 커브       | 기존 CSS와 유사하여 적응이 용이       |

```

### SASS (Syntactically Awesome Style Sheets)
개념: SASS는 CSS의 전처리기로, 변수를 사용하거나 중첩, 믹스인, 상속 등의 기능을 제공하여 CSS 작성 방식을 더 효율적이고 유지 보수 가능하게 한다.
SASS는 두 가지 문법을 제공하는데, 그 중 하나가 인덴트 문법을 사용하는 SASS이다.
```sass
.container
  width: 100%
  padding: 20px
  background-color: lightblue

  h1
    color: darkblue
    text-align: center
```
사용법: .sass 파일 확장자를 사용하고, 인덴트로 구조를 정의합니다.

### SCSS (Sassy CSS)
개념: SCSS는 SASS의 또 다른 문법으로, 기존 CSS 문법과 호환성을 유지하면서 SASS의 모든 기능을 제공한다.
사용법: .scss 파일 확장자를 사용하며, CSS와 동일한 중괄호 및 세미콜론 문법을 사용.
```scss
$bg-color: lightblue;
$text-color: darkblue;

.container {
  width: 100%;
  padding: 20px;
  background-color: $bg-color;

  h1 {
    color: $text-color;
    text-align: center;
  }
}
```
