# -*- coding: utf-8 -*-
from flask import current_app
from app import exception


class MongoWrapper(object):
    def __init__(self, mongo, collection):
        self.db = mongo.db[collection]

    @classmethod
    def isdict(cls, params):
        rs = isinstance(params, dict)
        if not rs:
            raise ValueError('%s is not of type %s' % (params, dict))
        return params

    def find(self, spec):
        spec = self.isdict(spec)
        return self.db.find(spec)

    def find_one(self, spec, field=None):
        spec = self.isdict(spec)
        return self.db.find_one(spec, field)

    def insert(self, **doc):
        return self.db.insert(doc)

    def insert_many(self, docs):
        return self.db.insert(docs, continue_on_error=True)

    def update(self, spec, docs):
        spec = self.isdict(spec)
        docs = self.isdict(docs)
        return self.db.update(spec, {'$set': docs})

    def force_update(self, spec, docs):
        spec = self.isdict(spec)
        docs = self.isdict(docs)
        return self.db.update(spec, {'$set': docs}, upsert=True)

    def update_many(self, spec, docs):
        spec = self.isdict(spec)
        docs = self.isdict(docs)
        return self.db.update(spec, {'$set': docs}, multi=True)

    def remove(self, spec):
        spec = self.isdict(spec)
        return self.db.remove(spec)

    def aggregate(self, pipeline):
        return self.db.aggregate(pipeline)

    def execute_bulk(self, inserting_docs, updating_docs):
        bulk = self.db.initialize_unordered_bulk_op()
        # Insert
        for item in inserting_docs:
            bulk.insert(item)
        # Update
        for item in updating_docs:
            spec = self.isdict(item).get('spec', None)
            doc = self.isdict(item).get('doc', None)
            bulk.update(spec, {'$set': doc})

        # Execute bulk
        try:
            bulk.execute()
        except Exception as e:
            current_app.logger.info('Execute bulk operations err: {0}'.format(e))
            raise exception.BadRequest(1006)
