---
layout: post
title:  "도커 gitlab컨테이너 업데이트하기"
summary: "보안이슈로 업데이트해야한다!"
author: yoo94
date: '2023-09-02 17:35:23 +0530'
category: Backend_infra
tags:
- Docker
- GitLab
- 컨테이너
- 백엔드인프라
- CI/CD
- docker-compose
- GitLab업데이트
- 백업복원
- 보안패치
- DevOps
keywords: Docker, GitLab, GitLab CE, 컨테이너 업데이트, docker-compose, GitLab 백업, restore.sh, GitLab 업그레이드, GitLab 버전 관리, GitLab 보안 패치, GitLab 이미지 태그, GitLab migration, GitLab-ctl, GitLab-rake
thumbnail: https://i.namu.wiki/i/KHNL7eMAx46cUBgM-wQRF1OPwkvHCF6oKMXDD3MpOwiUZedqQ_IZuA-vI2d1jMZIkDm9zQCFxb4FFS1HKvqJd5iHeA3PYSFRBYOYewHg6wvR4BwrQjucTirP9s5I4GGtpGBrtAqGgKl_vlGROsWrTA.svg
permalink: blog/docker_gitlab_update/
---
https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/

위 순서에 따라 버전을 하나씩 올려가면서 진행

#### 절차

![GitLab 업데이트 절차](/blog/postImg/Pasted image 20240119135605.png)

도커에 올라가 있는 깃랩을 업데이트한다.

![GitLab 현재 버전 확인](/blog/postImg/Pasted image 20240119135920.png)

![GitLab 버전 체크](/blog/postImg/Pasted image 20240119140116.png)

먼저 로컬 우분투에 도커 설치해서 올려보기로함,

![GitLab 백업 파일](/blog/postImg/Pasted image 20240119140854.png)

위 사진처럼 backup 파일들을 로컬로 가지고옴

```shell
scp 아이디@아이피:다운받을경로+파일이름 받을내로컬장소
scp unipost@unidocu:/home/unipost/backups/gitlab_config.tar.gz ./
scp unipost@unidocu:/home/unipost/backups/jenkins_data.tar.gz .
```


본사의 gitlab_* .tar.gz 들 을 가지고 왔다.

![GitLab 백업 파일 목록](/blog/postImg/Pasted image 20240119161424.png)

![GitLab 백업 스크립트](/blog/postImg/Pasted image 20240119150237.png)

이건 그냥 바로가기 만들어준거임 참고용 >,<

wls를 해서 내 pc 우분투에서 작업
아래 명령어로 백업 파일들에대한 볼륨을 하나씩 만들어 준다.
```shell
./restore.sh gitlab_* gitlab_*.tar.gz
```

![이미지](/blog/postImg/Pasted image 20240119151501.png)

그럼 아래 사진처럼 볼륨 세개가 생김
![이미지](/blog/postImg/Pasted image 20240119151427.png)


그다음 gitlab에 있는 우리회사 도커 소스를 가지고 온다. 거기에는
docker-compose.yml 이있는데 여기에 설정이 되어있다.
필요한것만 띄우게 정리하고
```shell
docker compose up -d
```
![이미지](/blog/postImg/Pasted image 20240119152047.png)

nginx, gitlab,smtp 만 설정하여 띄움
![이미지](/blog/postImg/Pasted image 20240119152642.png)

```shell
docker container logs -f gitlab
```
위 소스를 통해서 gitlab이 정상적으로 떴는지 확인

이제 gitlab 버전을 업그레이드 해줘야한다.
![이미지](/blog/postImg/Pasted image 20240119135605.png)

이 flow 대로 진행하는데, 먼저 15.11.13 ce 버전이다.
저 위에 있는 명령어는 썡으로 업그레이드하는 명령어이고
docker_compose.yml 을 통해 업그레이드 할 예정이기 떄문에

위의 버전을 아래의 사이트에서 검색해 준다.
https://hub.docker.com/r/gitlab/gitlab-ce/tags

![이미지](/blog/postImg/Pasted image 20240119164522.png)

여기 나와있는 gitlab/gitlab~~ 이거를 image에 넣어주고

![이미지](/blog/postImg/Pasted image 20240119164332.png)

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
![이미지](/blog/postImg/Pasted image 20240119155118.png)


차근차근 올려서 잘 되는지 확인
![[Pasted image 20240119173040.png]]
![이미지](/blog/postImg/Pasted image 20240119173040.png)


컨테이너 접속
```shell
docker container exec -it 컨테이너명 bash
```
gitlab-rake db: migration:status --tasks
gitlab-ctl reconfigure
