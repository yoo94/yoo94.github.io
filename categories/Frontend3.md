---
layout: page
title: 🌐 Frontend 고급
permalink: blog/categories/Frontend3/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card" style="width: 100%; max-width: 900px; margin: 0 auto;">
  {% for post in site.categories.Frontend3 %}
    {% if post.categories contains "Frontend3" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
