# -*- coding: utf-8 -*-
# 创建蓝本
from flask import Blueprint

main = Blueprint('main', __name__)
# 以下导入在main定义之后导入
from . import views, errors
