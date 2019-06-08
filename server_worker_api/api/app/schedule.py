from extensions import scheduler, mongo
from utils.farm_control import control_feeding
from db.mongo import MongoWrapper
from datetime import datetime
import logging


def configure_scheduler(app):
    logging.basicConfig()
    scheduler.add_job(auto_feeding, 'interval', kwargs={'app': app}, seconds=10)
    scheduler.start()


def auto_feeding(app):
    with app.app_context():
        setting_collection = MongoWrapper(mongo, 'setting')
        all_settings = list(setting_collection.find(spec={}))
        current_time = datetime.now()
        if all_settings:
            setting_group = {}
            for setting in all_settings:
                if setting['pair_id'] not in setting_group:
                    setting_group[setting['pair_id']] = []
                setting_group[setting['pair_id']].append(setting)

            for key, value in setting_group.iteritems():
                for item in value:
                    time_str = item['time']
                    time_obj = datetime.strptime(time_str, '%H:%M:%S')
                    if time_obj.hour == current_time.hour and current_time.minute == time_obj.minute and \
                            0 <= current_time.second - time_obj.second <= 10:
                        if item['message'] == 'OPEN':
                            print current_time.second - time_obj.second
                            print item
                            control_feeding('OPEN', feeding_type='AUTO')
                        elif item['message'] == 'CLOSE':
                            print current_time.second - time_obj.second
                            print item
                            control_feeding('CLOSE', feeding_type='AUTO')


