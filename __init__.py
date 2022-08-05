from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fb9f6e231bdcb1exit769c4d347bfb7cde49'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #Aqui em login vai o ome da função da página
login_manager.login_message = 'Faça o login para acessar essa página.'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import routes