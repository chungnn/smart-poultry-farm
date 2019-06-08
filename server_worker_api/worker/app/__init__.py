# -*- coding: utf-8 -*-
import imp

DEFAULT_FILE_NAME = 'app/config.py'
DEFAULT_CLASS_NAME = 'ChickenFarmConfig'
DEFAULT_GLOBAL_CONFIG_FILE = ''


def load_module(filename):
    """
    load module from python file
    :param filename:
    :return:
    """
    mod = imp.new_module('config')
    mod.__file__ = filename
    try:
        with open(filename) as config_file:
            exec (compile(config_file.read(), filename, 'exec'), mod.__dict__)
    except Exception as e:
        raise e
    return mod