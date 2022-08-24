from hello.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)

