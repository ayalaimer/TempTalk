from flask import Flask

def create app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '3gT9tZ4u'

    return app


