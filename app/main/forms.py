# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


# 定义表单字段
class NameForm(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class PostForm(FlaskForm):
    body = TextAreaField(u'正文', validators=[DataRequired()])
    submit = SubmitField(u'提交')