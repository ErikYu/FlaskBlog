# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask.ext.pagedown.fields import PageDownField


# 定义表单字段
class NameForm(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class PostForm(FlaskForm):
    body = PageDownField(u'正文', validators=[DataRequired()])
    submit = SubmitField(u'提交')