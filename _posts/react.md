---
layout: post
title:  "Added Latex Support"
summary: Writing Equations using Latex
author: yoo94
date: '2020-10-24 10:35:23 +0530'
category: react
thumbnail: /assets/img/posts/code.jpg
keywords: devlopr jekyll, how to use devlopr, devlopr, how to use devlopr-jekyll, devlopr-jekyll tutorial,best jekyll themes
usemathjax: true
permalink: /blog/react/
---

To add categories in blog posts all you have to do is add a **category** key with category values in frontmatter of the post :

```yml
---
category: ['react']
---
```

Then to render this category using link and pages. All we need to do is,

1. Create a new file with [your_category_name].md inside categories folder.

2. Copy categories/sample_category.md file and replace the content in [your_category_name].md in that. (Please don't copy the code below its just sample, since it renders the jekyll syntax dynamically)
