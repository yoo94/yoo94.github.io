---
layout: page
title: Backend_infra
permalink: blog/categories/Backend_infra/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.Backend_infra %}
    {% if post.categories contains "Backend_infra" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">백엔드 & 서버</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
