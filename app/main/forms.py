#-*- coding=utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField,PasswordField,SelectField
from wtforms.validators import Required, length, Regexp
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class LoginForm(Form):
    username = StringField(u'账号', validators=[Required(), length(1, 64)])
    password = PasswordField(u'密码', validators=[Required()])
    submit = SubmitField(u'登入')

class AddComRecordForm(Form):
    """
    用户提交维修记录的表单
    """
    user = StringField(u'* 物主姓名:', validators=[Required(), length(2, 5, message=u'姓名只允许2-5个字符！')])
    phone = StringField(u'* 手机号:', validators=[Required(), length(6, 11, message=u'只允许6-11位数字'), Regexp('[0-9]')])
    problem = TextAreaField(u'* 简要描述您的问题:', validators=[Required()])
    computer_type = StringField(u'* 您的电脑型号:', validators=[Required()])
    computer_password = StringField(u'您的电脑密码（可不填）:')
    submit = SubmitField(u'提交')

class AddEleRecordForm(Form):
    """
    用户提交维修记录的表单
    """
    user = StringField(u'* 物主姓名:', validators=[Required(), length(2, 5, message=u'姓名只允许2-5个字符！')])
    phone = StringField(u'* 手机号:', validators=[Required(), length(6, 11, message=u'只允许6-11位数字'), Regexp('[0-9]')])
    problem = TextAreaField(u'* 简要描述您的问题:', validators=[Required()])
    ele_type = StringField(u'* 您的电器类型:', validators=[Required()])
    submit = SubmitField(u'提交')


class GetRandomIdForm(Form):
    """
    序号相关的表单
    """
    random_id = StringField(u'请输入您的序列号：', validators=[Required()])
    submit = SubmitField(u'确认取回')

class AddCommentForm(Form):

    comment = TextAreaField(u'* 填写你的表白:', validators=[Required(),length(1, 64)])
    submit = SubmitField(u'提交')

class ArrangeForm(Form):
    arrange11= SelectField(u'第一意愿', choices=[ ('0',u'未选择'),
                                                 ('1',u'星期一'),
                                                 ('2',u'星期二'),
                                                 ('3',u'星期三'),
                                                 ('4',u'星期四'),
                                                 ('5',u'星期五'),
                                                 ('6',u'星期六'),
                                                 ('7',u'星期日')
                                                ])
    arrange12= SelectField(u'',choices=[('0',u'未选择'),('1',u'第一班'),('2',u'第二班'),('3',u'第三班')])
    arrange21= SelectField(u'第二意愿', choices=[ ('0',u'未选择'),
                                                 ('1',u'星期一'),
                                                 ('2',u'星期二'),
                                                 ('3',u'星期三'),
                                                 ('4',u'星期四'),
                                                 ('5',u'星期五'),
                                                 ('6',u'星期六'),
                                                 ('7',u'星期日')
                                                ])
    arrange22= SelectField(u'',choices=[('0',u'未选择'),('1',u'第一班'),('2',u'第二班'),('3',u'第三班')])
    arrange31= SelectField(u'第三意愿', choices=[ ('0',u'未选择'),
                                                 ('1',u'星期一'),
                                                 ('2',u'星期二'),
                                                 ('3',u'星期三'),
                                                 ('4',u'星期四'),
                                                 ('5',u'星期五'),
                                                 ('6',u'星期六'),
                                                 ('7',u'星期日')
                                                ])
    arrange32= SelectField(u'',choices=[('0',u'未选择'),('1',u'第一班'),('2',u'第二班'),('3',u'第三班')])
    arrange41= SelectField(u'第四意愿', choices=[ ('0',u'未选择'),
                                                 ('1',u'星期一'),
                                                 ('2',u'星期二'),
                                                 ('3',u'星期三'),
                                                 ('4',u'星期四'),
                                                 ('5',u'星期五'),
                                                 ('6',u'星期六'),
                                                 ('7',u'星期日')
                                                ])
    arrange42= SelectField(u'',choices=[('0',u'未选择'),('1',u'第一班'),('2',u'第二班'),('3',u'第三班')])
    submit=SubmitField(u'提交')


class doarrangeForm(Form):
    arrangeGroup=SelectField(u'选择要进行排班的两届成员')