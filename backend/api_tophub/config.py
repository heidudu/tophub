# -*- coding: utf-8 -*-
import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # github
    GITHUB_OAUTH2 = {
        #github上获取
        'client_id': '',
        'client_secret': '',
        'callback_url': '',
        'scope': 'user',
        'auth_url': 'http://github.com/login/oauth/authorize?client_id={client_id}&scope={scope}&state={csrf}'
                    '&redirect_uri={redirect_uri}',
    }
    # access_token过期时间设置,单位天
    ACCESS_TOKEN_EXP = 30

    # cookie 名称
    AUTH_COOKIE_NAME = 'token'

    # elastisearch配置，docker配置，所以host直接使用名称，正常情况为ip
    ELASTICSEARCH_URL = "elasticsearch:9200"

    # scrapyd配置
    SCRAPYD_URL = "http://127.0.0.1:6800"
    SCRAPY_PROJECT_NAME = "spider_tophub"

    # 爬虫scheduler配置
    JOBSTORES={'default': SQLAlchemyJobStore(url='mysql+pymysql://your_user:your_user_password@mysql:3306/your_databases')}
    JOB_DEFAULTS={
        'coalesce': True,
        'max_instances': 1
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://your_user:your_user_password@mysql:3306/your_databases'
    # 关闭flask_sqlalchemy事件系统
    SQLALCHEMY_TRACK_MODIFICATIONS = False





config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}