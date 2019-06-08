# -*- coding: utf-8 -*-
from flask import current_app, jsonify
from werkzeug.exceptions import HTTPException
from http_code import HTTP_STATUS_CODES
from error_code import *


def http_status_message(status_code):
    """Maps an HTTP status code to the textual status"""

    return HTTP_STATUS_CODES.get(status_code, '')


def get_error_message(data):
    """Using for extract log from marshmallow validation

    Args:
        data (dict): Dictionnary contain marshmallow validation result

    Returns:
        str/unicode: Message

    Example data:
    {
        'messages': {
            'info': {
                'rule_name': ['test server endpoint is exsited.']
            }
        },
        'exc': ValidationError({
            'info': {
                'rule_name': ['test server endpoint is exsited.']
            }
        }, status_code = 422, headers = {})
    }
    """
    try:
        messages = data['messages']
        for k, v in messages.items():
            if isinstance(v, dict):
                for ik, iv in v.items():
                    if isinstance(iv, list) and iv:
                        return iv[0]
                    elif isinstance(iv, str) or isinstance(iv, unicode):
                        return iv
            elif isinstance(v, str) or isinstance(v, unicode):
                return v
            else:
                return 'Validation error, re-check your data.'
    except Exception:
        return 'Validation error, re-check your data.'


def error_data(error_code, message):
    """Constructs a dictionary with status and message for returning in an
    error response"""

    error = {
        'code': error_code,
        'message': message
    }
    return error


class APIException(Exception):

    """The base exception class for all exceptions this library raises."""

    status_code = 500
    http_status_code = HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, error_code=None, *args):
        if error_code in self.http_status_code:
            self.error_code = error_code
        else:
            self.error_code = self.status_code
        message = self.http_status_code.get(
            error_code, http_status_message(self.status_code))
        self.message = message.format(*args)

    @property
    def description(self):
        return error_data(self.error_code, self.message)


class BadRequest(APIException):

    """HTTP 400 - Bad request: you sent some malformed data."""

    status_code = 400
    http_status_code = HTTP_400_BAD_REQUEST


class Unauthorized(APIException):

    """HTTP 401 - Unauthorized: bad credentials."""

    status_code = 401
    http_status_code = HTTP_401_UNAUTHORIZED


class Forbidden(APIException):

    """HTTP 403 - Forbidden: your credentials don't give you access to this resource."""

    status_code = 403
    http_status_code = HTTP_403_FORBIDDEN


class NotFound(APIException):

    """HTTP 404 - Not found."""

    status_code = 404
    http_status_code = HTTP_404_NOT_FOUND


class MethodNotAllowed(APIException):

    """HTTP 405 - Method Not Allowed."""

    status_code = 405
    http_status_code = HTTP_405_METHOD_NOT_ALLOWED


class NotAcceptable(APIException):

    """HTTP 406 - Not Acceptable."""

    status_code = 406
    http_status_code = HTTP_406_NOT_ACCEPTABLE


class Conflict(APIException):

    """HTTP 409 - Conflict."""

    status_code = 409
    http_status_code = HTTP_409_CONFLICT


class OverLimit(APIException):

    """HTTP 413 - Over limit: you're over the API limits for this time period."""

    status_code = 413
    http_status_code = HTTP_413_REQUEST_ENTITY_TOO_LARGE


class UnsupportedMediaType(APIException):

    """HTTP 415 - Unsupported Media Type: Unsupported media type in the request Content-Type header."""

    status_code = 415
    http_status_code = HTTP_415_UNSUPPORTED_MEDIA_TYPE


class UnprocessableEntity(APIException):

    """HTTP 429 - Unprocessable Entity: The request was well-formed but was unable to be followed due to semantic errors."""

    status_code = 422
    http_status_code = HTTP_422_UNPROCESSABLE_ENTITY


class RateLimit(APIException):

    """HTTP 429 - Rate limit: you've sent too many requests for this time period."""

    status_code = 429
    http_status_code = HTTP_429_TOO_MANY_REQUESTS


def api_error_handler(error):
    if isinstance(error, HTTPException):
        code = error.code
        if not isinstance(error.description, dict):
            if code == 422:
                # credits to vinhnt30
                data = getattr(error, 'data')
                error.description = error_data(code, get_error_message(data))
            else:
                error.description = error_data(code, http_status_message(code))
    elif isinstance(error, APIException):
        code = error.status_code
    else:
        code = 500
        error.description = error_data(code, http_status_message(code))
    msg = 'HTTP_STATUS_CODE_{0}: {1}'.format(code, error.description)
    if code != 404:
        current_app.logger.error(msg, exc_info=error)
    return jsonify(error=error.description), code
