import paho.mqtt.publish as publish
from flask import current_app
from ..db.mongo import MongoWrapper
from ..extensions import mongo
from datetime import datetime
import time
import os
from app.exception import NotFound

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


def control_feeding(status, feeding_type='MANUAL'):
    history_collection = MongoWrapper(mongo, 'history')
    if status == 'OPEN':
        publish.single(current_app.config['FEEDING_TOPIC'], '1', hostname=current_app.config['MQT_SERVER'])
    else:
        publish.single(current_app.config['FEEDING_TOPIC'], '0', hostname=current_app.config['MQT_SERVER'])

    current_time = datetime.now()
    time_str = '{0}-{1}-{2} {3}:{4}'.format(current_time.day, current_time.month, current_time.year, current_time.hour,
                                            current_time.minute)
    data = {
        '_id': gen_id('history'),
        'timestamp': time_str,
        'status': status,
        'type': feeding_type
    }
    history_collection.insert(**data)
