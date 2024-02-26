from flask import Flask
import os

application = Flask(__name__)

application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  

application.config['SECRET_KEY'] = '3daed8d179e2a254c691f3d6b2104484ade7aa315221bfbd'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

