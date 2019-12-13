# -*- coding: utf-8 -*-
from . import api
from flask import g, jsonify, make_response,request
from .errors import forbidden
from .decorators import login_required


@api.route('/user/userinfo')
@login_required()
def get_user():
    res = make_response({'success': True, 'data': g.current_user.to_json()})

    return res


