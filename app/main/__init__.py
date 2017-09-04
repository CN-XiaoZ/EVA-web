# -*- coding=utf-8 -*-
from flask import Blueprint
import sys
reload(sys)
sys.setdefaultencoding('utf8')

main = Blueprint('main', __name__)

from . import views, errors