# -*- coding: utf-8 -*-
from flask import render_template, session, redirect, url_for, request

from . import main
from .forms import PostForm
from .. import db
from ..models import User
from flask_login import login_required, current_user
from ..decorators import admin_required
from ..models import Permission, Post


@main.route('/', methods=['get', 'post'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=1, error_out=False)
    posts = pagination.items
    return render_template('index.html', pagination=pagination, posts=posts, form=form)
