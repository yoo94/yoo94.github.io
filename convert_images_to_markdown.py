#!/usr/bin/env python3
"""
HTML 이미지 태그를 Markdown 형식으로 변환하는 스크립트
<div style="display: flex; justify-content: center;">
  <img src="/path/image.png" alt="alt text" style="...">
</div>
형태를 ![alt text](/path/image.png) 형태로 변환합니다.
"""

import os
import re
import glob

def convert_html_img_to_markdown(content):
    """HTML 이미지 태그를 Markdown 형식으로 변환"""
    
    # 패턴 1: div로 감싸진 img 태그
    pattern1 = r'<div[^>]*>\s*<img\s+src="([^"]+)"\s+alt="([^"]*)"\s+[^>]*>\s*</div>'
    
    def replace_func1(match):
        src = match.group(1)
        alt = match.group(2)
        # alt 텍스트가 파일명과 같으면 더 간단한 설명으로 변경
        if alt.startswith("Pasted image"):
            alt = "이미지"
        return f'![{alt}]({src})'
    
    # 첫 번째 패턴 적용
    content = re.sub(pattern1, replace_func1, content, flags=re.MULTILINE | re.DOTALL)
    
    # 패턴 2: 여러 줄에 걸친 div + img 조합
    pattern2 = r'<div[^>]*style="[^"]*display:\s*flex[^"]*justify-content:\s*center[^"]*"[^>]*>\s*<img\s+src="([^"]+)"\s+alt="([^"]*)"\s+[^>]*>\s*</div>'
    
    def replace_func2(match):
        src = match.group(1)
        alt = match.group(2)
        if alt.startswith("Pasted image"):
            alt = "이미지"
        return f'![{alt}]({src})'
    
    # 두 번째 패턴 적용
    content = re.sub(pattern2, replace_func2, content, flags=re.MULTILINE | re.DOTALL)
    
    # 패턴 3: 더 관대한 패턴 (줄바꿈 포함)
    pattern3 = r'<div[^>]*>\s*\n?\s*<img[^>]+src="([^"]+)"[^>]+alt="([^"]*)"[^>]*>\s*\n?\s*</div>'
    
    def replace_func3(match):
        src = match.group(1)
        alt = match.group(2)
        if alt.startswith("Pasted image"):
            alt = "이미지"
        return f'![{alt}]({src})'
    
    # 세 번째 패턴 적용
    content = re.sub(pattern3, replace_func3, content, flags=re.MULTILINE | re.DOTALL)
    
    return content

def process_markdown_files():
    """_posts 디렉토리의 모든 .md 파일 처리"""
    
    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        print(f"'{posts_dir}' 디렉토리가 존재하지 않습니다.")
        return
    
    # 모든 .md 파일 찾기
    md_files = glob.glob(os.path.join(posts_dir, "*.md"))
    
    if not md_files:
        print("처리할 .md 파일이 없습니다.")
        return
    
    processed_files = []
    
    for file_path in md_files:
        try:
            # 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # 변환 적용
            converted_content = convert_html_img_to_markdown(original_content)
            
            # 변경사항이 있는지 확인
            if original_content != converted_content:
                # 백업 파일 생성
                backup_path = file_path + '.backup'
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
                
                # 변환된 내용으로 파일 업데이트
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(converted_content)
                
                processed_files.append(file_path)
                print(f"✅ 변환 완료: {file_path}")
                print(f"   백업 파일: {backup_path}")
            else:
                print(f"⏭️  변경사항 없음: {file_path}")
                
        except Exception as e:
            print(f"❌ 오류 발생 ({file_path}): {e}")
    
    print(f"\n🎉 처리 완료!")
    print(f"   전체 파일: {len(md_files)}개")
    print(f"   변환된 파일: {len(processed_files)}개")
    
    if processed_files:
        print(f"\n변환된 파일 목록:")
        for file_path in processed_files:
            print(f"  - {file_path}")
        
        print(f"\n⚠️  주의사항:")
        print(f"  - 각 파일의 .backup 파일이 생성되었습니다.")
        print(f"  - 변환 결과를 확인 후 문제가 없으면 .backup 파일을 삭제하세요.")
        print(f"  - 문제가 있다면 .backup 파일로 복구할 수 있습니다.")

def test_conversion():
    """변환 테스트 함수"""
    test_html = '''
<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/test.png" alt="테스트 이미지" style="width:auto; height:auto;">
</div>

<div style="display: flex; justify-content: center;">
  <img src="/blog/postImg/Pasted image 20240119135605.png" alt="Pasted image 20240119135605.png" style="max-width:auto;; height:auto;">
</div>
    '''
    
    result = convert_html_img_to_markdown(test_html)
    print("테스트 변환 결과:")
    print("=" * 50)
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    print("🚀 HTML 이미지 태그 → Markdown 변환기")
    print("=" * 50)
    
    # 테스트 실행 여부 확인
    test_mode = input("테스트 모드로 실행하시겠습니까? (y/N): ").lower().strip()
    
    if test_mode == 'y':
        test_conversion()
    else:
        confirm = input("모든 .md 파일을 변환하시겠습니까? (y/N): ").lower().strip()
        if confirm == 'y':
            process_markdown_files()
        else:
            print("작업이 취소되었습니다.")
