# -*- coding: utf-8 -*-
from flask import current_app, request, redirect, url_for, make_response
from . import auth
from .base_auth import redirect_sign_in, github_get_access_token, github_get_user_info, go_to_notice_page,\
    get_or_create_user
from app.models import Token
from app import db



@auth.route('/github')
def github_sign_in():
    return redirect_sign_in(current_app.config['GITHUB_OAUTH2'])


@auth.route('/github-callback')
def github_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    # 避免csrf攻击
    if request.cookies.get('csrf') != state:
        redirect(url_for('.github_sign_in'))

    # 获取第三方令牌
    result = github_get_access_token(code, state)
    if result.status_code != 200:
        return go_to_notice_page('wrong_token')
    if not result:
        redirect(url_for('.github_callback'))

    # 获取github_user_info
    github_user_info = github_get_user_info(result.json()['access_token'])
    if github_user_info.status_code != 200:
        return go_to_notice_page(github_user_info.json()['error'])

    # 获取user_id
    user_id = get_or_create_user(github_user_info.json())
    if not user_id:
        return go_to_notice_page('create_user_failed')

    # 生成access_token
    ip = request.remote_addr
    access_token = Token.create_access_token(ip, user_id)
    if not access_token:
        return go_to_notice_page('create_token_failed')

    # 返回access_token
    landing_page_domain = request.cookies['landing_page_domain']
    url = landing_page_domain + '/oauth?access_token=' + access_token

    return redirect(url)


@auth.route('/sign/in', methods=['POST'])
def sign_in():
    access_token = request.get_json()['access_token']
    max_age = 60*60*24*current_app.config['ACCESS_TOKEN_EXP']
    res = make_response({'success': True})
    res.set_cookie(current_app.config['AUTH_COOKIE_NAME'], value=access_token, httponly=True, max_age=max_age, path='/')
    return res


@auth.route('/sign/out', methods=['POST'])
def sign_out():
    access_token = request.cookies.get(current_app.config['AUTH_COOKIE_NAME'])
    token = Token.query.filter(Token.token == access_token).first()
    db.session.delete(token)
    db.session.commit()
    res = make_response({'success': True})
    res.set_cookie(current_app.config['AUTH_COOKIE_NAME'], '', httponly=True, max_age=0, path='/')
    return res











