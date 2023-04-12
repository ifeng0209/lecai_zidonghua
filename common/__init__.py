#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'superfeng'

import settings
from .logger_handler import get_logger
from .db_handler import DB

logger = get_logger(**settings.LOG_CONFIG)

db = DB(settings.DB_ELEPHANT_CONFIG)
