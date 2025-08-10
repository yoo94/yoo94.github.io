---
layout: page
title: 🐞 디버깅 & 개발 불편 (인간관계 포함)
permalink: blog/categories/Debug/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.Debug %}
    {% if post.categories contains "Debug" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
