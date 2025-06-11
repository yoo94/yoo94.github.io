lunr.ko.tokenizer = function(obj) {
  if (!arguments.length || obj == null || obj == undefined) return [];
  if (Array.isArray(obj)) return obj.map(function(t) { return lunr.utils.asString(t).toLowerCase(); });

  var str = obj.toString().toLowerCase().trim();
  var tokens = [];
  
  // 2-gram과 3-gram 생성
  for (var i = 0; i < str.length - 1; i++) {
    // 2-gram
    tokens.push(str.slice(i, i + 2));
    // 3-gram (가능한 경우)
    if (i < str.length - 2) {
      tokens.push(str.slice(i, i + 3));
    }
  }
  
  // 단일 문자도 추가
  for (var i = 0; i < str.length; i++) {
    tokens.push(str.charAt(i));
  }
  
  return tokens.filter(function(token) {
    return token.length > 0;
  });
};

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
      
  // Korean tokenizer 직접 구현
  if (typeof lunr !== 'undefined' && typeof lunr.ko !== 'undefined') {
    lunr.ko.tokenizer = function(obj) {
      if (!arguments.length || obj == null || obj == undefined) return [];
      if (Array.isArray(obj)) return obj.map(function(t) { return lunr.utils.asString(t).toLowerCase(); });

      var str = obj.toString().toLowerCase().trim();
      var tokens = [];
      
      // 단어 단위 토큰화 (공백 기준)
      var words = str.split(/[\s]+/);
      words.forEach(function(word) {
        tokens.push(word); // 원래 단어도 추가
        
        // 2-gram 추가 (한글 자모 조합 고려)
        if (word.length > 1) {
          for (var i = 0; i < word.length - 1; i++) {
            tokens.push(word.slice(i, i + 2));
          }
        }
      });
      
      return tokens.filter(function(token) {
        return token.length > 0;
      });
    };
    
    console.log('한글 검색을 위한 토크나이저를 등록했습니다.');
  }
  
  // 검색 초기화
  search_field.ghostHunter({
    results: search_results,
    onKeyUp: true,
    rss: base_url + '/feed.xml',
    info_template: "<h4 class='heading'>검색된 포스트 수: {{amount}}</h4>",
    result_template: search_result_template,
    before: function() {
      search_results.fadeIn();
    },
    // 한글 검색 설정
    includepages: true,
    filterFields: ['title', 'content', 'description'],
    lunrOptions: {
      usePipeline: true,
      tokenizer: lunr.ko.tokenizer,
      language: 'ko'
    }
  });
});