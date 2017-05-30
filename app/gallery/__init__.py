# -*- coding: utf-8 -*-
from flask import Blueprint
gallery = Blueprint('gallery', __name__)

from . import views
