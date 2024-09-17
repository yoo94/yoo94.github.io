source "https://rubygems.org"

gem 'jekyll', '~> 4.3.4'
gem 'faraday-retry'
gem 'backports', '~> 3.23'
gem 'kramdown'
gem 'puma'

# Plugins
group :jekyll_plugins do
    gem 'jgd', '~> 1.12'
    gem 'jekyll-feed', '~> 0.17.0'
    gem 'jekyll-paginate', '~> 1.1.0'
    gem 'jekyll-gist', '~> 1.5.0'
    gem 'jekyll-seo-tag'
    gem 'jekyll-sitemap'
    gem 'jekyll-admin'  # Add this line
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 2.0"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1" if Gem.win_platform?
gem "webrick", "~> 1.7"
gem "rack", "~> 3.1.7"
