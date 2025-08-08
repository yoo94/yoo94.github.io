---
layout: page
title: WebSecurity
permalink: blog/categories/WebSecurity/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.WebSecurity %}
    {% if post.categories contains "WebSecurity" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">보안</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
