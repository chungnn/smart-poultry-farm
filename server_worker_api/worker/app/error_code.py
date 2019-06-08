__author__ = 'huydq17'
# -*- coding: utf-8 -*-

HTTP_STATUS_CODES = {
    100:    'Continue.',
    101:    'Switching Protocols.',
    102:    'Processing.',
    200:    'OK.',
    201:    'Created.',
    202:    'Accepted.',
    203:    'Non Authoritative Information.',
    204:    'No Content.',
    205:    'Reset Content.',
    206:    'Partial Content.',
    207:    'Multi Status.',
    226:    'IM Used.',              # see RFC 3229
    300:    'Multiple Choices.',
    301:    'Moved Permanently.',
    302:    'Found.',
    303:    'See Other.',
    304:    'Not Modified.',
    305:    'Use Proxy.',
    307:    'Temporary Redirect.',
    400:    'Bad Request.',
    401:    'Unauthorized.',
    402:    'Payment Required.',     # unused
    403:    'Forbidden.',
    404:    'Not Found.',
    405:    'Method Not Allowed.',
    406:    'Not Acceptable.',
    407:    'Proxy Authentication Required.',
    408:    'Request Timeout.',
    409:    'Conflict.',
    410:    'Gone.',
    411:    'Length Required.',
    412:    'Precondition Failed.',
    413:    'Request Entity Too Large.',
    414:    'Request URI Too Long.',
    415:    'Unsupported Media Type.',
    416:    'Requested Range Not Satisfiable.',
    417:    'Expectation Failed.',
    418:    'I\'m a teapot.',        # see RFC 2324
    422:    'Unprocessable Entity.',
    423:    'Locked.',
    424:    'Failed Dependency.',
    426:    'Upgrade Required.',
    428:    'Precondition Required.',   # see RFC 6585
    429:    'Too Many Requests.',
    431:    'Request Header Fields Too Large.',
    449:    'Retry With.',           # proprietary MS extension
    500:    'Internal Server Error.',
    501:    'Not Implemented.',
    502:    'Bad Gateway.',
    503:    'Service Unavailable.',
    504:    'Gateway Timeout.',
    505:    'HTTP Version Not Supported.',
    507:    'Insufficient Storage.',
    510:    'Not Extended.'
}
HTTP_100_CONTINUE = {
}
HTTP_101_SWITCHING_PROTOCOLS = {
}
HTTP_200_OK = {
}
HTTP_201_CREATED = {
}
HTTP_202_ACCEPTED = {
}
HTTP_203_NON_AUTHORITATIVE_INFORMATION = {
}
HTTP_204_NO_CONTENT = {
}
HTTP_205_RESET_CONTENT = {
}
HTTP_206_PARTIAL_CONTENT = {
}
HTTP_300_MULTIPLE_CHOICES = {
}
HTTP_301_MOVED_PERMANENTLY = {
}
HTTP_302_FOUND = {
}
HTTP_303_SEE_OTHER = {
}
HTTP_304_NOT_MODIFIED = {
}
HTTP_305_USE_PROXY = {
}
HTTP_306_RESERVED = {
}
HTTP_307_TEMPORARY_REDIRECT = {
}
HTTP_400_BAD_REQUEST = {
    1001: 'Not login!',
    1002: 'Content-Type in request header is not \'application/json\'!',
    1003: 'Missing field in request!',
    1004: ''
}
HTTP_401_UNAUTHORIZED = {
    2000: ''
}
HTTP_402_PAYMENT_REQUIRED = {
    3000: ''
}
HTTP_403_FORBIDDEN = {
    4000: 'Access denied!'
}
HTTP_404_NOT_FOUND = {
}
HTTP_405_METHOD_NOT_ALLOWED = {
}
HTTP_406_NOT_ACCEPTABLE = {
}
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = {
}
HTTP_408_REQUEST_TIMEOUT = {
}
HTTP_409_CONFLICT = {
}
HTTP_410_GONE = {
}
HTTP_411_LENGTH_REQUIRED = {
}
HTTP_412_PRECONDITION_FAILED = {
}
HTTP_413_REQUEST_ENTITY_TOO_LARGE = {
}
HTTP_414_REQUEST_URI_TOO_LONG = {
}
HTTP_415_UNSUPPORTED_MEDIA_TYPE = {
}
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = {
}
HTTP_417_EXPECTATION_FAILED = {
}
HTTP_422_UNPROCESSABLE_ENTITY = {
    42201: 'Rule name: {0} already exists',
    42202: 'Metadata: {0} - {1} already exists',
    42203: 'Language: {0} already exists'
}
HTTP_428_PRECONDITION_REQUIRED = {
}
HTTP_429_TOO_MANY_REQUESTS = {
}
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = {
}
HTTP_500_INTERNAL_SERVER_ERROR = {
}
HTTP_501_NOT_IMPLEMENTED = {
}
HTTP_502_BAD_GATEWAY = {
}
HTTP_503_SERVICE_UNAVAILABLE = {
}
HTTP_504_GATEWAY_TIMEOUT = {
}
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = {
}
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = {
}