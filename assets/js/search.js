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
// 한국어 토크나이저 직접 구현
if (typeof lunr !== 'undefined' && typeof lunr.ko.tokenizer === 'undefined') {
  if(typeof lunr.ko === 'undefined') lunr.ko = {};
  lunr.ko.tokenizer = function(text) {
    var tokens = [];
    var str = text.toString().toLowerCase().trim();
    
    // 공백으로 단어 분리
    var words = str.split(/[\s]+/);
    
    words.forEach(function(word) {
      // 원본 단어 추가
      tokens.push(word);
      
      // 2-gram 및 3-gram 추가 (한글 검색 정확도 향상)
      if (word.length > 1) {
        for (var i = 0; i < word.length - 1; i++) {
          tokens.push(word.slice(i, i + 2));
          if (i < word.length - 2) {
            tokens.push(word.slice(i, i + 3));
          }
        }
      }
    });
    
    return tokens.filter(function(token) {
      return token.length > 0;
    });
  };
}
    search_field.ghostHunter({
    results: search_results,
    onKeyUp: true,
    rss: base_url + '/feed.xml',
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
      usePipeline: true,
      tokenizer: lunr.ko && lunr.ko.tokenizer ? lunr.ko.tokenizer : undefined
    }
  });
});