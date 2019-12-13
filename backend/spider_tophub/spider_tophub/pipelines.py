# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
from twisted.enterprise import adbapi
import pymysql
from .utils import add_to_index



class SpiderTophubPipeline(object):
    def open_spider(self, spider):
        self.file = open(sys.argv[1] + '.j1', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如:“/xe15”
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


class MysqlTwistedPipeline(object):
    """
    通用的数据库保存Pipeline
    """

    def __init__(self, dbpool, dont_filter):
        self.dbpool = dbpool
        self.dont_filter = dont_filter

    @classmethod
    def from_settings(cls, settings):
        """
        自定义组件或扩展很有用的方法: 这个方法名字固定, 是会被scrapy调用的。
        这里传入的cls是指当前的class
        """
        db_parms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        # 连接池ConnectionPool
        dbpool = adbapi.ConnectionPool("pymysql", **db_parms)


        # 不过滤的爬虫，即需要操作更新
        dont_filter = settings['DONT_FILTER']
        # 此处相当于实例化pipeline, 要在init中接收。
        return cls(dbpool, dont_filter)

    def open_spider(self, spider):
        if spider.name in self.dont_filter:
            query = self.dbpool.runInteraction(self.do_reset, spider)
            # 添加自己的处理异常的函数
            query.addErrback(self.handle_error)

    def process_item(self, item, spider):
        """
        使用twisted将mysql插入变成异步执行
        参数1: 我们每个item中自定义一个函数,里面可以写我们的插入数据库的逻辑
        """
        query = self.dbpool.runInteraction(self.do_insert, item, spider)
        # 添加自己的处理异常的函数
        query.addErrback(self.handle_error)
        return

    def do_reset(self, tx, spider):
        tx.execute('update top set position = 0 where node_id = %s and position <> 0', spider.custom_settings['node_id'])

    def do_insert(self, tx, item, spider):
        sql_in = 'select id from top where node_id=%s and url=%s'
        tx.execute(sql_in, (item['node_id'], item['url']))
        tmp = tx.fetchone()
        if tmp:
            if spider.custom_settings['type'] == 1:
                sql_in = 'update top set update_at=%s,position=%s,description_content=%s where id=%s'
                tx.execute(sql_in, (item['update_at'], item['position'], item['description_content'], tmp['id']))
                # 更新数据到es
                sql_in = 'select id from top where node_id=%s and url=%s'
                tx.execute(sql_in, (item['node_id'], item['url']))
                tmp = tx.fetchone()
                add_to_index(tmp['id'], item['title'], item['description_content'], item['update_at'])

        else:
            sql_in = 'insert into top(node_id, title, url, publish_at, description_content, create_at, update_at, position) values (%s, %s, %s, %s,%s, %s, %s, %s)'
            tx.execute(sql_in, (item['node_id'], item['title'], item['url'], item['publish_at'], item['description_content'], item['create_at'], item['update_at'], item['position']))
            # 自动添加数据到es
            sql_in = 'select id from top where node_id=%s and url=%s'
            tx.execute(sql_in, (item['node_id'], item['url']))
            tmp = tx.fetchone()
            add_to_index(tmp['id'],item['title'],item['description_content'],item['update_at'])


    @staticmethod
    def handle_error(failure):
        # 处理异步插入的异常
        print(failure)
