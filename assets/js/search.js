$(document).ready(function() {
    'use strict';
    
    // 검색 관련 DOM 요소
    var search_field = $('.search-form__field'),
        search_results = $('.search-results'),
        toggle_search = $('.toggle-search-button'),
        close_search = $('.close-search-button'),
        search_result_template = "\
          <div class='search-results__item'>\
            <a class='search-results__item__title' href='{{link}}'>{{title}}</a>\
            <span class='post__date'>{{pubDate}}</span>\
          </div>";

    // lunr-korean이 로드되었는지 확인
    if (typeof lunr !== 'undefined') {
        console.log('Lunr.js가 성공적으로 로드되었습니다.');
        
        // lunr-korean이 로드되었는지 확인
        if (typeof lunr.ko !== 'undefined' || typeof lunr.korean !== 'undefined') {
            console.log('한국어 검색 모듈이 성공적으로 로드되었습니다.');
            
            // GhostHunter 설정
            search_field.ghostHunter({
                results: search_results,
                onKeyUp: true,
                rss: base_url + '/feed.xml',
                zeroResultsInfo: false,
                info_template: "<h4 class='heading'>검색된 포스트 수: {{amount}}</h4>",
                result_template: search_result_template,
                before: function() {
                    search_results.fadeIn();
                },
                includepages: true,
                filterFields: {
                    title: {
                        boost: 10
                    },
                    description: {
                        boost: 5
                    },
                    content: {
                        boost: 1
                    }
                },
                lunrOptions: {
                    // lunr-korean 사용 설정
                    // lunr.ko 또는 lunr.korean 둘 중 사용 가능한 것 선택
                    tokenizer: typeof lunr.korean !== 'undefined' ? 
                        lunr.korean.tokenizer : 
                        (typeof lunr.ko !== 'undefined' ? lunr.ko.tokenizer : undefined),
                    usePipeline: true
                }
            });
        } else {
            console.error("한국어 검색 모듈이 로드되지 않았습니다.");
            
            // 기본 검색 설정 (한국어 지원 없음)
            search_field.ghostHunter({
                results: search_results,
                onKeyUp: true,
                rss: base_url + '/feed.xml',
                zeroResultsInfo: false,
                info_template: "<h4 class='heading'>검색된 포스트 수: {{amount}}</h4>",
                result_template: search_result_template,
                before: function() {
                    search_results.fadeIn();
                }
            });
        }
    } else {
        console.error("Lunr.js가 로드되지 않았습니다.");
    }
});