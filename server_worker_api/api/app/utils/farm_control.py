import paho.mqtt.publish as publish
from flask import current_app
from ..db.mongo import MongoWrapper
from ..extensions import mongo
from ..api import gen_id
from datetime import datetime


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
