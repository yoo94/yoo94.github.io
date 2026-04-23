---
layout: post
title: "Next.js 블루-그린(Blue-Green) 배포 실전 가이드 (Docker & docker-compose) 간단버전"
summary: "Jenkins와 Docker, Nginx를 활용한 무중단 배포 실전 구축 경험 공유"
author: yoo94
date: "2026-04-17 19:30:23 +0530"
category: [Backend_infra,Frontend3]
keywords: Next.js,블루그린,Blue-Green,무중단배포,젠킨스,Jenkins,도커,Docker,nginx,CI/CD,배포,devops,실전가이드
tags:
  - Next.js
  - 블루그린
  - Blue-Green
  - 무중단배포
  - 젠킨스
  - Jenkins
  - 도커
  - Docker
  - nginx
  - CI/CD
  - 배포
  - devops
  - 실전가이드
thumbnail: /blog/postImg/bluegreen1.png
permalink: blog/devops/bluegreen-nextjs/
---

혹시 상세한 안내가 필요하면 깃헙에 남겨주세요. 이건 그냥 기록이라 .. 대충 써요

# Next.js 블루-그린(Blue-Green) 배포 실전 가이드 (Docker & docker-compose) 1편 기본 세팅

운영업무만 하다가 오랜만에 회사에서 새로운 프로젝트를 하게되었다.
6개월만에 ㅜㅡㅜ 일 좀 주세요..
이전 프로젝트도 프론트엔드팀 리드개발자였고 이번에도 리드를 하게되었고
이번 글은 CI/CD 구축관련 글이 되겠따!!

일단, 젠킨스와 도커를 기반으로 할거라는 점!

1. 젠킨스와 도커 레지스트리는 이전 서비스에서 쓰던 것과 동일한 서버를 사용할 거기 때문에 준비가 되어있다는 점~
2. 서비스를 올릴 서버는 리눅스이고 ~
3. 올릴 서비스는 nextjs 16 standalone으로 배포할거고, api같은게 아직 나오지 않았고 마크업만 된 상태인 서비스 라는 점~
4. 무중단 배포를 위한 블루-그린 배포 할거라는 점~
5. nginx는 설치가 이미 되어있다는 점!

을 참고하시면 되겠다. 아 그리고 순서는 제 맘대로니까 순서 왜 이렇게하냐.. 하지 말아주시길.. ㅎ\_ㅎ

## 1. 블루-그린 배포란?
![블루그린배포란?](/blog/postImg/bluegreen1.png)
- **블루(Blue)와 그린(Green) 두 개의 독립된 환경**을 준비해, 한 쪽(예: 블루)이 서비스 중일 때 다른 쪽(그린)에 새 버전을 배포하고, 배포가 완료되면 트래픽을 전환하는 방식이다.
- 무중단 배포, 빠른 롤백, 안정성 확보에 유리하다.

---

## 2. 프로젝트 구조 예시

```
/deploy/dev/
  ├─ docker-compose-blue.yml
  ├─ docker-compose-green.yml
  └─ Dockerfile
/environment/ <--- env-cmd 라이브러리 사용해서 나눔. 나누는걸 좋아해서 ㅎ_ㅎ
  ├─ .env.development
  └─ .env.production
/package.json
/app, /features, /shared ...
```

근데 요새는 프로젝트 구조를 어떻게 가져가는지 잘 모르겠어서.. 좋은거 있으면 공유 댓글 부탁드려요..

---

1. 형상관리랑(나는 깃랩) 젠킨스랑 연결하기
2. 젠킨스랑 서비스서버랑 연결하기
3. 배포 파이프라인 작성하기
4. 서비스서버 프록시나 업스트림 설정하기

간략하게 이렇게 되겠다.

###### 1. 형상관리 - 젠킨스 연결하기

- 별거 없고 gitlab관련 플러그인 설치한 다음
- 이미지와 같은 설정에서 gitlab 블럭 생기면 거기에 이름,주소,credentials(웬만하면 하세용) 작성하면 접근 가능해 진다.
![블루그린배포란?](/blog/postImg/bluegreen2.png)

![블루그린배포란?](/blog/postImg/bluegreen3.png)

![블루그린배포란?](/blog/postImg/bluegreen4.png)

- 이부분은 ai한테 물어보는게 더 빠를듯

###### 2. 젠킨스랑 서비스 서버랑 연결하기

- ssh 통신을 해야하기 때문에, 젠킨스 관리 → system 가면 맨 밑에 SSH Servers 칸이 있다. 여기에 SSH 키를 등록해야 한다.

![블루그린배포란?](/blog/postImg/bluegreen5.png)
**[서비스 서버에서 SSH 키 생성 → 젠킨스에 등록하는 방법]**

1. **서비스 서버에서 SSH 키 생성**

   ```bash
   ssh-keygen -t rsa -b 4096 -C "deploy-server-key"
   # 기본 경로(예: ~/.ssh/id_rsa) 또는 원하는 경로 입력
   ```

   - `id_rsa` (개인키), `id_rsa.pub` (공개키) 생성됨

2. **서비스 서버의 개인키(id_rsa) 내용을 복사**

   ```bash
   cat ~/.ssh/id_rsa
   ```

   - 전체 내용을 복사

3. **젠킨스 관리 > 시스템 설정 > SSH Servers(또는 Credentials)에서**
   - Kind: SSH Username with private key
   - Username: 서비스 서버 계정명(예: ubuntu, ec2-user 등)
   - Private Key: 위에서 복사한 개인키(id_rsa) 전체 붙여넣기

4. **젠킨스에서 SSH 연결 테스트**
   - 정상 연결되는지 확인

![블루그린배포란?](/blog/postImg/bluegreen6.png)
> ⚠️ 이 방식은 서비스 서버의 개인키가 젠킨스에 저장되므로, 해당 키가 외부에 노출되지 않도록 주의해야 한다..
> 서비스 서버의 `~/.ssh/authorized_keys`에는 별도 작업 필요 없이, 해당 서버 계정으로만 접근이 가능하다.

행여나 권한관련된 에러가 뜬다면
서비스 서버에 Jenkins용 사용자 생성해야한다.

```bash
sudo adduser jenkins
# 또는 이미 있는 계정(ubuntu, deploy 등) 사용 가능
```

실무에서는 배포 전용 계정을 따로 두고, 최소 권한만 부여하는 것이 보안상 안전하고, 나또한 그렇게 했다.

---

3. 배포 파이프라인 작성하기

젠킨스와 서비스서버가 ssh 통신 테스트 까지 됐다면 이제, 배포관련된 스크립트, 쉘파일 등을 작성하면 되겠다.

순서는 중요하지 않고
일단 젠킨스에 파이프 라인을 작성해준다.

개발서버랑 운영서버만 운영 할 서비스이기 때문에 매개변수를 두개 넣어주고 환경변수를 나눠준다.

참고로 nodejs 는 20 이상을 사용해야하기때문에 jenkins에도 추가해야한다.

![블루그린배포란?](/blog/postImg/bluegreen7.png)

환경변수 세팅해주고
깃에서 클론땡겨와주고~
도커에 이미지 5개 이상이면 제일 오래된거 지워주고
이미지 생성해서 레지스트리에 밀어넣어주고
서비스 서버에 띄워져있는 도커이미지 확인해서 그린 블루 배포 해주면 된다.

```sh
if [[ $(docker ps -a --filter name=${BLUE_CONTAINER_NAME} --format '{{.Names}}') ]]; then
    # blue가 있으면 green을 새로 띄움
    docker pull ${DOC_HUB_REG}:${tag}
    docker run -d --name ${GREEN_CONTAINER_NAME} -p 8086:3000 ${DOC_HUB_REG}:${tag}
    sleep 10
    /bin/cp -f ${HOME_DIR}/deploy/nginx_upstream_green.conf ${CONF_DIR}/upstream
    docker stop ${BLUE_CONTAINER_NAME} || true
    docker rm ${BLUE_CONTAINER_NAME} || true
    sudo /usr/bin/systemctl reload nginx.service
else
    # blue가 없으면 blue를 새로 띄움
    docker pull ${DOC_HUB_REG}:${tag} # 도커 레지스트리에서 최신 이미지를 받아온다
    docker run -d --name ${BLUE_CONTAINER_NAME} -p 8085:3000 ${DOC_HUB_REG}:${tag} # blue 컨테이너를 백그라운드로 실행(8085→3000 포트 매핑)
    sleep 10 # 컨테이너가 완전히 뜰 때까지 10초 대기(헬스체크 대용)
    /bin/cp -f ${HOME_DIR}/deploy/nginx_upstream_blue.conf ${CONF_DIR}/upstream # blue용 nginx 업스트림 설정 파일을 복사(트래픽 전환 준비)
    /* 기존 green 컨테이너가 있으면 중지 및 삭제 */
    docker stop ${GREEN_CONTAINER_NAME} || true # green 컨테이너 중지(없어도 에러 무시)
    docker rm ${GREEN_CONTAINER_NAME} || true   # green 컨테이너 삭제(없어도 에러 무시)
    sudo /usr/bin/systemctl reload nginx.service # nginx 설정을 reload하여 트래픽을 blue 컨테이너로 전환
fi
```

blue/green 컨테이너를 번갈아가며 띄우고, nginx 업스트림을 바꿔 무중단 배포하는 것이다.

컨테이너 교체 후 nginx reload로 트래픽 전환까지 해주면 젠킨스에 있는 파이프라인은 역할 끝!

4. 서비스서버 프록시나 업스트림 설정하기

이제 젠킨스에서 실행할 것들을 설정해주면 된다.

4-1. nginx에는 프록시 설정을해서 도메인 연결시 해당 도커 이미지로 트래픽연결되게 설정해줘야한다.
server블록을 가진 conf파일이 있을건데 그건 스스로 찾아야한다.
보통 nginx/conf/여기에 .conf파일들 안에 설정 되어있을거임

그리고 서비스 이름 정했으면 그거 계속 일관되게 사용하자.
예를들어 youtube-you면 이걸 사용해야지 어디에는 youtube_you 어디에는 youtube-you 이렇게 쓰면
나중에 곤란해짐

```sh
server {
    listen       443 ssl;
    http2        on;
    ....
    location{
         proxy_pass http://여기에서비스이름정해서넣어;
    }
}
```

4-2. 위에 설정해준 젠킨스를 한번 실행하면 에러들이 난다. 디렉토리가 없다던가 그런것들..서비스 서버에 디렉토리들을 만들어주고, 젠킨스가 실행할 .sh 나 .conf를 넣어준다.

그 디렉토리에서

```sh
# nginx_upstream_blue.conf는
upstream 서비스명 {
    server 127.0.0.1:8085;
}
# nginx_upstream_green.conf는
upstream 서비스명 {
    server 127.0.0.1:8086;
}
```

이런식으로 해서 새로 배포 될때마다 실제 upstream을 바꿔주면 되겠다.

```bash
# 아래 명령어가 cp로 포트 바꿔줌
# green을 새로 띄울 때는
/bin/cp -f ${HOME_DIR}/deploy/nginx_upstream_green.conf ${CONF_DIR}/upstream
# blue를 새로 띄울 때는
/bin/cp -f ${HOME_DIR}/deploy/nginx_upstream_blue.conf ${CONF_DIR}/upstream
```

이렇게 되면 젠킨스에서 파이프라인 실행할때마다 프로세스는

깃랩에서 소스 땡겨가서 빌드하고 -> 이미지생성하고 -> 도커레지스트리에 넣어주고
-> 서비스 서버에서 sh 실행시켜서 도커 레지스트리에서 이미지 가져와서 실행

이렇게 된다.
