---
layout: post
title:  "docker compose 설정 개념"
summary: "명령어"
author: yoo94
date: '2023-09-26 17:35:23 +0530'
category: Backend_infra
tags: docker
keywords: docker
thumbnail: https://i.namu.wiki/i/KHNL7eMAx46cUBgM-wQRF1OPwkvHCF6oKMXDD3MpOwiUZedqQ_IZuA-vI2d1jMZIkDm9zQCFxb4FFS1HKvqJd5iHeA3PYSFRBYOYewHg6wvR4BwrQjucTirP9s5I4GGtpGBrtAqGgKl_vlGROsWrTA.svg
permalink: blog/docker_compose/
---
Docker compose란, 여러 개의 컨테이너로부터 이루어진 서비스를 구축, 실행하는 순서를 자동으로 하여, 관리를 간단히하는 기능이다.

Docker compose에서는 compose 파일을 준비하여 커맨드를 1회 실행하는 것으로, 그 파일로부터 설정을 읽어들여 모든 컨테이너 서비스를 실행시키는 것이 가능하다.

```yml
version: '3'
services:
    db:
      image: postgres:latest
      container_name: postgres
      restart: always
      ports:
        - "5432:5432"
      environment:
        POSTGRES_USER: "${DB_USER_ID}"
        POSTGRES_PASSWORD: "${DB_USER_PASSWORD}"
      volumes:
        - ./data:/var/lib/postgresql/data
```

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240616200511.png" alt="Pasted image 20240616200511.png" style="max-width:auto;; height:auto;">
</div>
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240616200520.png" alt="Pasted image 20240616200520.png" style="max-width:auto;; height:auto;">
</div>


```yml
docker-compose up
```
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240616201405.png" alt="Pasted image 20240616201405.png" style="max-width:auto;; height:auto;">
</div>
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240616201517.png" alt="Pasted image 20240616201517.png" style="max-width:auto;; height:auto;">
</div>
