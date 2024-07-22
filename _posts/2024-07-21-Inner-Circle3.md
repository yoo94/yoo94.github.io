---
layout: post
title:  "나의 이직 일기 - 패스트 캠퍼스 inner circle 첫 수업"
summary: "holiday"
author: yoo94
date: '2024-07-21 20:35:23 +0530'
category: ['change-jobs-diary']
tags:
- inner-circle
- fast campus
- developer
- inner circle
- 패스트 캠퍼스
- 이너서클
- ZEP
thumbnail: https://cdn.day1company.io/prod/uploads/202406/134545-1416/simbol-black.png
permalink: /blog/InnerCircle02/
---
# 대망의 첫수업

첫수업은 간단하게 노드어플리케이션을 만들라는 것이였다.

아 근데 내 노트북... github 키체인이 걸려있어서 뭔가 제대로 작동을 안했고..

pullRequest도 제대로 안돼서... 한시간 반을 날렸다...ㅜㅜ 죄송합니다...리더님..

<img src="/blog/postImg/img_7.png" width="50%" height="50%" />

## 조언들 종합

좀 더 깔끔하고 친절한 설명, 가독성 있는 변수명, 함수명 등이 기본이다.

방법이 중요하다기 보다는, 왜 그랬느냐가 중요하다. 합당한 이유 효율적인 이유가 필요하다.

```javascript
const baseUrl = 'https://date.nager.at/api/v3/';
const publicHolidaysUrl = `${baseUrl}PublicHolidays`;
const nextPublicHolidaysUrl = `${baseUrl}NextPublicHolidays`;
const availableCountriesUrl = `${baseUrl}AvailableCountries`;

async function getHoliday() {
    const args = process.argv.slice(2);

    if (args.length !== 2) {
        console.error('필요인수: 국가코드 연도_또는_next');
        return;
    }

    const [countryCode, yearOrNext] = args;

    if (!await isValidCountryCode(countryCode)) {
        console.error('Wrong country code');
        return;
    }
    if (yearOrNext.toLowerCase() !== 'next' && !/^\d{4}$/.test(yearOrNext)) {
        console.error('유효하지 않은 연도입니다.');
        return;
    }

    let url;
    if (yearOrNext.toLowerCase() === 'next') {
        url = `${nextPublicHolidaysUrl}/${countryCode}`;
    } else {
        url = `${publicHolidaysUrl}/${yearOrNext}/${countryCode}`;
    }

    try {
        const holidayData = await fetchHolidayData(url);
        if (holidayData) {
            holidayData.forEach(data => {
                console.log(`${data.date} ${data.name} ${data.localName}`);
            });
        }
    } catch (error) {
        console.error('Error data:', error);
    }
}
async function isValidCountryCode(countryCode) {
    try {
        const response = await fetch(availableCountriesUrl);
        if (!response.ok) {
            console.error(`api fetch 오류 상태 코드: ${response.status}`)
            return false;
        }
        const countries = await response.json();
        return countries.find(function(country) {
            return country.countryCode.toLowerCase() === countryCode.toLowerCase();
        });
    } catch (error) {
        console.error(error.message)
        return false;
    }
}
async function fetchHolidayData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            console.error(`api fetch 오류 상태 코드: ${response.status}`)
            return false;
        }
        return await response.json();
    } catch (error) {
        console.error('Error data:', error);
    }
}

getHoliday();

```
<img src="/blog/postImg/img_8.png" width="50%" height="50%" />

