from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


# 用户表
class Auth_admin(db.Model):
    __tablename__ = 'auth_admin'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False, unique=True)    # 邮箱
    username = db.Column(db.String(20), nullable=False, unique=True)    # 用户名
    password = db.Column(db.String(100), nullable=False)    # 密码
    rules = db.Column(db.Text, nullable=False, default='')    # 用户规则
    status = db.Column(db.Boolean, nullable=False, default='1')  # 账号状态
    remark = db.Column(db.String(255), nullable=False, default='')  # 备注信息
    login_time = db.Column(db.Integer, nullable=False, default='0')  # 最近登录时间
    login_ip = db.Column(db.String(15), nullable=False, default='')  # 最近登录IP

    def __init__(self, *args, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result


# 规则表
class Auth_rule(db.Model):
    __tablename__ = 'auth_rule'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    pid = db.Column(db.Integer, nullable=False, default='0', index=True)    # 上级id
    name = db.Column(db.String(30), nullable=False)    # 名称
    rule = db.Column(db.String(100), nullable=False, default='', index=True)    # 规则
    auth_check = db.Column(db.Boolean, nullable=False, default='1')  # 是否进行权限验证
    only_root = db.Column(db.Boolean, nullable=False, default='0')  # 仅开发者权限
    status = db.Column(db.Boolean, nullable=False, default='1')  # 状态
    listorder = db.Column(db.Integer, nullable=False, default='0')  # 排序












# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     telephone = db.Column(db.String(11), nullable=False)
#     username = db.Column(db.String(11), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#
#     def __init__(self, *args, **kwargs):
#         telephone = kwargs.get('telephone')
#         username = kwargs.get('username')
#         password = kwargs.get('password')
#
#         self.telephone = telephone
#         self.username = username
#         self.password = generate_password_hash(password)
#
#     def check_password(self, raw_password):
#         result = check_password_hash(self.password, raw_password)
#         return result
#
#
# class Question(db.Model):
#     __tablename__ = 'question'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     create_time = db.Column(db.DateTime, default=datetime.now())
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     author = db.relationship('User', backref=db.backref('questions'))
#
#
# class Answer(db.Model):
#     __tablename__ = 'answer'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     content = db.Column(db.Text, nullable=False)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     create_time = db.Column(db.DateTime, default=datetime.now())
#
#     question = db.relationship('Question', backref=db.backref('answers', order_by=id.desc()))
#     author = db.relationship('User', backref=db.backref('answers'))
