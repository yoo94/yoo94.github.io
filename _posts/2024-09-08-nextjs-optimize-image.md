---
layout: post 
title:  "next optimize image"
summary: "next 이미지 최적화"
author: yoo94 
date: '2024-09-08 14:35:23 +0530' 
category: ['nextJs','react']
tags: react,nextJs
permalink: blog/next-optimize-image/
---

### Next.js Image 컴포넌트란?

Next.js에서는 이미지를 효율적으로 처리하고 최적화하기 위한 Image 컴포넌트를 제공
이미지를 최적화하여 페이지 로딩 속도를 개선하고, 사용자 경험을 향상시킬 수 있음

```js
import Image from 'next/image';

<Image
  src="/path/to/image.jpg"
  alt="이미지 설명"
  width={500}
  height={300}
/>
```

| 속성명 (prop)   | 설명 및 예시                                                |
|-----------------|--------------------------------------------------------|
| `src`           | 표시할 이미지 파일 경로 또는 URL (예: `src="/profile.png"`)         |
| `width`         | 이미지 너비 지정 (예: `width={500}`)                           |
| `height`        | 이미지 높이 지정 (예: `height={500}`)                          |
| `alt`           | 이미지 대체 텍스트 설정 (예: `alt="Picture of the author"`)       |
| `loader`        | 이미지 로딩 방식을 지정하는 함수 (예: `loader={imageLoader}`)         |
| `fill`          | 이미지를 자동으로 필드에 맞게 채울지(예: `fill={true}`)                 |
| `sizes`         | 반응형 이미지의 크기 조절 (예: `sizes="(max-width: 768px) 100vw"`) |
| `quality`       | 이미지 품질을 설정 (1-100까지의 정수, 예: `quality={80}`)            |

| 속성명 (prop)      | 설명 및 예시                                                       |
|-------------------|------------------------------------------------------------------|
| `priority`        | 이미지 로딩 우선순위 설정 (예: `priority={true}`)                   |
| `placeholder`     | 이미지 로딩 중에 표시할 미리보기 이미지 설정 (예: `placeholder="blur"`) |
| `styles`          | 커스텀 CSS 스타일을 지정하여 이미지에 스타일링 적용 (예: `style={{objectFit: "contain"}}`) |
| `onLoadingComplete`| 이미지 로딩이 완료된 후 호출되는 콜백 함수 설정 (예: `onLoadingComplete={img => done()}`) |
| `onLoad`          | 이미지 로딩이 시작될 때 호출될 콜백 함수 설정 (예: `onLoad={event => done()}`) |
| `onError`         | 이미지 로딩 중 오류 발생 시 호출되는 콜백 함수 설정 (예: `onError={event => fail()}`) |
| `loading`         | 이미지 로딩 전략 설정 (eager / lazy) (예: `loading="lazy"`)       |
| `blurDataURL`     | 이미지 로딩 중 미리보기 이미지로 사용할 데이터 URI 설정 (예: `blurDataURL="data:image/jpeg..."`) |


#### Next/Image 컴포넌트 특징

- 이미지 최적화: 이미지를 자동으로 최적화하고, 필요한 크기로 조정함
- 이미지 포맷: WebP, JPEG, PNG 등 다양한 이미지 포맷 지원.
- 브라우저의 지원 여부에 따라 최상의 포맷 자동 선택
- 반응형 이미지: next/image를 사용하면 반응형 이미지 쉽게 생성 가능. 다양한 크기의 이미지를 제공하며 브라우저 창 크기에 따라 적절한 크기 이미지 자동 선택

##### 레이아웃 속성: next/image의 layout 속성을 사용해서 이미지의 레이아웃 제어 가능 (layout="fixed")

- intrinsic: (기본값) 이미지의 원본 크기를 유지하면서 조정
- fixed: 지정된 너비와 높이로 이미지가 고정
- responsive: 반응형 이미지로, 가로 비율을 유지하면서 너비만 지정
- 미리보기 이미지: 이미지 로딩 전, 미리보기 이미지를 생성하여 페이지 레이아웃이 변경되지 않고 사용자 경험을 향상

- Lazy loading: next/image 모듈은 레이지 로딩을 자동으로 지원, 화면에 나타날 때 이미지를 로드

따라서, 페이지 초기 로딩 성능을 향상시키고 대역폭을 절약

- 효율적인 캐싱: 이미지를 효율적으로 캐싱하여 이미지 로딩을 최적화
- 테마 감지: 테마(다크 모드 또는 라이트 모드)에 따라 이미지를 동적으로 선택할 수 있음
- 애니메이션 이미지: GIF와 같은 애니메이션 이미지를 지원함
- 기본적으로 이미지를 자동으로 최적화하고, 로딩할 때 애니메이션 유지

```css
.imgDark {
  display: none;
}

@media (prefers-color-scheme: dark) {
  .imgLight {
    display: none;
  }
  .imgDark {
    display: unset;
  }
}
```
```js
import styles from './theme-image.module.css'
import Image from 'next/image'

const ThemeImage = (props) => {
  const { srcLight, srcDark, ...rest } = props;

  return (
    <>
      <Image {...rest} src={srcLight} className={styles.imgLight} />
      <Image {...rest} src={srcDark} className={styles.imgDark} />
    </>
  );
}
```

## Image 라는 컴포넌트를 사용하면 거의 대부분 최적화를 해준다 
 참고로 외부에서 불러오는 이미지에대한 안전성을 부여하려면
next.config.mjs에서
images:{
    domains:["도메인""]
}
을 넣어주면 된다.

