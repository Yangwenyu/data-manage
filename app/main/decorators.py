from functools import wraps
from flask import redirect, url_for, session


# 登陆限制的函数
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_name'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('main.login'))
    return wrapper
