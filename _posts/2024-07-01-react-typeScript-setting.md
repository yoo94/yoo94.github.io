---
layout: post
title:  "CRA 없이 react+types"
summary: "react + typeScript 프로젝트 만들기"
author: yoo94
date: '2024-07-01 14:35:23 +0530'
category: DevLog
tags: react
thumbnail: 
permalink: blog/react-typeScript-setting/
---

## cra 없이 react 와 타입스크립트 설정

```shell
mkdir my-react-app
cd my-react-app
npm init -y
```

### React, ReactDOM, TypeScript, Webpack, Babel,eslint 및 관련 도구

```shell
npm install react react-dom
npm install --save-dev typescript @types/react @types/react-dom
npm install --save-dev webpack webpack-cli webpack-dev-server
npm install --save-dev babel-loader @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript
npm install --save-dev html-webpack-plugin
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint-plugin-react
```

### tsconfig.json생성

```shell
npx tsc --init
```
```text
{
  "compilerOptions": {
    "target": "ESNext", // 최신 ECMAScript 표준으로 컴파일, 최신 JavaScript 기능을 지원
    "lib": ["dom", "dom.iterable", "esnext"], // 사용할 라이브러리의 타입 정의, DOM API와 최신 ECMAScript 기능을 포함
    "allowJs": true, // JavaScript 파일을 TypeScript 프로젝트에 포함하여 컴파일 가능
    "skipLibCheck": true, // 라이브러리 파일(.d.ts)의 타입 검사를 건너뜀, 빌드 시간을 줄이기 위해 사용
    "esModuleInterop": true, // CommonJS 모듈(require)을 ES 모듈(import/export)과 호환 가능하게 설정
    "allowSyntheticDefaultImports": true, // ES6 스타일의 기본(default) import를 허용
    "strict": true, // 모든 엄격한 타입 검사 옵션을 활성화 (strictNullChecks, strictFunctionTypes 등)
    "forceConsistentCasingInFileNames": true, // 파일 및 모듈 이름의 대소문자 일관성을 강제
    "noFallthroughCasesInSwitch": true, // switch 문에서 case가 누락되는 것을 방지
    "module": "esnext", // ES 모듈 시스템 사용 (import/export 문법)
    "moduleResolution": "node", // Node.js 방식의 모듈 해석, node_modules에서 모듈을 찾음
    "resolveJsonModule": true, // JSON 파일을 모듈로 가져올 수 있도록 설정
    "isolatedModules": true, // 개별 TypeScript 파일을 독립적으로 컴파일하도록 강제
    "noEmit": true, // 실제 JavaScript 파일을 생성하지 않고, 타입 검사만 수행
    "jsx": "react-jsx" // React 17+의 새로운 JSX 변환을 사용, React를 명시적으로 import하지 않아도 됨
  },
  "include": ["src"] // src 디렉토리 내의 파일들을 컴파일 대상으로 포함
}
```
### .babelrc

```text
{
  "presets": [
    "@babel/preset-env", // 최신 JavaScript 문법을 구형 브라우저에서도 동작하도록 변환
    "@babel/preset-react", // JSX 문법과 React 관련 최신 기능을 지원
    "@babel/preset-typescript" // TypeScript 코드를 JavaScript로 변환 (타입 정보를 제거)
  ]
}
```
### webpack.config.js

```text
const path = require('path'); // Node.js의 path 모듈을 가져와서 파일 및 디렉토리 경로 작업을 쉽게 함
const HtmlWebpackPlugin = require('html-webpack-plugin'); // HTML 파일을 생성하고, 번들링된 JS 파일을 자동으로 포함시켜줌

module.exports = {
    entry: './src/index.tsx', // 애플리케이션의 진입점 파일, Webpack이 이 파일부터 시작해 의존성을 분석하여 번들링
    output: {
        filename: 'bundle.js', // 번들링된 결과 파일의 이름
        path: path.resolve(__dirname, 'dist'), // 번들 파일이 생성될 경로, 절대 경로로 변환
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js'], // 확장자 없이 import 할 수 있도록 처리 (순서대로 시도)
    },
    module: {
        rules: [
            {
                test: /\.(ts|tsx)$/, // .ts 또는 .tsx 파일에 대해 이 규칙을 적용
                use: 'babel-loader', // Babel을 사용하여 TypeScript 코드를 JavaScript로 변환
                exclude: /node_modules/, // node_modules 폴더는 변환 대상에서 제외
            },
            {
                test: /\.css$/, // .css 파일에 대해 이 규칙을 적용
                use: ['style-loader', 'css-loader'], // CSS 파일을 처리하여, 스타일을 DOM에 삽입
            },
        ],
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './index.html', // 이 HTML 파일을 템플릿으로 사용하여 최종 HTML 파일을 생성, 번들링된 JS 파일을 자동으로 삽입
        }),
    ],
    devServer: {
        contentBase: path.join(__dirname, 'dist'), // 개발 서버가 제공할 정적 파일의 경로
        compress: true, // 파일을 gzip으로 압축하여 제공
        port: 3000, // 개발 서버가 실행될 포트
    },
    mode: 'development', // Webpack의 모드를 개발(development)로 설정, 소스 맵과 같은 개발에 유용한 도구들이 활성화됨
};

```

### .eslintrc.js
```text
module.exports = {
    parser: '@typescript-eslint/parser', // TypeScript 코드를 파싱하는 데 사용하는 파서
    extends: [
        'eslint:recommended', // 기본적인 ESLint 권장 규칙을 적용
        'plugin:react/recommended', // React와 JSX에 관련된 권장 규칙을 적용
        'plugin:@typescript-eslint/recommended', // TypeScript에 관련된 권장 규칙을 적용
    ],
    parserOptions: {
        ecmaVersion: 2020, // 최신 ECMAScript 기능(ES11)을 사용할 수 있도록 설정
        sourceType: 'module', // ECMAScript 모듈 시스템을 사용 (import/export 문법)
        ecmaFeatures: {
            jsx: true, // JSX 문법을 지원하도록 설정 (React에서 JSX를 사용하기 위함)
        },
    },
    settings: {
        react: {
            version: 'detect', // 설치된 React 버전을 자동으로 감지하여 해당 버전에 맞는 규칙을 적용
        },
    },
    rules: {
        // 추가적인 규칙을 여기에 정의할 수 있음

        // Best practices
        'eqeqeq': ['error', 'always'], // 항상 === 또는 !== 사용하도록 강제 (느슨한 비교를 피함)
        'curly': ['error', 'all'], // 모든 제어 구조에 중괄호 사용을 강제 (가독성 및 안전성을 높임)

        // TypeScript specific rules
        '@typescript-eslint/explicit-function-return-type': 'off', // 함수 반환 타입을 명시적으로 작성하도록 요구 (비활성화할 경우 암시적 반환 타입 허용)
        '@typescript-eslint/no-explicit-any': 'warn', // any 타입 사용을 경고 (가능한 경우 구체적인 타입을 사용하도록 유도)
        '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_' }], // 사용되지 않는 변수에 대해 경고, _로 시작하는 매개변수는 예외로 처리

        // React specific rules
        'react/jsx-uses-react': 'off', // React 17+에서는 필요하지 않음, JSX 사용시 React를 자동으로 import하지 않아도 되도록 설정
        'react/react-in-jsx-scope': 'off', // React 17+에서는 필요하지 않음, JSX 사용시 React가 자동으로 전역에서 접근 가능하도록 설정

        // Code style
        'semi': ['error', 'always'], // 세미콜론을 항상 사용하도록 강제 (코드 일관성 유지)
        'quotes': ['error', 'single'], // 문자열에 항상 single quotes 사용을 강제 (코드 일관성 유지)
        'indent': ['error', 2], // 두 칸 들여쓰기를 강제 (코드 가독성 향상)
        'comma-dangle': ['error', 'always-multiline'], // 여러 줄의 객체나 배열에서 마지막 요소 뒤에 콤마를 허용 (git diff에서 변경 내역이 명확히 보이게 함)
        'no-trailing-spaces': 'error', // 라인의 끝에 불필요한 공백이 있으면 에러 발생 (코드 청결성 유지)

        // Accessibility (for React)
        'jsx-a11y/accessible-emoji': 'warn', // 이모지에 적절한 접근성을 적용하도록 경고
        'jsx-a11y/alt-text': 'warn', // 모든 이미지에 alt 속성을 강제 (스크린 리더 사용자들을 위한 접근성 보장)
        'jsx-a11y/anchor-has-content': 'warn', // 앵커 태그에 반드시 내용이 포함되도록 경고 (빈 링크 방지)
    },
};
```
## 프로젝트 구조
```arduino
my-react-app/
│
├── index.html
│
├── src/
│   ├── index.tsx
│   └── App.tsx
│
├── .babelrc
├── .eslintrc.js
├── tsconfig.json
├── webpack.config.js
└── package.json

```

#### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>React App</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```

#### src/index.tsx

React 18에서는 새로운 ReactDOM.createRoot API를 사용하여 렌더링을 처리

```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// 기존 ReactDOM.render 대신 ReactDOM.createRoot 사용
const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);

root.render(
        <React.StrictMode>
         <App />
        </React.StrictMode>
);

```
#### src/App.tsx

```tsx
import React from 'react';

const App: React.FC = () => {
 return (
         <div>
          <h1>Hello, TypeScript and React!</h1>
         </div>
 );
};

export default App;
```

### package.json 스크립트 추가

```text
{
  "scripts": {
    "start": "webpack serve --open", // 개발 서버를 시작하는 명령어, 웹 브라우저가 자동으로 열림
    "build": "webpack --mode production" // 프로젝트를 프로덕션 모드로 빌드하는 명령어, 최적화된 번들 생성
  }
}
```

#### 시작
```shell
npm start
```



