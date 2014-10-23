from flask import Blueprint
from thing.models.asdf import Thing


basic = Blueprint('basic', __name__)

@basic.route('/')
def index():
    return 'basic index'

@basic.route('/things')
def things():
    query = Thing.query.first()
    return query.__dict__['name']
