from app import db
from flask import current_app



def add_to_index(index, model):
    if not current_app.elasticsearch:
        return

    if not current_app.elasticsearch.indices.exists(index=index):  # 如果是第一次插入，Index 还没创建
        # 创建 Index
        current_app.elasticsearch.indices.create(index=index, ignore=400)
        # IK 模板，这里假设每个字段都用 text 类型，如果你要修改，也可以通过 __searchable__ 传递过来



        mapping = {
            index: {
                "properties": model.__searchable__
            }
        }
        current_app.elasticsearch.indices.put_mapping(index=index, body=mapping)

    payload = {}
    for field in model.__searchable__.keys():
        # 转时间戳
        if field == "update_at":
            payload[field] = int(getattr(model, field).timestamp()*1000)
        else:
            payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, id=model.id, body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)


def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return [], 0, []
    # 中文分词器 ik 会将 query 拆分成哪些查找关键字，前端将通过正则表达式来高亮这些词

    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    scores = [int(hit['_score']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value'],scores


class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page,):
        ids, total, scores = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0, []
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(db.case(when, value=cls.id)), total, scores


    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }



    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None



    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

    @classmethod
    def delete_all_index(cls):
        current_app.elasticsearch.indices.delete(index=cls.__tablename__, ignore=[400, 404])


db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)

