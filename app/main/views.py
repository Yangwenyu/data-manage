import os
import json
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, g, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import timedelta
from app import db
# from models import User, Question, Answer
from . import main
from .decorators import login_required
from ..models import users, gamedata, bx
# from app.models import Auth_admin, Auth_rule, Data_starsector


# db = SQLAlchemy()
# app = Flask(__name__)
# app.config.from_object(config)
# db.init_app(app)


# 边栏菜单
@main.route('/sidemenu/', methods=['GET'])
def sidemenu():
    sidemenu = []
    all_topname = db.session.execute("select distinct a.`name`, a.id from auth_rule as a "
                                     "where a.pid = 0 and a.status = 1 ORDER BY a.listorder").fetchall()
    for one_top in all_topname:
        sql_text = "select b.id, a.`name` as topname, b.`name`, b.rule, b.pagetitle, b.pagedesc, " \
                   "b.auth_check, b.only_root from auth_rule as a LEFT JOIN auth_rule as b " \
                   "on a.id = b.pid where b.status = 1 and b.pid = " + str(one_top[1]) + " ORDER BY b.listorder"
        secondary_rules = db.session.execute(sql_text).fetchall()
        all_ciji_rules = []
        ciji_rule = {}
        for one_rule in secondary_rules:
            ciji_rule['id'] = one_rule[0]
            ciji_rule['topname'] = one_rule[1]
            ciji_rule['name'] = one_rule[2]
            ciji_rule['rule'] = one_rule[3]
            ciji_rule['pagetitle'] = one_rule[4]
            ciji_rule['pagedesc'] = one_rule[5]
            ciji_rule['auth_check'] = one_rule[6]
            ciji_rule['only_root'] = one_rule[7]
            all_ciji_rules.append(ciji_rule)
        result = {'topname': one_top[0], 'ciji_rule': all_ciji_rules}
        sidemenu.append(result)
    return json.dumps({'sidemenu': sidemenu})


# 主页视图
@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')


# 登录视图
@main.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('page-login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.Auth_admin.query.filter(username == username, password == password).first()
        if user and user.check_password(password):
            session['user_name'] = user.username
            # session 保存时间
            session.permanent = True
            main.permanent_session_lifetime = timedelta(hours=12)
            return redirect(url_for('main.index'))
        else:
            return render_template('page-login.html', message='账号和密码错误，请重新再试！')


# 退出登录
@main.route('/logout/')
def logout():
    session.pop('user_name')
    return redirect(url_for('main.login'))






@main.route('/auth-admin/')
def auth_admin():
    return render_template('auth-admin.html')


@main.route('/auth-admin/register/', methods=['GET', 'POST'])
def auth_admin_register():
    if request.method == 'GET':
        return render_template('auth-admin.html')
    else:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        gender = request.values.get('gender')
        # 手机号验证
        email_check = Auth_admin.query.filter(Auth_admin.email == email).first()
        if email_check:
            return render_template('auth-admin.html', message='该邮箱已注册，请换一个邮箱！')
        else:
            auth_admin = Auth_admin(email=email, username=username, password=password, gender=gender)
            db.session.add(auth_admin)
            db.session.commit()
            # # 如果注册成功，跳转登录页面
            return redirect(url_for('main.auth_admin'))


@main.route('/api/gamedata-starsecor/')
def api_gamedata_starsector():
    context = {
        'starsectors': gamedata.Data_starsector.query.order_by('listorder').all()
    }
    c = context
    return json.dumps(c, cls=AlchemyEncoder)
    # return render_template('gamedata-starsector.html', **context)

@main.route('/gamedata-starsecor/')
def gamedata_starsector():
    return render_template('gamedata-starsector.html')


@main.route('/gamedata-starsecor/detail/<ship_id>')
def starsector_ship_detail(ship_id):
    starsector_ship = main.Data_starsector.query.filter(Data_starsector.id == ship_id).first()
    return render_template('gamedata-starsector.html', starsector_ship=starsector_ship)


@main.route('/bx-list/')
def bx_list():

    return render_template('bx/bx-list.html')



# 蜘蛛纸牌
@main.route('/spider-solitaire/')
def spider_solitaire():
    return render_template('game/spider-solitaire.html')





# 转换成json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    app.run()
