---
layout: post 
title:  "next kakao Developers 세팅 및 지도 불러오기"
summary: "next 에서 지도를 가져오자"
author: yoo94 
date: '2024-09-08 11:35:23 +0530' 
category: ['nextJs','react']
tags: react,nextJs
permalink: blog/next-kakao-Developers/
---

## Kakao Developers 세팅

1. 카카오 디벨로퍼 사이트 접속 후 앱 생성: https://developers.kakao.com/

2. 애플리케이션 생성 후, "앱 키" 섹션의 JavaScript 키 복사

3. 환경 변수에 NEXT_PUBLIC_KAKAO_MAP_CLIENT로 해당 키 저장 / 플랫폼 > Web에 로컬 호스트 추가: http://localhost:3000

4. 카카오 지도 API 사이트에서 > Web 선택: https://apis.map.kakao.com/web/관련 도큐먼트를 확인하며 카카오 지도 불러오기


## Kakao Map API로 지도 불러오기

1. 카카오 지도 API 가이드: https://apis.map.kakao.com/web/guide/

2. 지도 담을 영역 만들기 (<div id="map"></div>)

3. Javascript API로 지도 불러오기

4. Next/Script를 사용해 스크립트 동적 로드를 위해서 카카오 맵의 load 메서드 
사용하기: https://apis.map.kakao.com/web/documentation/#load
**Kakao 객체 정리가 안되었다는 eslint 에러 해결을 위해 상단에 /* global kakao */ 입력

5. 지도 스크립트의 로딩 및 초기화 후 페이지의 상호 작업 가능한 상태와 동기화하고, 
페이지 성능을 최적화하기 위해 Next/Script의 afterInteractive strategy와 onReady 사용

Kakao Map API로 지도 불러오기 (코드 예시)


```tsx
// 객체정의
/** global kakao */
import Layout from '@components/Layout';
import Script from 'next/script';

// window 객체에 kakao 프로퍼티 추가 선언(TS)
declare global {
  interface Window {
    kakao: any;
  }
}

export default function Home() {
  const loadKakaoMap = () => {
      //카카오 지도 로드 함수
    window.kakao.maps.load(() => {
      const mapContainer = document.getElementById('map');
      const mapOption = {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
      };
      new window.kakao.maps.Map(mapContainer, mapOption);
    });
  };

  return (
      //nextjs Script 태그로 카카오 지도 로드하기
    <Layout>
      <Script
        strategy="afterInteractive"
        type="text/javascript"
        src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={process.env.NEXT_PUBLIC_KAKAO_MAP_CLIENT}&autoload=false"
        onReady={loadKakaoMap}
      />
      <div id="map" className="w-full h-screen"></div>
    </Layout>
  );
}


```

## 마커 구현

#### 카카오 지도 마커 가이드: https://apis.map.kakao.com/web/sample/basicMarker/

```js
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도 중심좌표
        level: 3 // 지도의 확대 수준
    };

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 마커가 표시될 위치입니다
var markerPosition = new kakao.maps.LatLng(33.450701, 126.570667);

// 마커 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);

// 아래 코드는 지도 위에 마커를 제거하는 코드입니다
// marker.setMap(null);
```


## 커스텀 마커

#### 이미지 마커 생성 가이드: https://apis.map.kakao.com/web/sample/basicMarkerImage/
```js
var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.546539, 126.985006), // 지도의 중심좌표
        level: 4 // 지도의 확대 수준
    };

// 지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 이미지 마커의 주소입니다
var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png',  // 마커이미지 주소
    imageSize = new kakao.maps.Size(64, 69),  // 마커 이미지의 크기
    imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커의 좌표의 원시값, 이미지 안에서 좌표를 설정합니다.

// 마커가 표시될 위치입니다
var markerPosition = new kakao.maps.LatLng(37.546939, 126.995998);

// 마커 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition,
    image: new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption)
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);

```

## Kakao Map 마커 인포윈도우 구현

커스텀 오버레이 생성하기: https://apis.map.kakao.com/web/sample/customOverlay1/
마커에 마우스 이벤트 등록하기: https://apis.map.kakao.com/web/sample/addMarkerMouseEvent/

```js
// 마커에 커스텀 오버레이를 추가할 때 인포윈도우를 생성합니다
var iwContent = '<div style="padding:5px;">Hello World!</div>';

// 인포윈도우를 생성합니다
var infowindow = new kakao.maps.InfoWindow({
    content: iwContent
});

// 마커에 마우스 이벤트를 등록합니다
kakao.maps.event.addListener(marker, 'mouseover', function () {
    // 마커에 마우스를 올렸을 때 발생하는 인포윈도우를 마커위에 표시합니다.
    infowindow.open(map, marker);
});

// 마커에 마우스 이벤트를 등록합니다
kakao.maps.event.addListener(marker, 'mouseout', function () {
    // 마커에 마우스를 뗐을 때 인포윈도우를 제거합니다.
    infowindow.close();
});

```