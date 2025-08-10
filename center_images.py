#!/usr/bin/env python3
import os
import re
import glob

def wrap_images_with_center_div(file_path):
    """마크다운 파일의 모든 이미지를 가운데 정렬 div로 감쌉니다"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. 이미 div로 감싸진 이미지 패턴 확인 (건드리지 않음)
        already_wrapped_pattern = r'<div[^>]*justify-content:\s*center[^>]*>[\s]*<img[^>]*>[\s]*</div>'
        
        # 2. 단독 HTML img 태그 찾기 (div로 감싸지지 않은 것)
        # 여러 줄에 걸쳐 있을 수 있는 img 태그 처리
        html_img_pattern = r'(<img[^>]*>)'
        
        def replace_html_img(match):
            img_tag = match.group(1)
            
            # 이미 div로 감싸져 있는지 확인 (앞뒤 컨텍스트 체크)
            start_pos = match.start()
            end_pos = match.end()
            
            # 앞쪽 100자, 뒤쪽 50자 정도 확인
            before_context = content[max(0, start_pos-100):start_pos]
            after_context = content[end_pos:min(len(content), end_pos+50)]
            
            # 이미 center div로 감싸져 있는지 확인
            if 'justify-content: center' in before_context and '</div>' in after_context:
                return img_tag  # 이미 감싸져 있으면 그대로 반환
            
            # 스타일 속성 추가 또는 수정
            if 'style=' in img_tag:
                # 기존 style 속성 수정
                if 'width:' not in img_tag and 'height:' not in img_tag:
                    img_tag = re.sub(r'style="([^"]*)"', r'style="\1; width:70%; height:300px;"', img_tag)
                elif 'width:' not in img_tag:
                    img_tag = re.sub(r'style="([^"]*)"', r'style="\1; width:70%;"', img_tag)
                elif 'height:' not in img_tag:
                    img_tag = re.sub(r'style="([^"]*)"', r'style="\1; height:300px;"', img_tag)
            else:
                # style 속성 추가
                img_tag = img_tag.replace('>', ' style="width:70%; height:300px;">')
            
            return f'<div style="display: flex; justify-content: center;">\n  {img_tag}\n</div>'
        
        # HTML img 태그 처리
        content = re.sub(html_img_pattern, replace_html_img, content, flags=re.DOTALL)
        
        # 3. 마크다운 이미지 패턴 처리 ![alt](src)
        markdown_img_pattern = r'(^|\n)(!\[[^\]]*\]\([^)]+\))(\s*$|\s*\n)'
        
        def replace_markdown_img(match):
            prefix = match.group(1)
            img_markdown = match.group(2)
            suffix = match.group(3)
            
            # 마크다운을 HTML로 변환
            alt_match = re.search(r'!\[([^\]]*)\]', img_markdown)
            src_match = re.search(r'\]\(([^)]+)\)', img_markdown)
            
            if alt_match and src_match:
                alt_text = alt_match.group(1)
                src_url = src_match.group(1)
                
                img_tag = f'<img src="{src_url}" alt="{alt_text}" style="width:70%; height:300px;">'
                
                return f'{prefix}<div style="display: flex; justify-content: center;">\n  {img_tag}\n</div>{suffix}'
            
            return match.group(0)  # 변환 실패시 원본 반환
        
        content = re.sub(markdown_img_pattern, replace_markdown_img, content, flags=re.MULTILINE)
        
        # 내용이 변경되었을 때만 파일 저장
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            filename = os.path.basename(file_path)
            print(f"✅ {filename}: 이미지 중앙 정렬 적용 완료")
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
    
    print(f"총 {len(md_files)}개 파일 처리 시작...\n")
    
    success_count = 0
    for file_path in sorted(md_files):
        if wrap_images_with_center_div(file_path):
            success_count += 1
    
    print(f"\n처리 완료: {success_count}/{len(md_files)} 파일 수정됨")

if __name__ == "__main__":
    main()
