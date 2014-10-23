from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from thing.views import basic

app.register_blueprint(basic)
