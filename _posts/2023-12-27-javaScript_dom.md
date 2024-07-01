---
layout: post
title:  "DOM 조작"
summary: "DOM 이란?"
author: yoo94
date: '2023-12-27 17:35:23 +0530'
category: javaScript
tags: javaScript
keywords: dom
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/1200px-Unofficial_JavaScript_logo_2.svg.png
permalink: /blog/javaScript_dom/
---
# DOM 이란?

DOM ( DOM은 독립적으로 디자인된 기술이기 때문에, 어떠한 언어에서도 가능하고, 가장 많이 사용되는 언어가 JS일 뿐이다.) - 문서 객체 모들 The Document Object Model 의 약자이다 - html, xml문서

---

console.dir(elem)과 console.log(elem)의 차이  
두 명령어는 인수를 출력해준다. 인수가 **자바스크립트 객체**라면 보통 같은 결과를 보여주지만 인수가 **DOM 요소일 때**는 다른 결과를 출력한다.  
**console.log(el)는 요소의 DOM 트리를 출력.  
**console.dir(el)는 요소를 DOM 객체처럼 취급하여 출력. 따라서 프로퍼티를 확인하기 쉽다.
<img src="/assets/postImg/Pasted image 20240202164423.png" alt="Pasted image 20240202164423.png" style="max-width:100%;">

자바스크립트에서 DOM은 document 객체에 구현되어 있기 때문에 브라우저에서 작동되는 자바스크립트 코드에서는 document 객체를 조회할 수 있다.

`document.body`를 `console`로 찍어보면 body의 엘리먼트(Element)들을 확인할 수 있다.
body의 자식 엘리먼트도 찾을 수 있다.

```javascript
console.dir(document.body.children);
```

반대로 부모 엘리먼트를 찾고 싶을 때는 `parentElement`를 써주면 된다.

```javascript
let children = document.body.children[1];
children.parentElement;
```

createElement - CREATE  
querySelector, querySelectorAll - READ  
textContent, id, classList, setAttribute - UPDATE  
remove, removeChild, innerHTML = "" , textContent = "" - DELETE  
appendChild - APPEND  
innerHTML과 textContent의 차이  
Advanced Challenge  
DOM의 더 깊은 내용에 대해서 이해할 수 있다.  
createDocumentFragment를 활용하여, 더 효율적으로 DOM을 제어할 수 있다.  
HTML5 template tag 사용법을 이해할 수 있다.  
children과 childNodes의 차이를 이해할 수 있다.  
remove와 removeChild의 차이를 이해할 수 있다.  
같은 엘리먼트를 appendChild 하면, 기존 엘리먼트를 복사할까?  
좌표 정보 조회를 할 수 있다. - offsetTop...  
크기 정보 조회를 할 수 있다. - offsetWidth...

## 1) Element 생성

DOM을 JavaScript로 조작하여 HTML Element를 추가하거나 삭제, 혹은 내용을 변경할 수 있다.

우선 추가하는 방법부터 살펴보자.

`createElement()` 를 사용해 엘리먼트를 생성해 줄 수 있다.

div를 하나 생성해준다고 예시를 들어보자.
```javascript
const tweetDiv = document.createElement('div');
```

<img src="/assets/postImg/Pasted image 20240202164646.png" alt="Pasted image 20240202164646.png" style="max-width:100%;">

## 2) Element 추가

그림에서 봤던 공중에 떠있는 엘리먼트를, `append` 해야만 실제 웹 페이지 상에도 보여진다.

```javascript
document.body.append(tweetDiv);
```
### append()

ParentNode.append() 메서드는 ParentNode의 마지막 자식 뒤에 Node 객체 또는 DOMString 객체를 삽입한다. 여러개를 삽입 할 수 있다.

요소나 문자를 추가하는 예시들을 보자.  
요소(element) 추가하기

```javascript
let parent = document.createElement("div");
let p = document.createElement("p");
parent.append(p);
console.dir(parent.childNodes)  //NodeList(1)  0: p
```

문자(text) 추가하기

```javascript
let parent = document.createElement("div");
parent.append("Some text");

console.log(parent.textContent); // "Some text"
```

요소(element)와 문자(text) 함께 추가하기

```javascript
let parent = document.createElement("div");
let p = document.createElement("p");
parent.append("Some text", p);

console.dir(parent.childNodes); // NodeList [ #text "Some text", <p> ]
```

### appendChild()

Node.appendChild() 메소드는 한 노드를 특정 부모 노드의 자식 노드 리스트 중 마지막 자식으로 붙인다. 하나의 노드만 붙일 수 있다. 만약 주어진 노드가 이미 문서에 존재하는 노드를 참조하고 있다면 appendChild() 메소드는 노드를 현재 위치에서 새로운 위치로 이동시킨다.

이는 한 노드가 문서상의 두 지점에 동시에 존재할 수 없다는 것을 의미한다. 그래서 만약 노드가 이미 부모를 가지고 있다면 우선 삭제되고 새로운 위치로 이동한다.

```javascript
// 새로운 단락 요소를 생성하고 문서에 있는 바디 요소의 끝에 붙인다.
let p = document.createElement("p");
document.body.appendChild(p);
```
### append() VS appendChild()

- ParentNode.append()는 DOMString 객체도 추가 가능 but, Node.appendChild()는 오직 Node 객체만 허용

- ParentNode.append()는 반환하는 값이 없다. 한편 Node.appendChild()는 추가한 Node 객체를 반환한다.

- ParentNode.append()는 여러 개 노드와 문자를 추가할 수 있다. 한편 Node.appendChild()는 오직 노드 하나만 추가할 수 있다.


### prepend()

ParentNode의 첫번째 자식으로 Node 객체 또는 DOMString 객체를 삽입한다.

### after()

선택한 Element 뒤에 새 Element를 추가한다.

### before()

선택한 Element 앞에 새 Element를 추가한다.

## 3) Element 조회

querySelector는 한글로 셀렉터를 기반으로 한 질문을 한다, 쿼리를 날린다라는 의미이다.

### querySelector()

선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 Element를 반환한다. 일치하는 요소가 없으면 null을 반환한다.

```html
<body>
  <div class="tweet"></div>
  <div class="tweet"></div>
  <div class="tweet"></div>
  <div class="tweet"></div>
</body>
```

```javascript
const oneTweet = document.querySelector('.tweet')
```

### querySelectorAll()

선택자를 통해 여러개의 Element를 가져오기 위해서 사용한다.

querySelectorAll로 class가 tweet인 Element에 접근할 수있다.

```html
<body>
  <div class="tweet"></div>
  <div class="tweet"></div>
  <div class="tweet"></div>
  <div class="tweet"></div>
</body>
```

```javascript
const oneTweet = document.querySelectorAll('.tweet')
```

### getElementById()

Element의 id로 접근할 수 있다.

### getElementByClassName() / getElementsByClassName()

Element의 class 이름으로 접근할 수 있다.

## 4) Element update

### setAttribute(name, value)

지정된 요소의 속성 값을 설정한다. 속성이 이미 존재하면 값이 업데이트 되고, 그렇지 않으면 지정된 이름과 값으로 새 속성이 추가된다.

- 매개 변수 : name  
  DOMString값 설정되는 속성의 이름을 지정.
- 매개 변수 : value  
  DOMString값을 포함는 속성에 할당.

```javascript
let aElement = document.createElement('a')

aElement.setAttibute('id', 'javascipt')
```

### classList.add()

Element에 class name을 추가할 수 있다.

```javascript
let aElement = document.createElement('a')

aElement.classList.add('name')
```

### textContent

Element 및 Node에 텍스트를 추가할 수 있는 메서드이다.  
반환값은 문자열 또는 `null`이다.

```javascript
aElement.textContent = 'awesome'
```

### innerHTML

이 방법도 되긴 하는데, innerHTML 사용은 꼭 필요하지 않으면 쓰지 않는 것이 좋다.

```javascript
 aElement.innerHTML = 'awesome'
```

innerHTML는 이름 그대로 HTML을 반환한다. HTML tag를 직접 삽입하여 실행하는 형태의 메소드는 늘 이런 위험을 가지고 있다.

## 5) Element 제거

### removeChild() VS remove()

> 자식 Node를 삭제하는 메서드이다.

**remove()**는 노드를 메모리에서 삭제하고 종료한다.  
반면에 **removeChild()**는 메모리에 해당 노드는 그대로 존재하며, 부모 노드와의 부모-자식관계를 끊어 DOM 트리에서 제거한다. 최종적으로는 관계를 끊은 해당 노드의 참조를 반환한다.
```javascript
const container = document.querySelector('#container')
const tweetDiv = document.createElement('div')
container.append(tweetDiv)
```

```javascript
tweetDiv.remove() // 이렇게 append 했던 엘리먼트를 삭제할 수 있다.
```
