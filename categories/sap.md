---
layout: page
title: sap
permalink: blog/categories/sap/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.sap %}
    {% if post.categories contains "sap" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
