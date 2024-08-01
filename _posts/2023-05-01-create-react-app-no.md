---
layout: post
title:  "cra없이 react 프로젝트 만들기"
summary: "cra없이 react 프로젝트 만들기"
author: yoo94
date: '2023-05-01 14:35:23 +0530'
category: ['react','myconfused']
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/create-react-app-nocra/
---
npm이 있다는 가정하에

1. 프로젝트 디렉토리를 만들고 npm을 init해준다.
```shell

mkdir my-react-app
cd my-react-app
npm init -y
```

2. react와 reactDom을 설치하고, babel 과 webpack을 설정한다.
```shell
pm install react react-dom
npm install --save-dev @babel/core @babel/preset-env @babel/preset-react babel-loader webpack webpack-cli webpack-dev-server html-webpack-plugin
```
3. Babel 설정
 babelrc 파일을 프로젝트 루트에 생성하고 아래와 같이 설정
```json
{
  "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```
4. Webpack 설정
webpack.config.js 파일을 프로젝트 루트에 생성하고 아래와 같이 설정
```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 3000
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html'
    })
  ]
};

```
5. HTML 템플릿 작성
public 폴더에 index.html 파일을 생성
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
6. React 애플리케이션 작성
src 폴더에 index.js 파일을 생성하고 React 애플리케이션을 작성
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // App 컴포넌트는 필요에 따라 생성

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```
