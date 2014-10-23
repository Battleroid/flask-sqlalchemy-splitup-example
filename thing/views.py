from flask import Blueprint
from thing.models import Thing

basic = Blueprint('basic', __name__)

@basic.route('/')
def index():
    return 'Index'

@basic.route('/things')
def things():
    print Thing.query.all()
    return 'things'