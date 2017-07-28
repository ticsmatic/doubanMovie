# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    no = scrapy.Field()
    movie_name = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    region = scrapy.Field()
    language = scrapy.Field()
    date = scrapy.Field()
    length = scrapy.Field()
    another_name = scrapy.Field()
    introduction = scrapy.Field()
    grade = scrapy.Field()
    comment_times = scrapy.Field()
    pass

