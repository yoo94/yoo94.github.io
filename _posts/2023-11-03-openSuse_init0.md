---
layout: post
title:  "open Suse에 설정 및 네트워크설정"
summary: "sap설치를 위한 os 설치"
author: yoo94
date: '2023-11-04 17:35:23 +0530'
category: openSuse
tags: openSuse
keywords: openSuse,sap
thumbnail: https://blog.kakaocdn.net/dn/b4s4Dm/btsCc1tQAzr/hkkJvX7AcZUa3A1kzHZXWK/img.png
permalink: /blog/opensuseOSsetting_network/
---


open suse 설치해서 해보고자 하였다 

[https://get.opensuse.org/ko/](https://get.opensuse.org/ko/)


![](https://blog.kakaocdn.net/dn/b4s4Dm/btsCc1tQAzr/hkkJvX7AcZUa3A1kzHZXWK/img.png)



먼저 다운로드부터 받고, 

openSUSE-Leap-15.5-DVD-s390x-Build491.1-Media 난 이것을 다운 받았다.



그 다음 USB 를 BOOT용으로 만들기 위해 프로그램 하나를 설치했다. 

rufus(루퍼스)는 안됐다.
universal usb installer이라는 것을 설치해서 구웠다.

![](https://blog.kakaocdn.net/dn/wwQ6O/btsB6OP5nwy/F4BENGOUTy5iC6r5dPO5Zk/img.webp)



![](https://blog.kakaocdn.net/dn/bobwZm/btsB6vXanO0/DxFyjqWdZC2fLrEWBgg0Rk/img.png)



![](https://blog.kakaocdn.net/dn/bo4OUm/btsB7dhFYpA/qrXY5FTbGArcQKroOdRz9K/img.png)


![](https://blog.kakaocdn.net/dn/Am0BS/btsCawOpVlz/gVZOAxHykk0r3c0Ryv72W1/img.png)



이제 제일 중요한 볼륨 파티셔닝. 제일 중요하다. **XFS 파일 시스템으로 파티션**



![](https://blog.kakaocdn.net/dn/Ovu3S/btsCbc97R4H/0H28kKnd9Ez2TquEBrQBU1/img.png)

![](https://blog.kakaocdn.net/dn/vV8D0/btsB5BXVE36/Fis3yuTED7qva6SazALT6K/img.png)

![](https://blog.kakaocdn.net/dn/Cy91U/btsB7UWBxTK/J2Stfrss3YmGkR9nbztpX0/img.png)



![](https://blog.kakaocdn.net/dn/rDdTt/btsB5VB82Th/bPHxjNS0llFmChwddqNZ71/img.png)

![](https://blog.kakaocdn.net/dn/92MKT/btsB5XtdkYs/exkdZLJK0kLc1Jjjzbi6H1/img.png)


시간도 서울로 맞춰주고

root 계정 만들어주고



![](https://blog.kakaocdn.net/dn/yG382/btsB4Q2bu52/LyX22ElFKbWx718nkkDQeK/img.png)



나는 어차피 우리회사 방화벽을 내가 설정하기 때문에,  ssh만 열었다. 

open SUSE를 설치하고 그냥 리눅스처럼 ipconfig를 갈겼는데,

바로 안된다. ..;;; 

![](https://blog.kakaocdn.net/dn/bmkn09/btsB6gsq8HQ/t8GaQxWcWYdzP2kZGY6gs0/img.png)



오픈 수세 15 버전 이상부터  **arp, route, netstat, iptunnel, ipmaddr, ifconfig 명령어가 안된단다.**

허허... 

  

아래있는 이미지에 나온것 처럼 그냥 바뀐거 쓰거나 뭐 패키지 설치하면 된다는데, 패키지 설치까지 뭐 귀찮고

바뀐거로 써보자

![](https://blog.kakaocdn.net/dn/dBDIpL/btsB7et7vfL/rAhxV7esdhsCIy5BZjKMMk/img.png)

ip addr 하면 이렇게 연결된 네트워크가 나온다. 

![](https://blog.kakaocdn.net/dn/bfb0rs/btsB7TwACRa/NCRmXK3ytvlkIE0RR9TqZk/img.png)



네트워크 설정은 GUI로 설치했으면 그냥 

YaST2 에 들어가서 Network  Devices -> Network Settings 에 들어가서 각자 네트워크에 맞게 설정하면 된다.

DHCP 자동할당을 해도 되지만 서버로 사용할 거라면 수동 설정을 하도록 하자

