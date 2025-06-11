(function() {
  // 원래 lunr 토커나이저 저장
  var originalTokenizer = lunr.tokenizer;
  
  // 새로운 토큰화 함수로 오버라이드
  lunr.tokenizer = function(obj) {
    if (!arguments.length || obj == null || obj == undefined) return [];
    if (Array.isArray(obj)) return obj.map(function(t) { return t.toLowerCase(); });
    
    // 한글 문자열 처리를 위한 로직
    var str = obj.toString().trim().toLowerCase();
    
    // 정규식 패턴: 한글 음절 또는 영숫자 연속 문자열 추출
    var tokens = [];
    var pattern = /[\uAC00-\uD7A3]+|[a-zA-Z0-9]+/g;
    var match;
    
    while ((match = pattern.exec(str)) !== null) {
      // 한글은 음절 단위로 분리하여 토큰화
      var token = match[0];
      
      // 한글 문자열인 경우 (첫 글자가 한글 범위에 있는지 확인)
      if (token.charCodeAt(0) >= 0xAC00 && token.charCodeAt(0) <= 0xD7A3) {
        // 한글은 2글자 이상인 경우에만 개별 음절도 토큰으로 추가
        tokens.push(token); // 전체 단어 추가
        
        if (token.length >= 2) {
          // 개별 음절도 추가
          for (var i = 0; i < token.length; i++) {
            tokens.push(token[i]);
          }
          
          // 연속된 2글자도 토큰으로 추가 (검색 정확도 향상)
          for (var i = 0; i < token.length - 1; i++) {
            tokens.push(token.substring(i, i + 2));
          }
        }
      } else {
        // 영숫자는 그대로 추가
        tokens.push(token);
      }
    }
    
    return tokens;
  };
})();
// 외부 lunr.js를 사용하도록 수정된 ghostHunter
(function($) {
  // 외부에서 로드된 lunr를 사용 (내장 lunr 제거)
  
  $.fn.ghostHunter = function(options) {
    var opts = $.extend({}, $.fn.ghostHunter.defaults, options);
    
    if (opts.results) {
      pluginMethods.init(this, opts);
      return pluginMethods;
    }
  };

  $.fn.ghostHunter.defaults = {
    results: false,
    rss: "/rss",
    onKeyUp: false,
    result_template: "<a href='{{link}}'><p><h2>{{title}}</h2><h4>{{pubDate}}</h4></p></a>",
    info_template: "<p>검색 결과: {{amount}}개</p>",
    displaySearchInfo: true,
    zeroResultsInfo: true,
    before: false,
    onComplete: false
  };

  var pluginMethods = {
    isInit: false,
    init: function(target, opts) {
      var that = this;
      this.target = target;
      this.rss = opts.rss;
      this.results = opts.results;
      this.blogData = [];
      this.result_template = opts.result_template;
      this.info_template = opts.info_template;
      this.zeroResultsInfo = opts.zeroResultsInfo;
      this.displaySearchInfo = opts.displaySearchInfo;
      this.before = opts.before;
      this.onComplete = opts.onComplete;

      // 외부 lunr를 사용하여 인덱스 초기화
      this.index = lunr(function() {
        // 한글 분석기 추가
        if (lunr.ko) {
          this.use(lunr.ko);
        }
        
        this.field("title", { boost: 10 });
        this.field("description");
        this.field("link");
        this.field("category");
        this.field("pubDate");
        this.ref("id");
      });

      target.focus(function() {
        that.loadRSS();
      });

      target.closest("form").submit(function(e) {
        e.preventDefault();
        that.find(target.val());
      });

      if (opts.onKeyUp) {
        that.loadRSS();
        target.keyup(function() {
          that.find(target.val());
        });
      }
    },

    loadRSS: function() {
      if (this.isInit) return false;
      
      var that = this;
      var rssURL = this.rss,
          blogData = this.blogData;

      $.get(rssURL, function(data) {
        var posts = $(data).find("item");
        var documents = []; // 문서 배열 생성
        
        // 먼저 모든 문서 데이터 수집
        for (var i = 0; i < posts.length; i++) {
          var post = posts.eq(i);
          var parsedData = {
            id: (i + 1).toString(), // 문자열로 변환 (중요)
            title: post.find("title").text(),
            description: post.find("description").text(),
            category: post.find("category").text(),
            pubDate: post.find("pubDate").text(),
            link: post.find("link").text()
          };
          
          documents.push(parsedData); // 문서 배열에 추가
          blogData.push(parsedData); // blogData에도 추가
        }
        
        // 모든 문서를 가지고 새 인덱스 생성
        that.index = lunr(function() {
          // 한글 분석기 추가
          if (lunr.ko) {
            this.use(lunr.ko);
          }
          
          this.ref('id');
          this.field('title', { boost: 10 });
          this.field('description');
          this.field('category');
          this.field('link');
          this.field('pubDate');
          
          // 모든 문서를 한 번에 추가
          documents.forEach(function(doc) {
            this.add(doc);
          }, this);
        });
        
        console.log("인덱스 생성 완료: ", documents.length + "개 문서 색인됨");
      });

      this.isInit = true;
    },

    find: function(value) {
      var searchResult = this.index.search(value);
      var results = $(this.results);
      var resultsData = [];
      
      results.empty();
      
      if (this.before) {
        this.before();
      }
      
      if (this.zeroResultsInfo || searchResult.length > 0) {
        if (this.displaySearchInfo) {
          results.append(this.format(this.info_template, { amount: searchResult.length }));
        }
      }
      
      for (var i = 0; i < searchResult.length; i++) {
        var postData = {};
        
        // lunr 버전에 따라 결과 구조가 달라질 수 있으므로 처리
        var ref = searchResult[i].ref || searchResult[i].ref;
        
        // ref 값이 숫자형이면 그대로 사용, 문자열이면 파싱
        var postIndex = parseInt(ref, 10) - 1;
        
        if (this.blogData[postIndex]) {
          postData = this.blogData[postIndex];
          results.append(this.format(this.result_template, postData));
          resultsData.push(postData);
        }
      }
      
      if (this.onComplete) {
        this.onComplete(resultsData);
      }
    },

    clear: function() {
      $(this.results).empty();
      this.target.val("");
    },

    format: function(t, d) {
      return t.replace(/{{([^{}]*)}}/g, function(a, b) {
        var r = d[b];
        return typeof r === "string" || typeof r === "number" ? r : a;
      });
    }
  };
})(jQuery);