---
layout: post
title:  "리눅스 tail사용하기"
summary: ""
author: yoo94
date: '2023-06-17 17:35:23 +0530'
category: linux
tags: linux
keywords: linux, tar, gz
thumbnail: https://i.namu.wiki/i/u3xN1dzCaWAEf6Tb5X0oSiVFU4DTQ_355FJmLCSTY7GZNyOnv60tkvcu0s0cD4Oce9vK6kylpAIEU-BYcju6Ww.webp
permalink: /blog/linux_tail/
---
**tail 명령어**  
tail 명령어는 파일의 마지막 행을 기준으로 지정한 행까지의 파일 내용 일부를 출력해주는 명령어입니다. 기본값으로는 마지막 10줄을 출력하며 주로 tail은 리눅스에서 오류나 파일 로그를 실시간으로 확인할 때 매우 유용하게 사용됩니다.

# 파일 마지막 부분을 출력하는 명령어

```shell
tail [옵션][파일명]

tail filename.txt

tail -f filename.txt
```

#### 자주 사용하는 옵션

- **-f :** tail을 종료하지 않고 파일의 업데이트 내용을 실시간으로 계속 출력한다.
- **-n (라인 수) :** 파일의 마지막줄부터 지정한 라인수까지의 내용을 출력한다.
- **-c (바이트 수) :** 파일의 마지막부터 지정한 바이트만큼의 내용을 출력한다.
- **-q :** 파일의 헤더와 상단의 파일 이름을 출력하지 않고 내용만 출력한다.
- **-v :** 출력하기전에 파일의 헤더와 이름 먼저 출력한 후 파일의 내용을 출력한다.

### 실시간 로그 보기 (tail + grep)

```shell
Copytail -f mylog.log | grep 192.168.15.86
```

### 여러 파일을 동시에 표시하는 법

```shell
Copytail mylog1.log mylog2.log
```