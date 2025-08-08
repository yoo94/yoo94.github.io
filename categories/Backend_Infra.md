---
layout: page
title: 🛠️ 백엔드 & 서버
permalink: blog/categories/Backend_infra/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.Backend_infra %}
    {% if post.categories contains "Backend_infra" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
