from flask import Flask
from flask_cors import CORS
from auth import auth_ns
from flask_restx import Api
from exts import db
from models import User
from flask_jwt_extended import JWTManager


def create_app(config):
    app = Flask(__name__, static_url_path="/", static_folder="./client/build")
    app.config.from_object(config)

    CORS(app)

    api = Api(app)
    db.init_app(app)

    JWTManager(app)

    api.add_namespace(auth_ns)

    # model (serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "user": User}

    return app
