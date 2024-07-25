---
layout: post
title:  "Virtual Dom 이란 무엇인가?"
summary: "Virtual DOM이 나온 이유?"
author: yoo94
date: '2024-02-21 13:35:23 +0530'
category: ['myconfused','javaScript','react']
tags: react
thumbnail: https://blog.kakaocdn.net/dn/dpwvVE/btrBqolp4WG/xU2kPsR8hJ0Rpx9B1LSoZ1/img.png
permalink: blog/Virtual-Dom/
---
## Virtual DOM?

DOM이란 문서 객체 모델로, html/css <--> DOM <--> JavaScript 의 역할을 한다.

### Virtual DOM이 나온 이유

DOM에는 브라우저가 화면을 그리는데 필요한 모든 정보가 들어있어 실제 DOM을 조작하는 작업의 비용이 크기 때문이다
React에서는 실제 DOM의 변경 사항을 빠르게 파악하고 반영하기 위해서 내부적으로 가상 DOM을 만들어서 관리한다. 
쉽게 말해서, Virtual DOM은 DOM의 요약본이라고 볼 수 있다.

그렇다고 DOM이 무조건 느리다고는 할수 없다. React에서는 SPA방식을 사용하고 이기떄문이고, 정적인 웹 어플리케이션이라면
DOM을 그냥 변경하는것이 성능상 좋을 수 도있다. 하지만 최근 트렌드에서는 SPA가 트렌드이기 떄문에 DOM을 직접변경하는 것은 비효율 적이다.

### Virtual DOM의 과정
#### 1. 초기 렌더링

리액트 컴포넌트: 리액트 컴포넌트가 초기 상태에서 렌더링됩니다.
버추얼 돔 생성: 리액트는 컴포넌트의 렌더링 결과를 기반으로 버추얼 돔을 생성합니다.
실제 DOM 업데이트: 초기 버추얼 돔을 기반으로 실제 DOM이 생성되고 브라우저에 렌더링됩니다.
```text
React Component --Initial Render--> Virtual DOM --Initial Render--> Actual DOM
   <div>                              <div>                          <div>
     <h1>                               <h1>                           <h1>
       "Hello"                            "Hello"                        "Hello"
     </h1>                              </h1>                         </h1>
   </div>                             </div>                       </div>
```
#### 2. 상태 업데이트

상태 변화: 사용자 인터랙션이나 데이터 변경으로 인해 컴포넌트의 상태가 변경됩니다.
새로운 버추얼 돔 생성: 변경된 상태를 반영하여 새로운 버추얼 돔이 생성됩니다.
```text
User Action --State Change--> New Virtual DOM
   <div>                            <div>
     <h1>                             <h1>
       "World"                          "World"
     </h1>                            </h1>
   </div>                           </div>
```
#### 3. 디프(Diffing) 과정
버추얼 돔 비교: 기존 버추얼 돔과 새로운 버추얼 돔을 비교하여 변경된 부분을 찾습니다.
```text
Old Virtual DOM      New Virtual DOM
   <div>                <div>
     <h1>   --Diff-->    <h1>
       "Hello"            "World"
     </h1>               </h1>
   </div>              </div>
```
#### 4. 실제 DOM 업데이트
패치(Patching): 변경된 부분만 실제 DOM에 적용합니다. 
```text 
Changed Node: <h1>"World"</h1>
Actual DOM (Updated)
   <div>
     <h1>
       "World"
     </h1>
   </div>
```
#### 5. 결과
업데이트된 실제 DOM: 최소한의 변경 사항만 적용되어 실제 DOM이 업데이트됩니다.

```text
Actual DOM (Updated)
```
