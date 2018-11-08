from flask import Blueprint

api = Blueprint('api', __name__)

from .gamedata import *
from .bx import *