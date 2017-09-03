#-*- coding=utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, session, make_response
from . import main
from flask_login import login_required, current_user, login_user, logout_user
from .forms import LoginForm,AddCommentForm,AddComRecordForm, GetRandomIdForm,AddEleRecordForm
from ..models import Record,Erecord,Unid,Comment,Article,Category,User
from .. import db
from datetime import datetime
import random
import string
from functools import wraps
import sys

def Public(func):#公用账号 权限号为2017
    @wraps(func)
    def ADMIN(*args, **kwargs):
        PER = User.query.filter_by(name=session.get('name')).first()
        if PER.permission==2017:
            return func(*args, **kwargs)
        else:
            flash(u'你不是管理员')
            return redirect(url_for('main.index'))
    return ADMIN

def Admin(func):#管理员账号 权限号为2008
    @wraps(func)
    def ADMIN(*args, **kwargs):
        PER = User.query.filter_by(name=session.get('name')).first()
        if PER.permission==2008:
            return func(*args, **kwargs)
        else:
            flash(u'你不是管理员')
            return redirect(url_for('main.index'))
    return ADMIN

def Su(func):#超级管理员账号 权限号为1984
    @wraps(func)
    def ADMIN(*args, **kwargs):
        PER = User.query.filter_by(name=session.get('name')).first()
        if PER.permission==1984:
            return func(*args, **kwargs)
        else:
            flash(u'你不是管理员')
            return redirect(url_for('main.index'))
    return ADMIN


@main.route('/')
def index():
    clist = Category.query.all()
    alist = Article.query.all()
    return render_template('main/index.html',clist=clist,alist=alist)


@main.route('/user/amend', methods=['GET', 'POST'])
def user_amend():
    """
    用户添加维修记录
    :return:
    """
    dayOfWeek = datetime.today().weekday()
    type = request.args.get('type')
    if type == '2':
        form = AddEleRecordForm()
    else:
        form = AddComRecordForm()
    # alist = Record.query.all()
    if form.validate_on_submit():
        unid = Unid(random_id = string.join(
            random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 5)).replace(' ', ''))
        try:
            db.session.add(unid)
            db.session.commit()
        except:
            db.session.rollback()
            flash(u'随机码生成失败')
        if type == '2':
            erecord = Erecord(user=form.user.data, phone=form.phone.data, problem=form.problem.data,
                              create_time=datetime.now(), ele_type=form.ele_type.data, random_id=unid.random_id)
        else:
            record = Record(user=form.user.data, phone=form.phone.data, problem=form.problem.data,
                            create_time=datetime.now(),
                            computer_type=form.computer_type.data, computer_password=form.computer_password.data,
                            random_id=unid.random_id)
        i = 1
        while(i):
            try:
                if type == '2':
                    db.session.add(erecord)
                    db.session.commit()
                    flash(u'记录添加成功,您的随机码是 %s, 请务必截图保存' % erecord.random_id)
                else:
                    db.session.add(record)
                    db.session.commit()
                    flash(u'记录添加成功,您的随机码是 %s, 请务必截图保存' % record.random_id)
                i = 0
                return redirect(url_for('main.user_verify', random_id=unid.random_id))
            except:
                db.session.rollback()
    return render_template('main/amend.html', form=form)


@main.route('/user/verify/<int:random_id>', methods=['GET', 'POST'])
def user_verify(random_id):
    """
    用户确认物品取回
    :return:
    """
    form = GetRandomIdForm(random_id=random_id)
    if form.validate_on_submit():
        random_id = form.random_id.data
        record = Record.query.filter(Record.random_id == random_id).first()
        if record is None:
            erecord = Erecord.query.filter(Erecord.random_id == random_id).first()
            erecord.verify = True
            db.session.add(erecord)
            db.session.commit()
            flash(u'已确认取回')
        else:
            try:
                record.verify = True
                db.session.add(record)
                db.session.commit()
                flash(u'已确认取回')
            except:
                db.session.rollback()
                flash(u'未知错误')
        return redirect(url_for('main.user_amend'))
    return render_template('main/verify.html', form=form)


@main.route('/user/verify', methods=['GET', 'POST'])
def user_Verify():
    """
    用户确认物品取回
    :return:
    """
    form = GetRandomIdForm()
    if form.validate_on_submit():
        random_id = form.random_id.data
        record = Record.query.filter(Record.random_id == random_id).first()
        if record is None:
            erecord = Erecord.query.filter(Erecord.random_id == random_id).first()
            erecord.verify = True
            db.session.add(erecord)
            db.session.commit()
            flash(u'已确认取回')
        else:
            try:
                record.verify = True
                db.session.add(record)
                db.session.commit()
                flash(u'已确认取回')
            except:
                db.session.rollback()
                flash(u'未知错误')
        return redirect(url_for('main.user_amend'))
    return render_template('main/verify.html', form=form)

@main.route('/comment', methods=['GET', 'POST'])
def comment():
    form = AddCommentForm()
    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data,create_time=datetime.now())
        i = 1
        while(i):
            try:
                db.session.add(comment)
                db.session.commit()
                flash(u'评论提交成功')
                i = 0
                return redirect(url_for('main.index'))
            except:
                db.session.rollback()
    return render_template('main/comment.html', form=form)

@main.route('/Innerlogin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.username.data
        user = User.query.filter_by(name=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.innerindex'))
        flash(u'用户密码不正确')
    return render_template('main/login.html', form=form)

@main.route('/inner', methods=['GET'])
def innerIndex():
    return render_template('main/innerindex.html')

@main.route('/read/', methods=['GET'])
def read():
    a = Article.query.filter_by(id=request.args.get('id')).first()
    if a is not None:
        return render_template('main/read.html', a=a)
    flash(u'未找到相关文章')
    return redirect(url_for('main.index'))

