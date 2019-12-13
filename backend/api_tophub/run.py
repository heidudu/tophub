import os
from app import create_app, db
from flask_migrate import Migrate, upgrade,migrate, init as migrate_init
import click
from app.models import Auth, User, Token, Topic, Top, Node, Source,Task
import jwt
import datetime




app = create_app(os.getenv('FLASK_CONFIG') or 'default')
db_migrate = Migrate(app, db)


# 在shell窗口执行
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Auth=Auth, User=User, Token=Token, Topic=Topic, Top=Top, Node=Node, Source=Source, Task=Task)


@app.cli.command()
def deploy():
    migrate()
    upgrade()


@app.cli.command()
def init():
    db.create_all()
    migrate_init()


@app.cli.command()
def test():
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
        'iat': datetime.datetime.utcnow(),
        'iss': 'tophub',
        'data': {
            'id': 1,
        }
    }
    access_token=jwt.encode(payload, 'secret', algorithm='HS256').decode('ascii')
    print(access_token)
    data = jwt.decode(access_token, 'secret', algorithm='HS256')
    print(data)

# 历史爬虫数据同步到elasticsearch
@app.cli.command()
def reindex():
    Top.reindex()
    Node.reindex()
    Source.reindex()



if __name__ == '__main__':
    app.run(host='0.0.0.0')

