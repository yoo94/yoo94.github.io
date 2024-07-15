---
layout: post
title:  "js, java 파일 압축해서 zip 다운 받기"
summary: "zip 다운"
author: yoo94
date: '2024-07-09 12:35:23 +0530'
category: ['inner circle']
tags: webpack
thumbnail: https://cdn.day1company.io/prod/uploads/202406/134545-1416/simbol-black.png
permalink: /blog/InnerCircle01/
---
# 클라이언트

```javascript
window.$file = {}
$file.getFileAllDownload = function () {
            var fileList = [];
            $('.file-item').each(function() {
                var fileData = $(this).data(); // 현재 요소의 데이터를 가져옴
                fileList.push(fileData); // 배열에 추가
            });

            fetch('/file/allDownload.do', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(fileList)
            })
                .then(response => response.blob())
                .then(blob => {
                    // 클라이언트에서 파일 다운로드 링크 생성
                    var url = window.URL.createObjectURL(blob);
                    var a = document.createElement('a');
                    a.href = url;
                    a.download = 'files.zip';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                })
                .catch(error => {
                    console.error('Fetch 오류:', error);
                });
        };
```
먼저 클라이언트에서 호출한다.
- contentType: 'application/json': 서버로 보내는 요청 데이터의 타입을 지정
- responseType: 'blob': 서버로부터 어떤 타입의 데이터를 받을지 : (Binary Large Object)을 반환받기

1. var blob = new Blob([Uint8Array.from(response, a => a.charCodeAt(0))], {type: "application/zip"});
서버 응답  바이너리 데이터를 Uint8Array로 변환하여 Blob 객체를 생성
2. a.download = 'files.zip';   다운로드되는 파일의 이름을 'files.zip'으로 지정
3. document.body.appendChild(a);  앵커 요소를 문서의 <body>에 추가
4. a.click();   DOM에 추가되어야 클릭 이벤트를 사용
5. 사용한 객체는 제거


나같은 경우는 회사에 fileData들을 가져오는 api가 있기 때문에 그 부분은 생략했다.
```java
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;
    @RequestMapping("/file/allDownload")
	public void download(@RequestBody List<Map<String, String>> fileList, HttpServletResponse response, HttpServletRequest request) throws IOException {
		response.setContentType("application/zip");
		response.setHeader("Content-Disposition", "attachment; filename=\"files.zip\"");
		try (ByteArrayOutputStream baos = new ByteArrayOutputStream();
			 ZipOutputStream zos = new ZipOutputStream(baos)) {
			for (Map<String, String> fileMap : fileList) {
				String fileName = fileMap.get("FILE_NAME");
				ImportParam importParam = new ImportParam(fileMap);
				String path = 여기서 다운로드 받을 파일들의 경로를 써줍니다.
				try (InputStream inputStream = NasFileUtil.getNasFileAsInputStream(path)) {
					zos.putNextEntry(new ZipEntry(fileName));
					IOUtils.copy(inputStream, zos);
					zos.closeEntry();
				}
			}
			zos.finish();
			zos.flush();
			// Write the zip file bytes to the response output stream
			response.getOutputStream().write(baos.toByteArray());
			response.getOutputStream().flush();
		}
	}
```
