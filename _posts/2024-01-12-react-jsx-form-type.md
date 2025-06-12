---
layout: post
title:  "JSX란? JSX form 종류"
summary: "JSX Form  종류"
author: yoo94
date: '2024-01-12 14:35:23 +0530'
category: react
tags: react
thumbnail: /blog/postImg/Pasted image 20240505144527.png
permalink: blog/react-jsx-form-type/
---
##### state
```jsx
const [state,setstate] = useState({
   author: "",
   content:"",
   emotion: 1,
 });

  
const handleChangeEvent = (e)=>{
	let name = e.target.name;
	let value = e.target.value;
	setstate({
	  ...state,
	  [name] : value
	})
}

/// state 보내기
const handlesubmmit = ()=>{
	console.log(state)
}
```

##### onChange , onClick
#### input
```jsx
<input name="author" value={autor} onChange={(e)=>{
     setautor(e.target.value)
}}/>
```

#### textarea
```jsx
<textarea name="content" value={content} onChange={(e)=>{
     setcontent(e.target.value)
}}/>
```

#### select
```jsx
<div>
    <select name="emotion" value={state.emotion} onChange={handleChangeEvent}>
     <option value={1}>1</option>
     <option value={2}>2</option>
     <option value={3}>3</option>
     <option value={4}>4</option>
     <option value={5}>5</option>
    </select>
   </div>
```

#### button
```jsx
<div>
	<button name="save" onClick={handlesubmmit}>일기 저장</button>
</div>
```
