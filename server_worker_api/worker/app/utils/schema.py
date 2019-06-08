# -*- coding: utf-8 -*-
from marshmallow import fields, Schema


class Setting(Schema):
    hour = fields.Integer(required=True)
    minute = fields.Integer(required=True)
    duration = fields.Integer(required=True)
