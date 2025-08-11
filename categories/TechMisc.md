---
layout: page
title: 🧰 기타 기술 & 툴 TechMisc
permalink: blog/categories/TechMisc/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card" style="width: 100%; max-width: 900px; margin: 0 auto;">
  {% for post in site.categories.TechMisc %}
    {% if post.categories contains "TechMisc" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>