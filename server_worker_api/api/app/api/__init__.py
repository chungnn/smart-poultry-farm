# -*- coding: utf-8 -*-
from app.exception import NotFound
import time
import os
resource_dict = {
    'user': '101095-00',
    'role': '101095-01',
    'permission': '101095-02',
    'settings': '101095-03',
    'history': '101095-04',
    'pair_id': 'pair-05'
}


def get_resource(resource):
    if resource not in resource_dict:
        raise NotFound(5000)
    return resource_dict[resource]


def gen_id(resource):
    prefix = get_resource(resource)
    datetime = time.time()
    _id = prefix + str(datetime) + os.urandom(6).encode('hex')
    return _id
