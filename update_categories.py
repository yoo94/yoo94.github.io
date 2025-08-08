#!/usr/bin/env python3
import os
import re
import glob

def determine_new_category(old_categories, filename, content_preview=""):
    """기존 카테고리와 파일명을 기준으로 새로운 카테고리를 결정"""
    
    # DevLog 카테고리
    devlog_keywords = ['myconfused', 'planning', 'inner-Circle', 'inner-circle']
    
    # Backend_infra 카테고리
    backend_keywords = ['nodejs', 'docker', 'network', 'linux', 'openSuse']
    
    # WebSecurity 카테고리
    security_keywords = ['websecurity', 'account', 'WebSecurity']
    
    # TechMisc 카테고리
    misc_keywords = ['sap', 'webetc']
    
    # Frontend 관련 키워드들 (난이도별 분류)
    frontend_basic = ['html', 'css', 'javaScript', 'javascript', 'typeScript', 'typescript']
    frontend_intermediate = ['react', 'reactHook', 'reactStatetool', 'nextJs', 'nextjs']
    frontend_advanced = ['react-up', 'FEoptimize', 'requirejs']
    
    old_cats_str = str(old_categories).lower()
    filename_lower = filename.lower()
    
    # DevLog 체크
    for keyword in devlog_keywords:
        if keyword.lower() in old_cats_str:
            return "DevLog"
    
    # Backend_infra 체크
    for keyword in backend_keywords:
        if keyword.lower() in old_cats_str:
            return "Backend_infra"
    
    # WebSecurity 체크
    for keyword in security_keywords:
        if keyword.lower() in old_cats_str:
            return "WebSecurity"
    
    # TechMisc 체크
    for keyword in misc_keywords:
        if keyword.lower() in old_cats_str:
            return "TechMisc"
    
    # Frontend 분류
    frontend_all_keywords = frontend_basic + frontend_intermediate + frontend_advanced + ['frontend', 'Frontend']
    
    is_frontend = False
    for keyword in frontend_all_keywords:
        if keyword.lower() in old_cats_str:
            is_frontend = True
            break
    
    if is_frontend:
        # 고급 Frontend 체크
        for keyword in frontend_advanced:
            if keyword.lower() in old_cats_str:
                return "Frontend3"
        
        # 중급 Frontend 체크 (Next.js, 고급 React)
        if any(k in old_cats_str for k in ['nextjs', 'next.js', 'next-js', 'react-query', 'redux', 'recoil', 'server', 'streaming', 'optimization']):
            return "Frontend2"
        
        # Next.js 관련 파일명 체크
        if any(term in filename_lower for term in ['next', 'ssr', 'ssg', 'server']):
            return "Frontend2"
        
        # React Hook, 상태관리 등은 중급
        if any(k in old_cats_str for k in ['reacthook', 'hook', 'useeffect', 'usestate', 'usereducer', 'usecallback', 'usememo']):
            return "Frontend2"
        
        # 기본적으로 Frontend1 (초급)
        return "Frontend1"
    
    # 기본값은 Frontend1으로 설정 (프론트엔드 관련이라고 가정)
    return "Frontend1"

def update_category_in_file(file_path):
    """파일의 카테고리를 업데이트"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 기존 카테고리 찾기
        category_pattern = r'^category:\s*(.+)$'
        match = re.search(category_pattern, content, re.MULTILINE)
        
        if not match:
            print(f"카테고리를 찾을 수 없음: {file_path}")
            return False
        
        old_category = match.group(1).strip()
        filename = os.path.basename(file_path)
        
        # 새로운 카테고리 결정
        new_category = determine_new_category(old_category, filename, content[:500])
        
        # 카테고리 교체
        new_content = re.sub(
            category_pattern,
            f'category: {new_category}',
            content,
            flags=re.MULTILINE
        )
        
        # 파일 쓰기
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {filename}: {old_category} → {new_category}")
        return True
        
    except Exception as e:
        print(f"❌ 오류 {file_path}: {e}")
        return False

def main():
    posts_dir = "/Users/yoojaeseok/src/yoo94.github.io/_posts"
    md_files = glob.glob(os.path.join(posts_dir, "*.md"))
    
    print(f"총 {len(md_files)}개 파일 처리 시작...\n")
    
    success_count = 0
    for file_path in md_files:
        if update_category_in_file(file_path):
            success_count += 1
    
    print(f"\n처리 완료: {success_count}/{len(md_files)} 파일 성공")

if __name__ == "__main__":
    main()
