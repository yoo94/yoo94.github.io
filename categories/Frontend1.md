---
layout: page
title: 🌐 Frontend 초급
permalink: blog/categories/Frontend1/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.Frontend1 %}
    {% if post.categories contains "Frontend1" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
