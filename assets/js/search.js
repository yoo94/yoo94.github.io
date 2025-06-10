$(document).ready(function() {
    'use strict';
    var search_field = $('.search-form__field'),
        search_results = $('.search-results'),
        toggle_search = $('.toggle-search-button'),
        close_search = $('.close-search-button'),
        search_result_template = "\
          <div class='search-results__item'>\
            <a class='search-results__item__title' href='{{link}}'>{{title}}</a>\
            <span class='post__date'>{{pubDate}}</span>\
          </div>";

    toggle_search.click(function(event) {
      event.preventDefault();
      $('.search-form-container').addClass('is-active');

      setTimeout(function() {
        search_field.focus();
      }, 500);
    });

    $('.search-form-container').on('keyup', function(event) {
      if (event.keyCode == 27) {
        $('.search-form-container').removeClass('is-active');
      }
    });

    $('.close-search-button').click(function() {
      $('.search-form-container').removeClass('is-active');
    });

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
        filterFields: ['title', 'description'],
        displaySearchInfo: true,
        lunrOptions: {
            usePipeline: true,
            // 한국어 토크나이저 설정
            tokenizer: function (obj) {
                tokenizer: lunr.tokenizer // 기본 토크나이저로 변경
            }
        },
    });
    // 한글 검색을 위한 lunr-ko 초기화
    if (typeof lunr !== 'undefined' && typeof lunr.ko !== 'undefined') {
        lunr.tokenizer = lunr.ko.tokenizer;
    } else {
        console.error("lunr-ko가 제대로 로드되지 않았습니다.");
    }
  });