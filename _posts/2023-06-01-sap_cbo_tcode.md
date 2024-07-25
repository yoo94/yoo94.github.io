---
layout: post
title:  "sap CBO BDC T-CODE"
summary: "Enhancemnet"
author: yoo94
date: '2023-05-21 17:35:23 +0530'
category: sap
tags: sap
keywords: sap
thumbnail: https://i.namu.wiki/i/8714nM2OTlIubL44Exdh4QUXbuNUkGYZwJ2dc0kPkwtjBo85ZgCst0OmlfHM1kvsUNAx6rqjD4j1J7Plv1BgdA.svg
permalink: blog/sap_cbo_tcode/
---

### CBO
Enhancemnet라고 불리기도 하는데, SAP R/3의 표준기능, 테이블에 영향을 미치지 않는 상태에서 추가하고 기능을 개발하는 것을 말한다. 추가적인 Report의 개발은 일반적으로 CBO라고 표현하지 않는다.SAP가 표준으로 제공하고 있는 기능이나 프로세스가 회사의 실정에 비추어 부족하거나 부적합 하다고 판단이 되는 경우에는 일부기능을 개발하거나 표준 기능/프로세스를 변경하는 경우가 있다.

### BDC
Batch Data Communication 엑셀의 매크로 처럼 데이터를 form 이나 테이블 안에 다건, 단건 전송할 수 있는 기술

<img src="/blog/postImg/Pasted image 20240312130753.png" alt="Pasted image 20240312130753.png" style="max-width:100%;">

### TCODE
T 코드는 특정 작업을 실행할 때마다 사용되는 트랜잭션 코드다. SAP ERP의 각 기능에는 연관된 SAP 트랜잭션 코드가 있다.

결론적으로는 웹이나 다른 화면에서 데이터들을 작성하여 sap rfc를 호출하면서 데이터를 보내면
rfc가 단순 sap 에서 제공하는 것이면 BDC로 넘어가겠지만, 회사마다 custom을 할 수 있기 때문에 CBO를 호출하여 BDC에 맞게 데이터를 가공한다. 그다음 T-Code를 호출하여 해당 트랜잭션을 호출하고 그 안에 있는 BDC를 실행시켜 데이터를 넣고 해당 T-Code의 기능을 마무리 짓는다.
