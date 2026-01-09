---
layout: page
title: 🔢 알고리즘
permalink: blog/categories/Algorithm/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card" >
  {% for post in site.categories.Algorithm %}
    {% if post.categories contains "Algorithm" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
