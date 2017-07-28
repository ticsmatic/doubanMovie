# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class DoubanMoviePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            user='root',
            password='123456',
            host = '127.0.0.1',
            db = 'test',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "insert into douban_movie(no,movie_name,director,writer,actor,type,region,language,date,length,another_name,introduction,grade,comment_times) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    item['no'],
                    item['movie_name'],
                    item['director'],
                    item['writer'],
                    item['actor'],
                    item['type'],
                    item['region'],
                    item['language'],
                    item['date'],
                    item['length'],
                    item['another_name'],
                    item['introduction'],
                    item['grade'],
                    item['comment_times']
                )
            )
            self.conn.commit()
        except Exception as e:
            print(e)
        return item
