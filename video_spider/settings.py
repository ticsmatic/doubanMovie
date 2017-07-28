# -*- coding: utf-8 -*-

BOT_NAME = 'video_spider'

SPIDER_MODULES = ['video_spider.spiders']
NEWSPIDER_MODULE = 'video_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

# 默认的头
DEFAULT_REQUEST_HEADERS = {
                           'Referer': 'https://movie.douban.com/'
}

ITEM_PIPELINES = {
   'video_spider.pipelines.DoubanMoviePipeline': 300,
}

DOWNLOAD_DELAY = 0.5   # 250 ms of delay