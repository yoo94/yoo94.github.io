---
layout: post
title:  "빌드 도구들 Ant, Maven, Gradle"
summary: "빌드 도구들 Ant, Maven, Gradle"
author: yoo94
date: '2023-12-16 17:35:23 +0530'
category: webetc
tags: webetc
keywords: Ant, Maven, Gradle
thumbnail: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1UXT3Ous2UpkMSNSv6b20E5pnwqT2VvQ8aA&s
permalink: blog/ant_maven_gradle/
---
빌드도구는 소스코드에서 어플리케이션 생성을 자동화 하기 위한 프로그램이다. 빌드는 코드를 사용 or 실행 가능한 형태로 컴파일링, 링킹, 패키징 하는것을 포함한다.  
기본적으로 빌드 자동화는 아래와 같은 정형화된 다양한 작업을 스크립팅하거나 자동화 하는 행위이다.

Ant는 XML 기반의 스크립트를 사용하고 Maven은 XML 기반의 설정 파일을 사용한다.
그래서 Ant에서 스크립트로 메이븐을 실행 할 수 도있고, 젠킨스 역할을 할 수 있다.
### 1. Apache ANT

[**Ant**](http://ant.apache.org/)는 Java 기반의 빌드 도구로 다른 빌드 도구보다 역사가 오래되었다. Ant는 개발자가 원하는 것을 개발할 수 있다는 유연성에 큰 장점이 있다.   
**[ANT의 특징]**

- 각 프로젝트에 대한 XML기반 빌드 스크립트 개발
- 형식적인 규칙이 없음 : 결과물을 넣을 위치를 정확히 알려줘야 하며, 프로젝트에 특화된 Target과 Dependency를 이용해 모델링
- 절차적 : 명확한 빌드 절차 정의가 필요
- 생명주기를 갖지 않기 때문에 각각의 target에 대한 의존관계와 일련의 작업을 정의해 주어야 함

**[ANT의 단점]**

- 유연성이 높으나 프로젝트가 복잡해질 경우 각각의 Build과정을 이해하기 어려움
- XML, Remote Repository를 가져올 수 없었음 (IVY 도입)
- 스크립트의 재사용이 어려움

### 2. Apache Maven

[**Maven**](https://maven.apache.org/)은 프로젝트에 필요한 모든 'Dependency (종속성)'를 리스트의 형태로 Maven에게 알려 관리 할 수 있도록 돕는 방식을 말한다. 

- Dependency를 관리하고, 표준화된 프로젝트(Standardized project)를 제공
- XML, remote repository를 가져 올 수 있음 : 개발에 필요한 종속되는 'jar', 'class path'를 다운로드 할 필요 없이 선언만으로 사용 가능
- 상속형 : 하위 XML이 필요 없는 속성도 모두 표기

과 같은 기능을 한다. 즉, **'POM.xml'** 이라는 Maven 파일에 필요한 'Jar', 'Class Path'를 선언해 주면 직접 다운로드 할 필요 없이 Maven은 Repository에서 필요한 모든 파일들을 해당 프로젝트로 불러와 준다. 이러한 장점에도 불구하고, Maven은 몇가지 단점이 있는데 그것은 바로 아래와 같다.

- 라이브러리가 서로 종속할 경우 XML이 복잡해짐
- 계층적인 데이터를 표현하기에 좋지만, 플로우나 조건부 상황을 표현하기엔 어려움
- 편리하나 맞춤화된 로직 실행이 어려움

### 3. Apache Gradle

최근 소프트웨어개발 범위의 변화에 따라 빌드의 자동화에대한 요구도증가하게 되었다. **[Gradle](https://gradle.org/)**은 JVM 기반의 빌드 도구로 기존의 Ant와 Maven을 보완하였다. 따라서 JAVA 혹은 Groovy를 이용해 logic을 개발자의 의도에 따라 설계할 수 있다.

- 오픈소스기반의 build 자동화 시스템으로 Groovy 기반 DSL(Domain-Specific Language)로 작성
- Build-by-convention을 바탕으로함: 스크립트 규모가 작고 읽기 쉬움
- Multi 프로젝트의 빌드를 지원하기 위해 설계됨 
- 설정 주입 방식 (Configuration Injection)

따라서 초기 프로젝트 설정에 드는 시간을 절약할 수 있으며 기존의 Maven이나 Ivy등과 같은 빌드 도구들과도 호완이 가능하다는 점이다.  
