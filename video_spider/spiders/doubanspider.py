# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from scrapy.cmdline import execute
from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from video_spider.items import DoubanMovieItem


class DouBanSpider(CrawlSpider):
    name = 'douban_movie'
    # 起始url
    start_urls = [
        "https://movie.douban.com/top250"
    ]
    # 抓取规则
    # 握草，可以这样简写？？？
    rules = [
        Rule(LinkExtractor(allow=(r"https://movie.douban.com/subject/\d+/?$")), callback="parse_page"),
        Rule(LinkExtractor(allow=(r"https://movie.douban.com/top250")), follow=True)
    ]

    # 解析抓取到网页
    def parse_page(self, response):
        soup = BeautifulSoup(response.body, 'html.parser', from_encoding='utf-8')
        movie_name_tag = soup.find('div', id='content').findChild('h1')
        no = soup.find('span', 'top250-no').get_text()
        movie_name = movie_name_tag.findChildren()[0].get_text() + movie_name_tag.findChildren()[1].get_text()
        director = soup.find('a', rel='v:directedBy').get_text()
        #TODO 这里，厉害了，我的BS
        writer = soup.find('span', text='编剧').next_sibling.next_sibling.text
        actor = '/'.join(star.text for star in soup.findAll('a', rel='v:starring'))
        type = '/'.join(genre.text for genre in soup.findAll('span', property='v:genre'))
        region = soup.find('span', text='制片国家/地区:').next_sibling
        language = soup.find('span', text='语言:').next_sibling
        date = soup.find('span', property='v:initialReleaseDate').text
        length_tag = soup.find('span', property='v:runtime')
        if str(length_tag.next_sibling) != '<br/>':
            length = length_tag.text + str(length_tag.next_sibling)
        else:
            length = length_tag.text
        another_name = soup.find('span', text='又名:').next_sibling
        introduction = soup.find('span', property='v:summary').text
        grade = soup.find('strong', property='v:average').text
        comment_times = soup.find('span', property='v:votes').text

        item = DoubanMovieItem()
        item['no'] = no
        item['movie_name'] = movie_name
        item['director'] = director
        item['writer'] = writer
        item['actor'] = actor
        item['type'] = type
        item['region'] = region
        item['language'] = language
        item['date'] = date
        item['length'] = length
        item['another_name'] = another_name
        item['introduction'] = introduction
        item['grade'] = grade
        item['comment_times'] = comment_times

        return item
# if __name__ == '__main__':
#     execute('scrapy crawl douban_movie'.split(' '))