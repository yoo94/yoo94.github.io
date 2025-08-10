---
layout: post
title:  "도커 gitlab컨테이너 업데이트하기"
summary: "보안이슈로 업데이트해야한다!"
author: yoo94
date: '2023-09-02 17:35:23 +0530'
category: Backend_infra
tags: docker
keywords: docker
thumbnail: https://i.namu.wiki/i/KHNL7eMAx46cUBgM-wQRF1OPwkvHCF6oKMXDD3MpOwiUZedqQ_IZuA-vI2d1jMZIkDm9zQCFxb4FFS1HKvqJd5iHeA3PYSFRBYOYewHg6wvR4BwrQjucTirP9s5I4GGtpGBrtAqGgKl_vlGROsWrTA.svg
permalink: blog/docker_gitlab_update/
---
https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/

위 순서에 따라 버전을 하나씩 올려가면서 진행

#### 절차
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119135605.png" alt="Pasted image 20240119135605.png" style="max-width:100%;; height:70%;">
</div>
도커에 올라가 있는 깃랩을 업데이트한다.

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119135920.png" alt="Pasted image 20240119135920.png" style="max-width:100%;; height:70%;">
</div>

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119140116.png" alt="Pasted image 20240119140116.png" style="max-width:100%;; height:70%;">
</div>

먼저 로컬 우분투에 도커 설치해서 올려보기로함,

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119140854.png" alt="Pasted image 20240119140854.png" style="max-width:100%;; height:70%;">
</div>

위 사진처럼 backup 파일들을 로컬로 가지고옴

```shell
scp 아이디@아이피:다운받을경로+파일이름 받을내로컬장소
scp unipost@unidocu:/home/unipost/backups/gitlab_config.tar.gz ./
scp unipost@unidocu:/home/unipost/backups/jenkins_data.tar.gz .
```


본사의 gitlab_* .tar.gz 들 을 가지고 왔다.
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119161424.png" alt="Pasted image 20240119161424.png" style="max-width:100%;; height:70%;">
</div>
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119150237.png" alt="Pasted image 20240119150237.png" style="max-width:100%;; height:70%;">
</div>

이건 그냥 바로가기 만들어준거임 참고용 >,<

wls를 해서 내 pc 우분투에서 작업
아래 명령어로 백업 파일들에대한 볼륨을 하나씩 만들어 준다.
```shell
./restore.sh gitlab_* gitlab_*.tar.gz
```

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119151501.png" alt="Pasted image 20240119151501.png" style="max-width:100%;; height:70%;">
</div>

그럼 아래 사진처럼 볼륨 세개가 생김
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119151427.png" alt="Pasted image 20240119151427.png" style="max-width:100%;; height:70%;">
</div>


그다음 gitlab에 있는 우리회사 도커 소스를 가지고 온다. 거기에는
docker-compose.yml 이있는데 여기에 설정이 되어있다.
필요한것만 띄우게 정리하고
```shell
docker compose up -d
```
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119152047.png" alt="Pasted image 20240119152047.png" style="max-width:100%;; height:70%;">
</div>

nginx, gitlab,smtp 만 설정하여 띄움
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119152642.png" alt="Pasted image 20240119152642.png" style="max-width:100%;; height:70%;">
</div>

```shell
docker container logs -f gitlab
```
위 소스를 통해서 gitlab이 정상적으로 떴는지 확인

이제 gitlab 버전을 업그레이드 해줘야한다.
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119135605.png" alt="Pasted image 20240119135605.png" style="max-width:100%;; height:70%;">
</div>

이 flow 대로 진행하는데, 먼저 15.11.13 ce 버전이다.
저 위에 있는 명령어는 썡으로 업그레이드하는 명령어이고
docker_compose.yml 을 통해 업그레이드 할 예정이기 떄문에

위의 버전을 아래의 사이트에서 검색해 준다.
https://hub.docker.com/r/gitlab/gitlab-ce/tags

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119164522.png" alt="Pasted image 20240119164522.png" style="max-width:100%;; height:70%;">
</div>

여기 나와있는 gitlab/gitlab~~ 이거를 image에 넣어주고

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119164332.png" alt="Pasted image 20240119164332.png" style="max-width:100%;; height:70%;">
</div>

중간에 nginx 만 다시 실행하고 싶으면
```shell
 docker container stop nginx
 docker container start nginx
```

아무튼 모든 컨테이너를 다시 올리면
```shell
 docker compose up -d
```
이미지를 읽어서 자동으로 업데이트 해준다.
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119155118.png" alt="Pasted image 20240119155118.png" style="max-width:100%;; height:70%;">
</div>


차근차근 올려서 잘 되는지 확인
![[Pasted image 20240119173040.png]]
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119173040.png" alt="Pasted image 20240119173040.png" style="max-width:100%;; height:70%;">
</div>


컨테이너 접속
```shell
docker container exec -it 컨테이너명 bash
```
gitlab-rake db: migration:status --tasks
gitlab-ctl reconfigure
