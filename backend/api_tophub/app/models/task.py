# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
import shortuuid


# 爬虫定时任务
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    # 名称
    name = db.Column(db.String(32), unique=True,index=True)
    # 间隔时间（分钟）
    interval = db.Column(db.Integer, default=3)
    # 状态 0停止，1运行
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task name={0}>'.format(self.name)

