from app import db
from datetime import datetime


# 保险列表数据
class Bx_list(db.Model):
    __tablename__ = 'bx_list'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    bxname = db.Column(db.String(30), nullable=False)    # 保险名称
    introduction = db.Column(db.Text, nullable=False, default='')    # 保险简介
    company = db.Column(db.String(50), nullable=False)    # 所属保险公司
    coverage = db.Column(db.String(30), nullable=False, default='0')    # 保额
    url = db.Column(db.String(300), nullable=False)    # 网址
    create_time = db.Column(db.DateTime, default=datetime.now())


# 保险关键字
class Bx_keys(db.Model):
    __tablename__ = 'bx_keys'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keyword = db.Column(db.String(20), nullable=False, default='')    # 关键词
    bx_id = db.Column(db.Integer, db.ForeignKey('bx_list.id'))

    bx = db.relationship('Bx_list', backref=db.backref('bx_keys'))    # 外键
