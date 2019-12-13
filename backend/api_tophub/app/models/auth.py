# -*- coding: utf-8 -*-
from datetime import datetime
from app import db


class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    # 用户的唯一id
    openid = db.Column(db.String(64), unique=True)
    # 令牌
    #access_token = db.Column(db.String(64))
    # 令牌有效时间，单位为秒
    #expires_in = db.Column(db.Integer)
    # 刷新令牌
    #refresh_token = db.Column(db.String(64))
    # 注册来源
    # source = db.Column(db.Enum('github', 'qq'), default='github')
    # 引用User表的id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 创建时间
    create_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return '<Auth %r>' % self.openid


