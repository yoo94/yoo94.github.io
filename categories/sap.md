---
layout: page
title: sap
permalink: /blog/categories/sap/
---

<h5> Posts by Category : {{ page.title }} </h5>
<div class="card">
    {% for post in site.categories.sap %}
        <li class="category-posts">
            <span>{{ post.date | date_to_string }}</span>
            <a href="{{ post.url }}">{{ post.title }}</a>
        </li>
    {% endfor %}
</div>