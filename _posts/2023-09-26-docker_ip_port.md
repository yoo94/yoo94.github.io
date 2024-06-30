---
layout: post
title:  "docker ip,port 확인"
summary: ""
author: yoo94
date: '2023-09-26 20:35:23 +0530'
category: docker
tags: docker
keywords: docker
thumbnail: https://i.namu.wiki/i/KHNL7eMAx46cUBgM-wQRF1OPwkvHCF6oKMXDD3MpOwiUZedqQ_IZuA-vI2d1jMZIkDm9zQCFxb4FFS1HKvqJd5iHeA3PYSFRBYOYewHg6wvR4BwrQjucTirP9s5I4GGtpGBrtAqGgKl_vlGROsWrTA.svg
permalink: /blog/docker_ip_port/
---
도커에서 외부와 매핑된 포트를 확인하려면 다음 명령어 중 하나를 사용할 수 있습니다.

1. **도커 컨테이너의 상세 정보 확인:**

   `docker inspect 컨테이너_이름_또는_ID`

   위 명령어를 실행하면 컨테이너의 상세 정보가 JSON 형식으로 출력됩니다. 여기에서 "Ports" 섹션을 찾아보면 외부와 매핑된 포트 정보를 확인할 수 있습니다.

2. **도커 컨테이너 목록 및 포트 정보 확인:**

   `docker ps`

   위 명령어로 현재 실행 중인 도커 컨테이너 목록을 확인할 수 있습니다. 포트 매핑 정보는 "PORTS" 열에 표시됩니다.

2. **도커 컨테이너 목록 및 포트 정보 확인:**
   bashCopy code

   `CONTAINER ID   IMAGE        COMMAND               CREATED       STATUS       PORTS                    NAMES abc1234        my_image     "command"             2 hours ago   Up 2 hours   0.0.0.0:8080->80/tcp     my_container`

   위 예시에서는 8080 포트가 호스트와 80 포트가 컨테이너와 매핑되어 있습니다.

3. **도커 컨테이너의 포트만 확인:**

   `docker port 컨테이너_이름_또는_ID`

   위 명령어를 사용하면 특정 컨테이너의 포트 매핑 정보만 확인할 수 있습니다.


위의 명령어 중 하나를 선택하여 사용하면 도커 컨테이너의 외부와 매핑된 포트를 확인할 수 있습니다.