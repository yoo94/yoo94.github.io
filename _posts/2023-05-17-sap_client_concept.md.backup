---
layout: post
title:  "Client Concept"
summary: "SAP 시스템에서 지칭하는 조직적으로 최상위 독립 단위"
author: yoo94
date: '2023-05-21 17:35:23 +0530'
category: TechMisc
tags: sap
keywords: sap
thumbnail: https://i.namu.wiki/i/8714nM2OTlIubL44Exdh4QUXbuNUkGYZwJ2dc0kPkwtjBo85ZgCst0OmlfHM1kvsUNAx6rqjD4j1J7Plv1BgdA.svg
permalink: blog/sap_client_concept/
---
### **Client**   

- **SAP 시스템에서 지칭하는 조직적으로 최상위 독립 단위**
- **데이터베이스에서 데이터가 나누어지는 최상위 단위**

다시 말해 Client 하나는 하나의 SAP system 환경을 말하며, Client 마다 서로 다른 SAP system 환경을 구축할 수 있다. 
SAP 서버에 접속 후 로그인 화면을 보면 상단에 클라이언트를 입력하게 되어 있다.

그 말은 **하나의 물리적 서버에는 여러 클라이언트가 존재** 할 수 있으며

그 중 하나를 선택해서 접속할 수 있음을 알 수 있다. 

### 서버가 하나의 물리적 단위라 하면 하나의 서버 내에서 논리적으로 나누어지는 단위가 클라이언트이다.

일반적으로 하나의 개발 서버에는 개발자가 개발할 수 있는 개발 전용 Client 와

컨설턴트가 Configuration 작업을 할 수 있는 IMG 전용 Client를 분리하여 생성한다.
IMG Client 는 반드시 Configuration Data만 존재해야 하며 Application Data는 발생시키면 안된다. 

그 이유는 IMG Client가 SAP 세팅이 완료되는 하나의 메인 Client 이며 향후 품질/운영서버로 Client Copy(이관) 가 되는 주 Client이기 때문이다.

## Client Dependent  - DATA 

해당 클라이언트에서 발생한 데이터들은 그 클라이언트에서만 관리되어 지며 다른 클라이언트에서는 보이지 않는다. 

즉, 데이터들은 클라이언트에 종속적으로 존재하며 다른 클라이언트 간에 서로 공유되지는  않는다.
이것을 **Client Dependent** 속성이라 하고 다른 말로는 **Client-Specific** 이라고도 한다. 

SAP에서 관리되는 데이터들은 대부분 Client-Dependent 속성을 가지고 있으며,

다음과 같이 3가지로 분류된다.

#### Application Data
End-User가 SAP를 사용하면서 발생하는 실 데이터 
1) **Master Data** : 각 모듈 별 주요 기준이 되는 데이터   ( ex> 자재정보, 단가정보, 고객정보, 공급업체정보 등... )  
2) **Transaction Data** : 물류와 회계 등 실제 업무의 흐름으로 발생한 데이터  ( ex> 회계전표, 물류전표, 판매오더 등... )|


#### configuration Data
SAP system Customizing시 세팅한 데이터   _( 예외적으로 Client Indepedent 데이터도 존재 )_|
#### User Master Data
SAP 사용자에 대한 정보 데이터

_( *Customizing : SAP System을 구축되는 회사의 업종( 자동차, 철강, 화학, 유통 등..) 과 프로세스에 맞게 End-User(현업)이 사용할 수 있도록 시스템을 변경하는 작업 )_


## Client Independent - Repository Object   

200번 Client에서 작업한 Configuration 데이터들은 Client Dependent 속성이므로

300번 Client에서는 존재하지 않을 것이다. 반면에 300번 Client에서 개발한 프로그램은

데이터와는 다르게 200번 Client에서는 보이게 된다. 


**Repository Object **( 개발 Object )****    
  - Program, Function, Class, Table, View 등...  
    
  **일부 Configuration Data**   
  - 국가코드, 통화키 등...

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240202133919.png" alt="Pasted image 20240202133919.png" style="max-width:auto;; height:auto;">
</div>
