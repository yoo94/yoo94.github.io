---
layout: page
title: webetc
permalink: blog/categories/webetc/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.webetc %}
    {% if post.categories contains "webetc" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
