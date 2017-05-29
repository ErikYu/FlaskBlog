# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录')
    submit = SubmitField(u'登陆')


class RegistrationForm(FlaskForm):
    email = StringField(u'注册邮箱', validators=[DataRequired(), Email(), Length(1, 64)])
    username = StringField(u'用户名', validators=[DataRequired(), Length(1, 64), Regexp('^[a-zA-Z]*$', 0, u'用户名格式')])
    password = PasswordField(u'请输入密码', validators=[DataRequired(), EqualTo('password2', message=u'两次密码输入必须一致')])
    password2 = PasswordField(u'再输入一次', validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已经被注册')

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError(u'用户名已被注册')