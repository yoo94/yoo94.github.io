---
layout: post
title:  "리눅스 크론 cron 사용하기"
summary: "명령어"
author: yoo94
date: '2023-08-04 17:35:23 +0530'
category: linux
tags: linux
keywords: linux, tar, gz
thumbnail: https://i.namu.wiki/i/u3xN1dzCaWAEf6Tb5X0oSiVFU4DTQ_355FJmLCSTY7GZNyOnv60tkvcu0s0cD4Oce9vK6kylpAIEU-BYcju6Ww.webp
permalink: blog/cron/
---
시작
```shell
sudo service cron start
```

##### **1. 크론탭 설정** 

```shell
$ crontab -e
```

위 명령어를 사용하여 crontab에서 실행할 명령어를 설정할 수 있습니다.

(각 라인마다 앞에 #로 되어있는 부분은 주석입니다.)

쭉 내려가서 맨 밑에 라인에 한 줄씩 원하는 명령어를 추가하면 됩니다.

간단하게 작성방법을 살펴보겠습니다. 

앞부분은 시간 관련된 내용을 작성하고 그 뒤에 실행할 명령어를 입력하는 방식입니다.
```shell
$ * * * * * sh /home/user/test.sh
```

시간 관련된 내용을 살펴보면 

분(0-59), 시간(0-23), 일(1-31), 월(1-12), 요일(0-7) 순서로 작성하게 됩니다.

숫자로 시간을 지정하거나 그렇지 않다면 *로 입력하여 다섯 가지를 전부 입력해야 합니다.

*로 입력한다면 그 위치의 내용은 모든 주기에 실행한다고 생각하면 됩니다.(매분, 매시간, 매일, 매월, 모든 요일)

##### **2. 크론탭 설정 목록 조회** 

설정을 완료했다면 내가 설정한 내용을 확인할 수도 있습니다.

```shell
$ crontab -l
```

위 명령어를 사용하여 crontab의 설정 내용을 조회할 수 있습니다.

##### **3. 크론탭 로그 보기**

로그를 통해 crontab에 설정한 내용들이 내가 설정한 시간에 잘 실행이 되었는지 확인해볼 수 있습니다.

syslog에서 CRON으로 검색하여 그 내용을 확인합니다.

```shell
tail -f /var/log/syslog|grep CRON
```

