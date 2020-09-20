from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from healthcheck import HealthCheck, EnvironmentDump

# @TODO use application factory approach
app = Flask(__name__)

# wrap the flask app and give a heathcheck url
health = HealthCheck(app, "/healthz")
envdump = EnvironmentDump(app, "/environment")

app.config.from_object('notejam.config.Config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "signin"
login_manager.init_app(app)

mail = Mail()
mail.init_app(app)

from notejam import views
