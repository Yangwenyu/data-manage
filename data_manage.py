from flask import Flask, render_template, request, redirect, url_for, session, g
import config
# from models import User, Question, Answer
from exts import db
# from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    return render_template('page-login.html')


if __name__ == '__main__':
    app.run()
