---
layout: post
title:  "리눅스 chmod"
summary: ""
author: yoo94
date: '2023-06-24 17:35:23 +0530'
category: linux
tags: linux
keywords: linux, tar, gz
thumbnail: https://i.namu.wiki/i/u3xN1dzCaWAEf6Tb5X0oSiVFU4DTQ_355FJmLCSTY7GZNyOnv60tkvcu0s0cD4Oce9vK6kylpAIEU-BYcju6Ww.webp
permalink: /blog/linux_chmod/
---


|       |     |     |       |     |     |       |     |     |
| ----- | --- | --- | ----- | --- | --- | ----- | --- | --- |
| Owner |     |     | Group |     |     | Other |     |     |
| r     | w   | x   | r     | w   | x   | r     | w   | x   |
| 4     | 2   | 1   | 4     | 2   | 1   | 4     | 2   | 1   |

여기서 r은 읽기(read), w는 쓰기(write), x 는 실행(execution) 의 의미입니다.

기존에 부여한 권한에서 권한을 빼거나 더할때는 문자로 지정하는게 편하고 전체를 새로 지정할 때는 숫자가 편합니다.

즉 _test.sh_ 란 파일이 있을 때 모두가 실행할수 있게 실행 속성을 추가할 경우 아래와 같이 문자로 지정하는게 편리합니다.

```bash
chmod +x test.sh
```

숫자로 권한을 부여할 경우 일부 권한만 추가할 수 없으므로 아래와 같이 지정합니다.

```bash
chmod 755 test.sh
```


ssh 정보를 담고 있는 홈 디렉터리의 .ssh 폴더에 대해 모두의 접근 권한을 해제할 경우는 숫자가 더 편리합니다.

```bash
chmod 700 ~/.ssh
```

문자로 권한을 부여할 경우 아래와 같이 해야 합니다.

```bash
chmod u+rwx,g=-rwx,o=-rwx ~/.ssh
```

### 소유자에게 파일 실행 권한 부여

```bash
chmod u+x file
```

```bash
chmod u+x file
```


### .ssh 폴더를 소유자만 접근 가능하게 설정

숫자로 권한 지정

```bash
chmod 700 ~/.ssh
```

+, - 로 권한 지정

```bash
chmod u+rwx,g-r-w-x,o=-r-w-x ~/.ssh
```

= 구문 사용

```bash
chmod u+rwx,g=,o=- ~/.ssh
```


### other 에 group 과 동일 권한 부여

```shell
chmod o=g file
```

### other 는 모든 권한 제거
```shell
chmod -R /varo= file
```

### 하위 파일/디렉터리 권한 지정

```shell
chmod -R 755 /var/www/myapp
```

#### chown와 chmod를 하위 파일과 폴더들에 한번에 적용하기
둘다 공통적으로 `-R` 옵션을 적용해주면 됩니다.
#### chmod의 경우

```shell
$ chmod -R [8bit permission] [file name or folder name]
```

예시

```shell
// example의 하위 폴더와 파일들에 권한을 666(-rw-rw-rw-)로 변경합니다.

$ chmod -R 666 example
```



#### chown의 경우

```shell
$ chown -R [owner name]:[group name] [filename or directory]
```

예시

```shell
// example의 하위 폴더와 파일들에 소유자를 sam으로 그룹을 abbey로 설정합니다.

$ chown -R sam:abbey example
```