# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 定义表单字段
class NameForm(Form):
    name = StringField(u'用户名', validators=[DataRequired()])
    submit = SubmitField(u'提交')
