import json
from flask import request, jsonify
from app.models import *
from app.api import api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from .common import AlchemyEncoder
from ..models import users, gamedata, bx


@api.route('/bx-list', methods=['GET', 'POST'])
def bx_list():
    context = {
        'bx_list': bx.Bx_list.query.all()
    }
    c = context
    return json.dumps(c, cls=AlchemyEncoder)
