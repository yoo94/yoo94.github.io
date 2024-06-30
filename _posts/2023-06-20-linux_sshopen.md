---
layout: post
title:  "리눅스 OS 확인하기, SSH 오픈하기"
summary: ""
author: yoo94
date: '2023-06-20 17:35:23 +0530'
category: linux
tags: linux
keywords: linux, tar, gz
thumbnail: https://i.namu.wiki/i/u3xN1dzCaWAEf6Tb5X0oSiVFU4DTQ_355FJmLCSTY7GZNyOnv60tkvcu0s0cD4Oce9vK6kylpAIEU-BYcju6Ww.webp
permalink: /blog/linux_ssh_os/
---
## os확인
상세하게
```shell
$cat /etc/*release
```

간단하게
```shell
$cat /etc/issue*
```

커널정보
```shell
$cat /proc/version
```

## open ssh 설치

```shell
yum install openssh-server openssh-clients openssh-askpass`

vi /etc/ssh/sshd_config
```