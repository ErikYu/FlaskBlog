# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_script import Manager, Shell

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
app.config['SECRET_KEY'] = 'hard to guess string'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# 定义表单字段
class NameForm(Form):
    name = StringField(u'用户名', validators=[DataRequired()])
    submit = SubmitField(u'提交')


@app.route('/', methods=['get', 'post'])
def hello_world():
    form = NameForm()
    return render_template('index.html', form=form)


# 定义模型
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role %r' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
