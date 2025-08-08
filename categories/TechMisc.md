---
layout: page
title: TechMisc
permalink: blog/categories/TechMisc/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.TechMisc %}
    {% if post.categories contains "TechMisc" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">기타 기술 & 툴</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
