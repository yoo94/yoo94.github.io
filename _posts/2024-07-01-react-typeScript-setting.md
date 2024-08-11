---
layout: post
title:  "CRA 없이 react+types"
summary: "react + typeScript 프로젝트 만들기"
author: yoo94
date: '2024-07-01 14:35:23 +0530'
category: ['react','typeScript']
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
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}

```
### .babelrc

```json
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react",
    "@babel/preset-typescript"
  ]
}

```
### webpack.config.js

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.tsx',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        use: 'babel-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './index.html',
    }),
  ],
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 3000,
  },
  mode: 'development',
};
```

### .eslintrc.js
```javascript
module.exports = {
  parser: '@typescript-eslint/parser',
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:@typescript-eslint/recommended',
  ],
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
  rules: {
    // 프로젝트에 맞게 추가 규칙 설정 가능
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

```json
{
  "scripts": {
    "start": "webpack serve --open",
    "build": "webpack --mode production"
  }
}
```

#### 시작
```shell
npm start
```



