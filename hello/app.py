import os
from flask import Flask
from hello.db import db, migrate
from dotenv import load_dotenv
from hello.routes.hello import bp as hello

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.register_blueprint(hello)
    db.init_app(app)
    migrate.init_app(app, db)
    return app


if __name__ == '__main__':
    load_dotenv()
    app = create_app()
    app.run(port=8080, debug=True)