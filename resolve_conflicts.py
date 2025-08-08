#!/usr/bin/env python3
import os
import re
import glob

def resolve_conflict_in_file(file_path):
    """충돌이 있는 파일에서 우리의 카테고리 변경을 유지하면서 충돌 해결"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 충돌 마커가 있는지 확인
        if '<<<<<<< HEAD' not in content:
            return False
        
        # 충돌 해결: 우리의 카테고리를 유지하고 원격의 date 형식 사용
        # date 형식 통일 (작은따옴표 -> 큰따옴표)
        resolved_content = re.sub(
            r"<<<<<<< HEAD\ndate: '([^']+)'\ncategory: ([^\n]+)\n=======\ndate: \"([^\"]+)\"\ncategory: ([^\n]+)\n>>>>>>> [^\n]+",
            r'date: "\3"\ncategory: \4',
            content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        # 더 복잡한 충돌 패턴도 처리
        resolved_content = re.sub(
            r"<<<<<<< HEAD\n([^=]+)\n=======\n([^>]+)\n>>>>>>> [^\n]+",
            r'\2',  # 우리 버전(아래쪽) 사용
            resolved_content,
            flags=re.MULTILINE | re.DOTALL
        )
        
        if resolved_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(resolved_content)
            print(f"✅ 충돌 해결: {os.path.basename(file_path)}")
            return True
        
    except Exception as e:
        print(f"❌ 오류 {file_path}: {e}")
    
    return False

def main():
    # 충돌이 있는 파일들
    conflict_files = [
        "_posts/2024-06-15-myconfused-curring.md",
        "_posts/2024-06-26-myconfused-react-Styled-Component.md", 
        "_posts/2024-07-02-myconfused-reflow-repaint.md",
        "_posts/2024-07-05-webpack2.md",
        "_posts/2024-07-09-javaScript-zipFile.md",
        "_posts/2024-08-20-myconfused-react-recoil.md",
        "_posts/2024-08-23-nextJs-data-fetching.md",
        "_posts/2024-08-25-nextJs-csr-ssr-ssg.md",
        "_posts/2024-11-21-next-auth3.md",
        "_posts/2025-02-20-re-react3.md"
    ]
    
    for file_path in conflict_files:
        full_path = f"/Users/yoojaeseok/src/yoo94.github.io/{file_path}"
        resolve_conflict_in_file(full_path)

if __name__ == "__main__":
    main()
