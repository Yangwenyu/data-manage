import json
from flask import request, jsonify, render_template
from app.models import *
from app.api import api
from ..models import gamedata
from .common import AlchemyEncoder


@api.route('/starsector-ships/')
def api_gamedata_starsector():
    context = {
        'starsectors': gamedata.Data_starsector.query.order_by('listorder').all()
    }
    c = context
    return json.dumps(c, cls=AlchemyEncoder)


@api.route('/starsector-detail/<ship_id>')
def starsector_ship_detail(ship_id):
    starsector_ship = gamedata.Data_starsector.query.filter(gamedata.Data_starsector.id == ship_id).first()
    return json.dumps({'ship_detail': starsector_ship}, cls=AlchemyEncoder)
