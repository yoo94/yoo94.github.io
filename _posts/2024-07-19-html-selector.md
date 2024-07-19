---
layout: post
title:  "선택자 (selector)"
summary: "차이"
author: yoo94
date: '2024-07-19 12:35:23 +0530'
category: ['myconfused','html','javaScript']
tags: selector
keywords: selector
thumbnail: https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/120px-HTML5_logo_and_wordmark.svg.png
permalink: /blog/javascript-selector/
---

#여러 선택자들
html의 요소를 선택 할 때에는 여러 선택지가 있다.
보통 사용하는 것들은 크게 css선택자와, js에서 html의 요소를 선택하는 방법이 있다.

예를 들어 
## querySelector
css 선택자를 사용하여 문서에서 일치하는 요소들을 반환한다.
```javascript
const element = document.querySelector('.myClass');
const elements = document.querySelectorAll('.myClass');
```

아래 선택자들은 html의 특정 속성을 가지고  id, class 등으로 선택한다.
```javascript
const element = document.getElementById('myId');
const elements = document.getElementsByClassName('myClass');
const elements = document.getElementsByTagName('div');
const elements = document.getElementsByName('username');
```

그럼 뭐가 다를까?
#### css선택자는 NodeList를 반환하고, 
#### 속성 선택자는 HTMLCollection을 반환한다.
이게 뭐가 다른걸까..?
###### NodeList
- 요소들을 특정 시점에 선택하여 작업
- 새로운 요소가 추가되더라도 초기 선택된 요소들만 변경
###### HTMLCollection:
- 선택된 요소들이 실시간으로 업데이트.
- 새로운 요소가 추가되면 자동으로 컬렉션에 포함되어 스타일이 적용.

즉
NodeList
```javascript
const item = document.querySelectorAll('.item');

//스타일 지정
item.forEach(element => {
    element.style.backgroundColor = 'yellow';
});
// 요소 추가
document.getElementById('addItemButton').addEventListener('click', () => {
    const newItem = document.createElement('div');
    newItem.className = 'item';
    newItem.textContent = 'New Item';
    document.body.appendChild(newItem);
    item.forEach(element => {
        element.style.backgroundColor = 'yellow';
    });
    // 새로운 요소는 배경색이 노란색으로 설정되지 않음
});
```
위에 아이템은 저 item에다 백그라운드를 yellow로 지정하고 저 item 클래스를 하나더 추가하면 
yellow가 지정안된 item이 추가된다.

HTMLCollection
```javascript
const item = document.getElementsByClassName('item');

document.getElementById('addItemButton').addEventListener('click', () => {
    const newItem = document.createElement('div');
    newItem.className = 'item';
    newItem.textContent = 'New Item';
    document.body.appendChild(newItem);
    Array.from(item).forEach(item => {
        item.style.backgroundColor = 'yellow';
    });
    // 새로운 요소는 배경색이 노란색으로 설정됨
});
```
