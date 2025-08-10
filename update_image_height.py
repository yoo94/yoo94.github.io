#!/usr/bin/env python3
import os
import re
import glob

def update_image_height(file_path):
    """이미지의 height를 70%로 변경합니다"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # height:300px를 height:70%로 변경
        content = re.sub(
            r'height:300px;',
            r'height:70%;',
            content
        )
        
        # 내용이 변경되었을 때만 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            filename = os.path.basename(file_path)
            print(f"✅ {filename}: 이미지 height를 70%로 변경 완료")
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
    
    print(f"총 {len(md_files)}개 파일의 이미지 height 변경 시작...\n")
    
    success_count = 0
    for file_path in sorted(md_files):
        if update_image_height(file_path):
            success_count += 1
    
    print(f"\n처리 완료: {success_count}/{len(md_files)} 파일 수정됨")

if __name__ == "__main__":
    main()
