# coding=utf-8
__author__ = 'huydq17'

import time
from flask import current_app
from datetime import datetime


def to_string(time_from, time_to):
    if (time_from.day, time_from.month, time_from.year) == (time_to.day, time_to.month, time_to.year):
        return '{0}/{1}/{2}'.format(time_from.day, time_from.month, time_from.year)
    return '{0}/{1}/{2} - {3}/{4}/{5}'.format(time_from.day, time_from.month, time_from.year,
                                              time_to.day, time_to.month, time_to.year)


class DateTimeWrapper(object):
    def __init__(self):
        # Timestamp is in millisecond
        pass

    @staticmethod
    def curr_timestamp(unit='second'):
        if unit == 'millisecond':
            return int(time.time()) * 1000
        return int(time.time())

    @staticmethod
    def to_datetime(timestamp, fmt='%H:%M:%S %d-%m-%Y'):
        """
        Convert timestamp in second to datetime readable format
        :param timestamp:
        :param fmt:
        :return:
        """
        try:
            return datetime.fromtimestamp(int(timestamp)).strftime(fmt)
        except Exception as e:
            current_app.logger.error('Error when convert timestamp to datetime: {0}'.format(str(e)))
            return timestamp

    @staticmethod
    def to_timestamp(str_datetime, fmt='%H:%M:%S %d-%m-%Y'):
        """
        Convert datetime in string with valid format to timestamp
        """
        timestamp = time.mktime(datetime.strptime(str_datetime, fmt).timetuple())
        return int(timestamp)

    @staticmethod
    def datetime_to_timestamp(datetime_obj, unit='second'):
        """
        Convert python datetime object to timestamp in unit (second or millisecond)
        """
        delta = 1000 if unit == 'millisecond' else 1
        return int(time.mktime(datetime_obj.timetuple()) * delta)

    @staticmethod
    def rfc3339_to_timestamp(rfc_time, fmt='%Y-%m-%dT%H:%M:%S.%fZ'):
        """
        Convert UTC time in RFC 3339 format to timestamp
        Example: 2017-07-19T03:20:13.801Z -> 3h 20m 13s (UTC time) or 10h 20m 13s in GMT+7 time
        :param rfc_time:
        :param fmt
        :return:
        """
        utc_dt = datetime.strptime(rfc_time, fmt)

        # Convert UTC datetime to seconds since the
        timestamp = (utc_dt - datetime(1970, 1, 1)).total_seconds()
        return int(timestamp)

    @staticmethod
    def format_timestamp(timestamp, unit='second'):
        """
        Convert timestamp in second (or millisecond) to human readable time
        Example: timestamp = 3661, unit = second -> Readable time = 1h 1m 1s
        """
        if timestamp == 'N/A':
            return timestamp

        seconds = timestamp
        if unit == 'millisecond':  # timestamp in millisecond
            seconds = int(timestamp / 1000)
        days = int(seconds / (24 * 3600))
        tmp = seconds - days * 24 * 3600
        hours = int(tmp / 3600)
        tmp = seconds - days * 24 * 3600 - hours * 3600
        minutes = int(tmp / 60)
        seconds = seconds - days * 24 * 3600 - hours * 3600 - minutes * 60

        result = "0"
        if days > 0:
            result = str(days) + " ngày " + str(hours) + " giờ " + str(minutes) + " phút " + str(seconds) + " giây"
        elif hours > 0:
            result = str(hours) + " giờ " + str(minutes) + " phút " + str(seconds) + " giây"
        elif minutes > 0:
            result = str(minutes) + " phút " + str(seconds) + " giây"
        elif seconds > 0:
            result = str(seconds) + " giây"
        return result
