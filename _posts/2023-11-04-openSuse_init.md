---
layout: post
title: "open Suse에 sap 세팅하기"
summary: "sap 세팅"
author: yoo94
date: "2023-11-03 17:35:23 +0530"
category: Backend_infra
tags:
- openSUSE
- 리눅스설치
- 네트워크설정
- SAP환경
- OS설정
- XFS파일시스템
- YaST2
- 서버구축
- 백엔드인프라
keywords: openSUSE, SAP 설치 환경, 리눅스 OS 설정, 네트워크 설정, YaST2, XFS 파일 시스템, ifconfig 대체, ip addr, DHCP 설정, 수동 IP 설정, 서버 구축, 방화벽 설정, USB 부팅, openSUSE Leap
thumbnail: https://blog.kakaocdn.net/dn/b4s4Dm/btsCc1tQAzr/hkkJvX7AcZUa3A1kzHZXWK/img.png
permalink: blog/opensusesapSetting/
---

![](https://blog.kakaocdn.net/dn/buI7WL/btsCgs7mJ6v/tvC1vZa76KETuKrkiqxKQ0/img.png)

**# OS** **기본 언어는 EN**

**# zypper install saptune**

**->**

SAPconf라는 것도 있고 SAPtune도 있는데 SAPconf 는 SAP 워크로드에 대해 시스템을 준비하기 위한 최소한의 tool이다. SAP 시스템을 사용하기 위해 OS Kernel 파라미터를 변경하는 도구라고 생각하면 된다.

부팅 시 sysctl 를 사용하여 동적으로 커널 매개변수를 SAP 시스템의 권장 값으로 설정한다.

SAPtune은 더 세분화된 tool이라고 생각하면 되겠다.

**# zypper install uuidd libuuid1**

-> uuidd libuuid1 이 패키지 버전이 동일하게

UUID란. 네트워크 상에서 고유성이 보장되는 id를 만들기 위한 표준 규약이다.

**# zypper install glibc**

=> glibc-2.31-150300.46.1 이상으로

libc는 "표준 C 라이브러리"를 말하는 대 명사이고

glibc는 GNU에서 만든 libc 이다.

기능이 궁금하다면 아래 링크를 확인 바란다!!

[https://www.gnu.org/software/libc/](https://www.gnu.org/software/libc/)

[

The GNU C Library - GNU Project - Free Software Foundation

The GNU C Library The project website can be found here: https://sourceware.org/glibc The GNU C Library - The project provides the core libraries for the GNU system and GNU/Linux systems, as well as many other systems that use Linux as the kernel. These li

www.gnu.org

](https://www.gnu.org/software/libc/)

**# zypper install libgcc_s1 libstdc++6 libatomic1**

-> 이건 그냥 s4hana를 위한 라이브러리라고 생각하자

Minimum versions are libgcc_s1-11.2.1, libstdc++6-11.2.1 and libatomic1-11.2.1, for example:

# rpm -q libgcc_s1 libstdc++6 libatomic1

libgcc_s1-11.2.1+git610-1.3.9.x86_64

libstdc++6-11.2.1+git610-1.3.9.x86_64

libatomic1-11.2.1+git610-1.3.9.x86_64

### **# 설치하다가 생긴 에러들**

zypper install saptune 을 하니까 repo-non-free (15.5) is invalid 하면서 에러가 났다... 15.5 는 참 별로인거같긴한데...

![](https://blog.kakaocdn.net/dn/xMkMe/btsCfBKzTIs/fdqqbfPvKk5fJ66qkTKhOK/img.png)

**일단 제일먼저 해볼게**

**zypper clean -all**

이걸 통해서 일단 레포지토리 다 정리해주고

**zypper ref**

이걸 통해서 다시 참조 해주면 된다고 공식문서에 나와있다. 근데 안됨 ㅡㅡ

![](https://blog.kakaocdn.net/dn/bZH9nN/btsCew3z2gZ/h23hmMRK2cWE4noNsFx9U0/img.png)

그래서

**zypper --gpg-auto-import-keys ref**

자동적으로 키를 임포트해서 신뢰하게 만드는 그런거다.

![](https://blog.kakaocdn.net/dn/c79b0L/btsClaYHSgY/IEORbmIuCx3RjaQjauAB7K/img.png)

짜란.. 다 됐다. 근데 이게 임시로 해결한거고

새로 고침 명령에 --gpg-auto-import-keys 옵션을 제공하더라도 zypper는 알 수 없는 키에 대해 경고를한다
