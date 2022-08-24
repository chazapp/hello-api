import wtforms_json
from datetime import datetime, date
from flask import Blueprint, jsonify, request, Response
from hello.models.users import User
from wtforms import Form, DateField, ValidationError

from hello.db import db

wtforms_json.init()

class BirthdayForm(Form):
    birthday = DateField(format="%Y-%m-%d")

    def validate_birthday(form, field):
        now = date.today()
        if field.data > now:
            raise ValidationError("Birthday must be a date before today.")

bp = Blueprint("hello", __name__)

def get_days_until_birthday(birthday: date) -> int:
    today = date.today()
    this_year = (date(today.year, birthday.month, birthday.day) - today).days
    if this_year >= 0:
        return this_year
    next_year = (date(today.year + 1, birthday.month, birthday.day) - today).days
    return next_year

@bp.route("/hello/<username>", methods=["PUT"])
def save_user_dob(username: str) -> Response:
    form = BirthdayForm.from_json(request.get_json())
    if form.validate():
        user = User.query.filter_by(username=username).first()
        if user:
            user.birthday = form.birthday.data
        else:
            user = User(birthday=form.birthday.data, username=username)
        db.session.add(user)
        db.session.commit()
        return '', 204
    else:
        return form.errors, 400


@bp.route("/hello/<username>", methods=["GET"])
def say_hello(username) -> Response:
    user = User.query.filter_by(username=username).first()
    if user:
        now = datetime.now()
        if user.birthday.month == now.month and user.birthday.day == now.day:
            return jsonify({"message": f"Hello {username} ! Happy Birthday !"}), 200
        else:
            return jsonify({"message": f"Hello {username} ! Your birthday is in {get_days_until_birthday(user.birthday)} day(s)"}), 200
    else:
        return jsonify({"message": f"Hello {username} ! We don't have your birthday on file yet."}), 404

