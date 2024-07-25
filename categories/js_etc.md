---
layout: page
title: webpack
permalink: blog/categories/js_etc/
---

<h5> Posts by Category : {{ page.title }} </h5>
<div class="card">
    {% for post in site.categories.js_etc %}
        <li class="category-posts">
            <span>{{ post.date | date_to_string }}</span>
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endfor %}
</div>

