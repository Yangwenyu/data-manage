from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import config
# from models import User, Question, Answer
from models import Auth_admin, Auth_rule, Data_starsector
from exts import db
from decorators import login_required
from sqlalchemy import or_
from datetime import timedelta
import json
import datetime


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# 主页视图
@app.route('/')
@login_required
def index():
    return render_template('index.html')


# 登录视图
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('page-login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = Auth_admin.query.filter(username == username, password == password).first()
        if user and user.check_password(password):
            session['user_name'] = user.username
            # session 保存时间
            session.permanent = True
            app.permanent_session_lifetime = timedelta(hours=12)
            return redirect(url_for('index'))
        else:
            return render_template('page-login.html', message='账号和密码错误，请重新再试！')


# 退出登录
@app.route('/logout/')
def logout():
    session.pop('user_name')
    return redirect(url_for('login'))






@app.route('/auth-admin/')
def auth_admin():
    return render_template('auth-admin.html')


@app.route('/auth-admin/register/', methods=['GET', 'POST'])
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
            return redirect(url_for('auth_admin'))


@app.route('/gamedata-starsecor/')
def gamedata_starsector():
    context = {
        'starsectors': Data_starsector.query.order_by('listorder').all()
    }
    c = context
    return json.dumps(c, cls=AlchemyEncoder)
    # return render_template('gamedata-starsector.html', **context)


@app.route('/gamedata-starsecor/detail/<ship_id>')
def starsector_ship_detail(ship_id):
    starsector_ship = Data_starsector.query.filter(Data_starsector.id == ship_id).first()
    return render_template('gamedata-starsector.html', starsector_ship=starsector_ship)


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
