# -*- coding: utf-8 -*-
import os
from flask import request, make_response, redirect, current_app
import requests
from app.models import User, Auth
from app import db
import re


# 重定向登录
def redirect_sign_in(oauth2):

    # 用于第三方登录校验,防止csrf
    csrf = os.urandom(24)
    # 请求来源
    landing_page_domain = re.search(r"((http|ftp|https)://)(([a-zA-Z0-9._-]+)|([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}))(([a-zA-Z]{2,6})|(:[0-9]{1,4})?)",request.referrer).group()

    # 'http://github.com/login/oauth/authorize?client_id={client_id}&scope={scope}&state={csrf}'
    # '&redirect_uri={redirect_uri}'
    url = oauth2['auth_url'].format(client_id=oauth2['client_id'], scope=oauth2['scope'], csrf=csrf, redirect_uri=oauth2['callback_url'])

    res = make_response(redirect(url))

    # cookie设置
    # 过期时间 15分钟
    max_age = 60 * 15
    res.set_cookie('csrf', value=csrf, httponly=True, max_age=max_age)
    res.set_cookie('landing_page_domain', value=landing_page_domain, httponly=True, max_age=max_age)
    return res


# 获取GitHub令牌
def github_get_access_token(code, state):
    data = {
        'client_id': current_app.config['GITHUB_OAUTH2']['client_id'],
        'client_secret': current_app.config['GITHUB_OAUTH2']['client_secret'],
        'code': code,
        'redirect_uri': current_app.config['GITHUB_OAUTH2']['callback_url'],
        'state': state
    }
    headers = {
        'accept': 'application/json'
    }

    return requests.post('https://github.com/login/oauth/access_token',data=data, headers=headers)


# 获取GitHub用户信息
def github_get_user_info(access_token):
    url = 'https://api.github.com/user?access_token=' + access_token
    headers = {
        'Accept': 'application/json',
        'User-Agent': request.headers['user-agent']
    }
    return requests.get(url, headers=headers)


# 第三方登录报错返回客户端
def go_to_notice_page(message):
    landing_page_domain = request.cookies['landing_page_domain']
    return redirect(landing_page_domain + 'notice?notice=' + message)


# 获取或注册user
def get_or_create_user(oauth2_user_info):
    auth = Auth.query.filter_by(openid=oauth2_user_info['id']).first()
    if not auth:
        try:

            user = User(
                nickname=oauth2_user_info['name'] or oauth2_user_info['login'],
                avatar=oauth2_user_info['avatar_url'] or ' ',
            )
            auth = Auth(openid=oauth2_user_info['id'])
            auth.user = user
            db.session.add(auth)
            db.session.commit()
        except:
            db.session.rollback()
            return False

        return Auth.query.filter_by(openid=oauth2_user_info['id']).first().user_id
    return auth.user_id






