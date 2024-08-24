from flask import Flask

from blueprint.general import app as general
from blueprint.user import app as user
from blueprint.admin import app as admin
import config
from extensions import db
app = Flask(__name__)
app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
db.init_app(app)
with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run()
