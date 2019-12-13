# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config
from elasticsearch import Elasticsearch
from apscheduler.schedulers.background import BackgroundScheduler



db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #config[config_name].init_app(app)

    # elastisearch 配置
    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) if app.config['ELASTICSEARCH_URL'] else None

    db.init_app(app)


    # blueprint设置
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/oauth')

    # 解决跨域
    CORS(app, supports_credentials=True,)

    # 爬虫scheduler配置
    app.scheduler = BackgroundScheduler(jobstores=app.config['JOBSTORES'], job_defaults=app.config['JOB_DEFAULTS'])
    app.scheduler.start()



    return app

