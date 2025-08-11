---
layout: page
title: 📚 독후감 BookReport
permalink: blog/categories/BookReport/
---

<h5>Posts by Category: {{ page.title }}</h5>


<div class="card" >
  {% for post in site.categories.BookReport %}
    {% if post.categories contains "BookReport" %}
      <li class="category-posts">
        <a href="{{ post.url }}">{{ post.title }}</a>
        &nbsp;
        <span>{{ post.date | date_to_string }}</span>
      </li>
    {% endif %}
  {% endfor %}
</div>