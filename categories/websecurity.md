---
layout: page
title: 🔐 보안 WebSecurity
permalink: blog/categories/WebSecurity/
---

<h5>Posts by Category: {{ page.title }}</h5>


<div class="card" >
  {% for post in site.categories.WebSecurity %}
    {% if post.categories contains "WebSecurity" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>