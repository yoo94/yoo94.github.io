---
layout: page
title: 🧠 개발 일지 & 회고 & 생각
permalink: blog/categories/DevLog/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.DevLog %}
    {% if post.categories contains "DevLog" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
