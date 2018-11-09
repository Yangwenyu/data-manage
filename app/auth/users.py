from flask import request, Flask, render_template, jsonify
from app.models import *
from app.auth import auth


@auth.route('/login/', methods=['GET', 'POST'])
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