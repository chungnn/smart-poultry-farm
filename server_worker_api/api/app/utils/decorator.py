# -*- coding: utf-8 -*-

from functools import wraps
from flask_jwt_extended import  verify_jwt_in_request, get_jwt_claims, get_jwt_identity
from utils_func import get_permissions, add_new_permission, check_permission_existed
from ..exception import BadRequest


def check_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO : update code for check permission
            verify_jwt_in_request()
            user_info = get_jwt_claims()
            username = get_jwt_identity()
            lst_roles = user_info['roles']
            lst_permission = get_permissions(lst_roles)
            if permission not in lst_permission:
                if not check_permission_existed(permission):
                    add_new_permission(permission)
                raise BadRequest(1009)
            return func(*args, **kwargs)
        return wrapper
    return decorator




