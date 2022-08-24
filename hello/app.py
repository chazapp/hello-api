import os
from flask import Flask, Response
from hello.db import db, migrate
from dotenv import load_dotenv
from hello.routes.hello import bp as hello
from hello.routes.metrics import bp as metrics


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.register_blueprint(hello)
    app.register_blueprint(metrics)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/health", methods=["GET"])
    def health():
        return Response("", 200)

    return app