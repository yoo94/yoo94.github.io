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

    close_search.click(function() {
        $('.search-form-container').removeClass('is-active');
    });

    search_field.ghostHunter({
        results: search_results,
        onKeyUp: true,
        rss: base_url + '/feed.xml',
        zeroResultsInfo: false,
        info_template: "<h4 class='heading'>Number of posts found: {{amount}}</h4>",
        result_template: search_result_template,
        before: function() {
            search_results.fadeIn();
        },
        includepages: true, // 필요한 경우 페이지 포함
        filterFields: ['title', 'description'], // 검색할 필드
        displaySearchInfo: true,
        lunrOptions: {
            usePipeline: true,
            // 한글을 위한 lunr-ko 사용
            tokenizer: function (obj) {
                return lunr.ko(obj);
            }
        }
    });
});
