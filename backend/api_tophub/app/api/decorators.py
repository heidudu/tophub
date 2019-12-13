# -*- coding: utf-8 -*-
from functools import wraps
from flask import request, current_app,g
from .errors import forbidden
from app.models.token import Token
from . import api


@api.before_request
def before_request():
    token = request.cookies.get(current_app.config['AUTH_COOKIE_NAME'])
    if token:
        res = Token.check_access_token(token)
        if not token:
            return
        if res and ('success' in res):
            g.current_user = res['data'].user
            return
        else:
            return
    else:
        return


def login_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if hasattr(g, 'current_user') :
                return f(*args, **kwargs)
            else:
                return forbidden('need login')
        return decorated_function
    return decorator


def admin_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if hasattr(g, 'current_user') and (g.current_user.role == 100):
                return f(*args, **kwargs)
            else:
                return forbidden('need admin')
        return decorated_function
    return decorator
