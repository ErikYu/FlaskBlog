# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, request, flash
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required
from .. import db


@auth.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'邮箱/密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'已登出')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['get', 'post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        flash(u'你现在可以登录了')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
