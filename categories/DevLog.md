---
layout: page
title: DevLog
permalink: blog/categories/DevLog/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.DevLog %}
    {% if post.categories contains "DevLog" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">개발일지 & 생각</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
