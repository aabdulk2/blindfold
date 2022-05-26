from flask import Flask, render_template
from flask_login import LoginManager
from app.routes.auth_routes import auth_routes
from app.models import db, Users
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://blindfold_dev:blindfoldpassword@localhost/blindfold_db'
app.config['SECRET_KEY'] = 'secretKey'
db.init_app(app)
socketio = SocketIO(app)

app.register_blueprint(auth_routes)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route("/", methods=["GET"])
def home():
    return "Hello"

if __name__ == '__main__':
    socketio.run(app)