---
layout: page
title: account
permalink: /blog/categories/account/
---

<h5>Posts by Category: {{ page.title }}</h5>

<div class="card">
  {% for post in site.categories.account %}
    {% if post.categories contains "account" %}
      <li class="category-posts">
        <span>{{ post.date | date_to_string }}</span>
        &nbsp;
        <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</div>
