# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, request, jsonify
from ..extensions import mongo, parser
from ..utils.farm_control import control_feeding
from ..utils.schema import Setting
from ..exception import BadRequest, NotFound
from ..db.mongo import MongoWrapper
import copy
from . import gen_id
from marshmallow import fields
from datetime import date, datetime, time, timedelta


api = Blueprint('chicken_farm_api', __name__, url_prefix='/api/v1/chicken_farm')


@api.route('/get_settings', methods=['GET'])
def get_all_settings():
    setting_collection = MongoWrapper(mongo, 'setting')
    all_settings = list(setting_collection.find(spec={}))
    rs = []
    if all_settings:
        setting_group = {}
        for setting in all_settings:
            if setting['pair_id'] not in setting_group:
                setting_group[setting['pair_id']] = []
            setting_group[setting['pair_id']].append(setting)

        for key, value in setting_group.iteritems():
            open_obj = value[0]
            time_open_obj = datetime.strptime(open_obj['time'], '%H:%M:%S')
            close_obj = value[1]
            time_close_obj = datetime.strptime(close_obj['time'], '%H:%M:%S')
            duration = time_close_obj.minute - time_open_obj.minute
            data = {
                'hour': time_open_obj.hour,
                'minute': time_open_obj.minute,
                'duration': duration
            }
            rs.append(data)

    return jsonify({'count': len(rs), 'settings': rs})


@api.route('/settings', methods=['POST'])
def setting():
    params = {
        'settings': fields.List(fields.Nested(Setting), required=True)
    }
    args = parser.parse(params)
    settings = args.get('settings')
    settings_collection = MongoWrapper(mongo, 'setting')
    if settings_collection:
        settings_collection.remove(spec={})

    if settings:
        for sett in settings:
            pair_id = gen_id('pair_id')
            setting_time = datetime.combine(date.today(), time(sett.get('hour'), sett.get('minute')))
            dt_open = setting_time
            dt_close = setting_time + timedelta(minutes=sett.get('duration'))
            open_config = {
                '_id': gen_id('settings'),
                'pair_id': pair_id,
                'time': str(dt_open.time()),
                'message': 'OPEN'
            }
            settings_collection.insert(**open_config)
            close_config = {
                '_id': gen_id('settings'),
                'pair_id': pair_id,
                'time': str(dt_close.time()),
                'message': 'CLOSE'
            }
            settings_collection.insert(**close_config)
        return jsonify({'message': 'setting time successfully'})
    return jsonify({'message': 'setting time failed'})


@api.route('/feeding', methods=['POST'])
def feeding():
    params = {
        'status': fields.String(required=True)
    }
    args = parser.parse(params)
    status = args['status']
    control_feeding(status)
    return jsonify({'message': 'feeding {0}'.format(status)})


@api.route('/feeding_history', methods=['GET'])
def get_feeding_history():
    history_collection = MongoWrapper(mongo, 'history')
    all_history = history_collection.find({})
    print all_history
    return jsonify({'history': list(all_history)})
