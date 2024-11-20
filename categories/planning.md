---
layout: page
title: planning
permalink: blog/categories/planning/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.planning %}
    {% if post.categories contains "planning" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
