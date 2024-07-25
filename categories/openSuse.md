---
layout: page
title: openSuse
permalink: blog/categories/openSuse/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.openSuse %}
    {% if post.categories contains "openSuse" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
