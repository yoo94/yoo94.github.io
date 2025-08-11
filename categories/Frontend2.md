---
layout: page
title: 🌐 Frontend 중급
permalink: blog/categories/Frontend2/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card" style="width: 100%; max-width: 900px; margin: 0 auto;">
  {% for post in site.categories.Frontend2 %}
    {% if post.categories contains "Frontend2" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>
