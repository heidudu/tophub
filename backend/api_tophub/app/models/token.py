# -*- coding: utf-8 -*-
from app import db
import jwt
import datetime
from flask import current_app



class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    # ip
    ip = db.Column(db.String(64))
    # 用户访问令牌
    token = db.Column(db.Text)
    # 引用User表的id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Token %r>' % self.id

    @staticmethod
    def create_access_token(ip, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['ACCESS_TOKEN_EXP']),
                'iat': datetime.datetime.utcnow(),
                'iss': 'tophub',
                'data': {
                    'id': user_id,
                }
            }
            # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str
            access_token = jwt.encode(payload, 'secret', algorithm='HS256').decode('ascii')
            token = Token(
                ip=ip,
                token=access_token,
                user_id=user_id
            )
            db.session.add(token)
            db.session.commit()
        except:
            return False
        return access_token

    @staticmethod
    def check_access_token(access_token):
        try:
            payload = jwt.decode(access_token, 'secret', algorithms='HS256')
            if ('data' in payload) and ('id' in payload['data']):
                result = Token.query.filter_by(token=access_token, user_id=payload['data']['id']).first()
                if not result:
                    raise jwt.InvalidTokenError
                else: return {'success':True,'data':result}
            else:
                raise jwt.InvalidTokenError

        except jwt.ExpiredSignatureError:
            return {'error': 'token_expired'}
        except jwt.InvalidTokenError:
            return {'error': 'invalid_token'}