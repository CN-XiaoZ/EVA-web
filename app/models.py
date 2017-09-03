# -*- coding=utf-8 -*-

from . import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash  # 引入密码加密 验证方法
from flask_login import UserMixin  # 引入flask-login用户模型继承类方法
from sqlalchemy.sql import func


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DATETIME)
    random_id = db.Column(db.Integer, unique=True)
    user = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    problem = db.Column(db.Text)
    computer_type = db.Column(db.String(64))
    computer_password = db.Column(db.String(64))
    split = db.Column(db.Boolean, default=False)
    solve = db.Column(db.Boolean, default=False)
    mender = db.Column(db.String(64), default='')
    verify = db.Column(db.Boolean, default=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Erecord(db.Model):
    __tablename__ = 'erecord'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DATETIME)
    random_id = db.Column(db.Integer, unique=True)
    user = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    problem = db.Column(db.Text)
    ele_type = db.Column(db.String(64))
    solve = db.Column(db.Boolean, default=False)
    mender = db.Column(db.String(64), default='')
    verify = db.Column(db.Boolean, default=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Unid(db.Model):
    _tablename_='unid'
    id = db.Column(db.Integer, primary_key=True)
    random_id = db.Column(db.Integer, unique=True)

class User(UserMixin, db.Model):
    # 在使用Flask-Login作为登入功能�?在user模型要继承UserMimix�?
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    tel=db.Column(db.String(64))
    arrangewant=db.Column(db.String(64))
    arrange=db.Column(db.String(64))
    premission=db.Column(db.Integer)
    group=db.Column(db.Integer)
    grade=db.Column(db.Integer)
    exam=db.Column(db.Text)
    time=db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    # real_name = db.Column(db.String(64), unique=True)
    # record = db.relationship('Record', backref='user')

    @property
    def password(self):
        raise AttributeError(u'不是可获取信息')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # 增加password会通过generate_password_hash方法来加密储�?

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        # 在登入时,我们需要验证明文密码是否和加密密码所吻合

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DATETIME)
    comment = db.Column(db.Text)
    verify = db.Column(db.Boolean, default=False)

from markdown import markdown
import bleach
class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    create_time = db.Column(db.DATETIME, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p','img']
        attrs = {
            'img': ['src', 'alt']
        }
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True, attributes=attrs))

db.event.listen(Article.body, 'set', Article.on_changed_body)

class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    articles = db.relationship('Article', backref='category')


#以下是内部管理部分的

class Arrange(db.Model):
    __tablename__='arrange'
    card_id=db.Column(db.String(64),primary_key=True)
    name=db.Column(db.String(64))
    arrange=db.Column(db.String(64))
    term=db.Column(db.Integer)

class Exam(db.Model):
    __tablename__ = 'exam'
    Qid = db.Column(db.Integer, primary_key=True)
    Stem = db.Column(db.Text)
    Select_1 = db.Column(db.Text)
    Select_2 = db.Column(db.Text)
    Select_3 = db.Column(db.Text)
    Select_4 = db.Column(db.Text)
    Select_Right = db.Column(db.Integer)
    lv = db.Column(db.Integer)

class Marks_record(db.Model):
   __tablename__ = 'marks_record'
   id = db.Column(db.Integer, primary_key=True,autoincrement=True)
   username=db.Column(db.String(64))
   time=db.Column(db.DATETIME,default=datetime.utcnow())
   Q_ID=db.Column(db.Integer)
   Select=db.Column(db.String(64))
   mark=db.Column(db.String(64))

class Finance(db.Model):
    __tablename__ = 'finance'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    pm=db.Column(db.Integer)
    num = db.Column(db.Integer)
    tip = db.Column(db.Text)
    remain = db.Column(db.Integer)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
