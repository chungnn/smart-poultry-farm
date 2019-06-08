# -*- coding: utf-8 -*-
from ..db.mongo import MongoWrapper
from ..extensions import mongo
from ..exception import NotFound
from ..api import gen_id


def get_permissions(roles):
    """
    get all permission in roles
    :param roles:
    :return:
    """
    roles_collection = MongoWrapper(mongo, 'role')
    spec = {'role_name': {'$in': list(roles)}}
    cursor = roles_collection.find(spec)
    lst_perm = []
    for role in cursor:
        lst_perm.extend(role['permission'])
    return lst_perm


def add_new_permission(permission):
    """
    add new permission 
    :param permission: 
    :return: 
    """
    perm_collection = MongoWrapper(mongo, 'permission')
    _id = gen_id('permission')
    description = 'This is permission of system'
    new_perm = {'_id': _id, 'permission_name': permission, 'description': description}
    perm_collection.insert(**new_perm)


def check_permission_existed(perm):
    """

    :param perm:
    :return:
    """
    perm_collection = MongoWrapper(mongo, 'permission')
    datas = perm_collection.find({'permission_name': perm})
    if datas.count() > 0:
        return True
    return False
