from app import db


# 远行星号的舰船数据表
class Data_starsector(db.Model):
    __tablename__ = 'data_starsector'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)    # 名称
    shipclass = db.Column(db.String(30), nullable=False)    # 名称
    force = db.Column(db.String(30), nullable=False)    # 所属势力
    pic_address = db.Column(db.String(100), nullable=False)    # 名称
    listorder = db.Column(db.Integer, nullable=False, default='0', index=True)    # 排序id
