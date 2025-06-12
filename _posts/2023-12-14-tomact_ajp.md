---
layout: post
title:  "아파치, 톰캣 AJP 통신하기"
summary: "아파치, 톰캣 AJP 통신하기"
author: yoo94
date: '2023-12-14 17:35:23 +0530'
category: webetc
tags: webetc
keywords: tomcat,apache,ajp
thumbnail: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1UXT3Ous2UpkMSNSv6b20E5pnwqT2VvQ8aA&s
permalink: blog/apche_ajp/
---
##### **아파치 -    톰캣 연동 동작 플로우**

1. 아파치 웹서버의 httpd.conf에 톰캣 연동을 위한 설정을 추가하고 톰캣에서 처리할 요청을 지정한다.

2. 사용자의 브라우저는 아파치 웹서버에 접속하여 요청한다. (통상 80 port )

3. 아파치 웹서버는 사용자의 요청이 들어왔을때, 이 요청이 톰캣에서 처리되도록 지정된 요청인지 확인한다.

4. 톰캣에서 처리해야하 하는 경우 아파치 웹서버는 톰캣의 AJP 포트(통상 8009 port) 에 접속해 요청을 톰캣에게 전달한다.   

5. 톰캣은 아파치 웹서버로부터 요청을 받아 처리한 후, 처리 결과를 다시 아파치 웹서버에게 돌려준다.

6. 아파치 웹 서버는 톰캣으로 전달받은 처리 결과를 사용자에게 전송한다.      


##### 설정해야 할 파일
|  |  |  |  |
| ---- | ---- | ---- | ---- |
|  | 파일명 | 위치 | 설명 |
| 1 | httpd.conf | {apache설치경로}/conf | apache 기본설정파일 |
| 2 | workers.properties | {apache설치경로}/conf | AJP Connector를 통해 서비스하는 Application server를 등록하는 설정파일 |
| 3 | mod_jk.conf | 다운 | Apache와 Tomcat의 연동을 위해 AJP Connector Module을 apache에 load하는 설정파일 |
| 4 | httpd-vhost.conf | {apache 설치경로}/conf/extra | 한개의 apache파일에 다수의 tomcat을 설정하기 위해 생성된 관리 파일 |
| 5 | server.xml | {tomcat설치경로}/conf | tomcat 기본설정파일 |
|  |  |  |  |
''
##### **아파치 - 톰캣 연동 순서**   

**1. 아파치, 톰캣 각각 설치**

**2. JK connector 설치**   

   - 아파치가 설치된 경로의 modules 디렉터리에 mod_jk 파일을 위치시킨다. http.conf의 mod_jk.so 위치와 일치해야함.

***mod_jk 모듈이란?**   

   AJP프로토콜을 사용하여 톰캣과 연동하기 위해 만들어진 모듈이다. mod_jk는 톰캣에서 배포되고 ,(톰캣 홈페이지에서 tomcat-connector 다운 ) 아파치 웹서버에 설치해주어야 한다.   

**3. 아파치 설정**

**1) workers.properties 파일 생성**

- workers.properties에 연동할 톰캣의 정보 (host, port, lbfactor (작업할당량) 등)   

```
worker.list=webmail, sysman, mobile  // 이름은 임의로 설정


worker.webmail.type=ajp13 
worker.webmail.host=localhost
worker.webmail.port=8009 //포트번호. 톰캣에서 설정한 포트와 일치해야함
worker.webmail.lbfactor=1 //서버밸런스 비율 


worker.sysman.type=ajp13
worker.sysman.host=localhost
worker.sysman.port=8019 // 포트중첩 불가. 

worker.mobile.type=ajp13
worker.mobile.host=localhost
worker.mobile.port=8019 // 포트중첩 불가. 
```

**2) 연동할 톰캣의 정보를 가진 properties파일은 생성 했으면 아파치가 실행할때 참조하는 httpd.conf파일에 이를 명시해주어야한다.**

**3) httpd.conf**

```
LoadModule jk_module /etc/apache2/modules/mod_jk.so
# mod_jk.so의 위치

JkWorkersFile /etc/apache2/conf/workers.properties
# workers 설정 파일 위치

JkLogFile /etc/apache2/logs/mod_jk.log
# 로그파일 위치

JkShmFile /etc/apache2/logs/mod_jk.shm
# Load balancing workers will not function properly 오류 대응, httpd의 권한


JkMount /*.jsp webmail
JkMount /*.do webmail
JkMount /sysman/* sysman
JkMount /mobile/* mobile
.
.

# URL에 따른 요청 처리 설정
```

*** JkMount:** 이 부분에서 어떤 URL로 오는 경우, 어떤 worker(톰캣)가 처리할 지 결정할지 설정한다.

JkMount 뒤에 오는 /* 는 모든 url의 요청을 의미한다.

즉, 모든 url의 요청에서 서블릿 관련처리가 필요하다면, workers.properties파일에 명시된 worker(WAS)에게로 넘기겠다.

라는 의미가 된다.   

톰캣이 여러대인경우    workers.list의 각 worker이름(webmail,sysman,mobile)에 따라서 설정한다.   

**4. 톰캣 설정 - server.xml**   

    **1) 기존의 HTTP 커넥터(8080port) 제거 (주석처리)**   

            -아파치를 통해 :80 가상 포트로 접속하기 때문에, 톰캣으로 직접 접속하는 :8080 포트는 사용을 막는다.

```
<!--
<Connector URIEncoding="UTF-8" connectiontimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443" server=" " maxPostZize="1-"/>
-->
```

**2) AJP 커넥터 설정 (주석 해제)**      

```
<!-- Define an AJP 1.3 Connector on port 8009 -->
<Connector port="8009" protocol="AJP/1.3" redirectPort="8443" address="localhost"/>
```

이 ajp커넥터에 등록한 정보와 아파치 workers.properties의 정보가 일치해야 통신이 가능하다.

#####    ***AJP란?   Apache JServ Protocol**   

웹서버 뒤에 있는 와스로 부터 웹서버에서 받은 요청을 와스로 전달해주는 프로토콜이다.   

아파치와 톰캣을 연동하기 위해서는    AJP를 통해 서로 통신을 한다.

아파치는 이를 사용하여 80포트로 들어오는 요청은 자신이 받고, 이 요청중 서블릿을 필요로 하는 요청은 톰캣에게 전달하여 처리한다. (httpd.conf 의 JkMount설정 )

해당 프로토콜(ajp)는 다양한 WAS에서 지원한다. ex) 아파치, 톰캣, 제우스, 웹로직, 웹스피어 등...   

**5. 아파치, 톰캣 모두 설정 완료 후, 각각 재기동.**   

**6. 아파치 80 접속 확인**   

   - 8080 포트 없이 접속되는지 확인한다.   

   - 연동 전에는 포트 번호를 붙여야 하지만, 이후에는 포트 번호 없이 접속이 가능하다.   
