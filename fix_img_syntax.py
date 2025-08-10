#!/usr/bin/env python3
import os
import re
import glob

def fix_img_tag_syntax(file_path):
    """img 태그의 문법 오류를 수정합니다"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # img 태그의 문법 오류 수정
        # width="50%" height="50%" / style="..." 를 style="width:70%; height:300px;" 로 수정
        content = re.sub(
            r'<img([^>]*?)width="[^"]*"\s*height="[^"]*"\s*/\s*style="width:70%; height:300px;">',
            r'<img\1style="width:70%; height:300px;">',
            content
        )
        
        # 중복된 스타일 속성 정리
        content = re.sub(
            r'<img([^>]*?)style="([^"]*?)"\s*style="([^"]*?)">',
            r'<img\1style="\3">',  # 두번째 style 속성 사용
            content
        )
        
        # 내용이 변경되었을 때만 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            filename = os.path.basename(file_path)
            print(f"✅ {filename}: img 태그 문법 수정 완료")
            return True
        else:
            filename = os.path.basename(file_path)
            print(f"⏭️  {filename}: 변경사항 없음")
            return False
            
    except Exception as e:
        print(f"❌ 오류 {file_path}: {e}")
        return False

def main():
    posts_dir = "/Users/yoojaeseok/src/yoo94.github.io/_posts"
    md_files = glob.glob(os.path.join(posts_dir, "*.md"))
    
    print(f"총 {len(md_files)}개 파일의 img 태그 문법 검사 시작...\n")
    
    success_count = 0
    for file_path in sorted(md_files):
        if fix_img_tag_syntax(file_path):
            success_count += 1
    
    print(f"\n처리 완료: {success_count}/{len(md_files)} 파일 수정됨")

if __name__ == "__main__":
    main()
