import os
import pytest
from datetime import date
from hello.app import create_app
from hello.db import db


@pytest.fixture()
def app():
    os.environ["DB_URI"] = "sqlite://"
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    with app.app_context():
        db.create_all()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


def test_birthday_hello(client):
    resp = client.put("/hello/test", json={
        "birthday": "1996-03-30",
    })
    assert resp.status_code == 204
    resp = client.put("/hello/test", json={
        "birthday": "2000-03-30"
    })
    assert resp.status_code == 204
    resp = client.get("/hello/test")
    assert resp.status_code == 200


def test_birthday_in_future(client):
    today = date.today()
    future = date(year=today.year+1, month=today.month, day=today.day)
    resp = client.put("/hello/test", json={
        "birthday": f"{future.isoformat()}"
    })
    assert resp.status_code == 400

def test_metrics(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200