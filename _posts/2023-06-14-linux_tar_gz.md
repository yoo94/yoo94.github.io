---
layout: post
title:  "리눅스 tar, gz, zip 압축 및 해제"
summary: "명령어 사용법"
author: yoo94
date: '2023-06-14 17:35:23 +0530'
category: linux
tags: linux
keywords: linux, tar, gz
thumbnail: https://i.namu.wiki/i/u3xN1dzCaWAEf6Tb5X0oSiVFU4DTQ_355FJmLCSTY7GZNyOnv60tkvcu0s0cD4Oce9vK6kylpAIEU-BYcju6Ww.webp
permalink: /blog/linux_tar_gz/
---
##  tar 명령어 사용법 

tar는 Tape ARchiver 테이프 아카이버의 앞글자를 딴 말로 정확히 말하자면 압축방식은 아니고 일종의 묶음 형태입니다. tar파일은 리눅스 및 유닉스에서 가장 많이 사용되는 형태로써 tar로 묶이기 전 파일들의 속성과 디렉터리 구조등을 모두 보존할 수 있고 압축 & 압축해제 등의 작업을 거치면서 파일이 변경, 소실될 염려가 없기 때문에 소스 배포 파일을 만드는 용도로 자주 사용됩니다.

### tar 압축하기

```shell
Copytar -cvf [파일명.tar] [대상 폴더명]

# 현재 위치의 pjt폴더를 test.tar로 묶기
tar -cvf test.tar pjt
```

### tar 압축해제

```shell
Copytar -xvf [파일명.tar]

# 현재 위치의 test.tar를 압축해제
tar -xvf test.tar
```

<<<<<<< HEAD
=======
### tar 특정 디렉토리만 압축해제

```shell
tar xvfzp jenkins_data.tar.gz jenkins_home/unidocu
```

### tar 명령어 옵션

- -f : 대상 tar 아카이브 지정. (기본 옵션)
- -c : tar 아카이브 생성. 기존 아카이브 덮어쓰기. (파일 묶을 때 사용)
- -x : tar 아카이브에서 파일 추출. (파일 풀 때 사용)
- -v : 처리되는 과정(파일 정보)을 자세하게 나열.
- -z : gzip 압축 적용 옵션.
- -j : bzip2 압축 적용 옵션.
- -t : tar 아카이브에 포함된 내용 확인.
- -C : 대상 디렉토리 경로 지정.
- -A : 지정된 파일을 tar 아카이브에 추가.
- -d : tar 아카이브와 파일 시스템 간 차이점 검색.
- -r : tar 아카이브의 마지막에 파일들 추가.
- -u : tar 아카이브의 마지막에 파일들 추가.
- -k : tar 아카이브 추출 시, 기존 파일 유지.
- -U : tar 아카이브 추출 전, 기존 파일 삭제.
- -w : 모든 진행 과정에 대해 확인 요청. (interactive)
- -e : 첫 번째 에러 발생 시 중지.

### tar 주요 사용법

```shell
# 대상 디렉토리를 포함한 모든 파일과 디렉토리를 tar로 묶기
tar cvf test.tar [PATH] 

# 파일을 지정하여 tar 아카이브로 묶기
tar cvf test.tar [FILE_1] [FILE_2] 

# tar 아카이브를 현재 디렉토리에 풀기
tar xvf test.tar 

# tar 아카이브를 지정된 디렉토리에 풀기
tar xvf test.tar -C [PATH] 

# tar 아카이브의 내용 확인하기
tar tvf test.tar 

# gzip으로 압축된 tar 아카이브를 현재 디렉토리에 풀기
tar zxvf test.tar.gz 

# bzip2로 압축된 tar 아카이브를 현재 디렉토리에 풀기
tar jxvf test.tar.bz2 

#현재 디렉토리를 tar로 묶고 gzip으로 압축하기
tar zcvf test.tar.gz * 

# 현재 디렉토리를 tar로 묶고 bzip2로 압축하기
tar jcvf test.tar.bz2 * 

# tar 아카이브 묶거나 풀 때 파일 별 진행 여부 확인하기
tar cvfw test.tar * 

# 현재 디렉토리의 모든 파일과 디렉토리를 tar로 묶기
tar cvf T.tar *
```

##  gzip 명령어 사용법 

리눅스에서 주로 파일을 압축하는 방식은 위에서 설명한 tar를 사용하여 여러 개의 파일을 하나로 묶고 이 묶은 tar 파일을 gzip 명령어를 사용하여. gz 형식으로 압축을 많이 합니다. gz은 gzip파일의 약자입니다. 만약 gzip 명령어를 찾을 수 없다고 나오면  apt-get install gzip 으로 설치하시면 됩니다.

### gz 압축하기

```shell
Copygzip [옵션][파일명]

# test.txt를 test.gz로 압축하기
gzip test.txt
```

### gz 압축해제

```shell
Copygzip -d [파일명]

# test.gz 압축해제
gzip -d test.gz 
```

### gzip 명령어 옵션

- -n : n은 1부터 9까지 숫자의 설정으로, 1이 가장 빠르지만 압축률은 가장 낮음
- -c : 압축된 파일 내용을 출력하고 원본파일은 그대로 보존
- -d : 압축 해제
- -f : 사용중인 파일도 강제로 압축
- -l : 압축 파일의 정보 출력
- -r : 지정한 디렉터리 안에 포함된 모든 파일을 압축하거나 해제합니다.
- -t : 압축 파일 테스트 (실제로 압축이 풀리지는 않음)
- -v : 압축 혹은 압축 해제를 할 때 자세한 정보 출력
- -h : 도움말 출력
- -V : 버전 정보 출력

##  zip / unzip 명령어 사용법 

윈도우에서 주로 사용하는 압축 형태인 zip 파일을 리눅스 서버로 옮겨서 작업하는 경우도 종종 있습니다. zip은 여러 파일을 묶고 압축할 수 있는 유틸리티로 tar와는 달리 아카이빙과 압축을 함께 할 수 있습니다. zip 명령어를 찾을 수 없다고 나오면  apt-get install zip 으로 설치하시면 됩니다.

### zip 압축하기

```shell
Copyzip [압축 파일명][압축할 파일명]

# mylog.log를 mylog.zip으로 압축하기(단일 파일 압축)
zip mylog.zip mylog.log 

# mylog1.log, mylog2.log, mylog3.log를 mylog.zip으로 압축하기(다중 파일 압축)
zip mylog.zip mylog1.log mylog2.log mylog3.log 

# 현 위치 디렉토리와 하위 디렉토리를 모두 test.zip으로 압축
zip -r test.zip ./* 
```

### zip 압축해제

```shell
Copyunzip [파일명]

# test.zip 압축 해제
unzip test.zip 
```

### zip 명령어 옵션

- -n : n은 1부터 9까지 숫자의 설정으로, 1이 가장 빠르지만 압축률은 가장 낮음
- -r : 하위 디렉터리까지 포함하여 압축
- -e : zip 파일에 암호 설정
- -x : 압축시 파일 제외
- -P : 압축 파일 생성 시 암호를 입력하여 생성
- -d : 지정된 위치에 압축 해제

###  unzip 명령어 옵션

- -a : 압축 해제 텍스트 파일을 기본적으로 자동 변환
- -L : 파일 이름을 대문자 시스템에서 소문자로 변환
- -C : 대소 문자를 구분하지 않고 이름을 일치시킴
- -o : 항상 파일을 덮어쓰기
- -n : 파일을 추출할 때 파일을 덮어쓰지 않음