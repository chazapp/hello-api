import os
import pytest
from hello.app import create_app
from hello.db import db


@pytest.fixture()
def app():
    os.environ["DB_URI"] = "sqlite:///memory"
    app = create_app()
    app.config.update({
        "TESTING": True
    })
    app.app_context().push()
    db.create_all()
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


def test_birthday_hello(client):
    resp = client.put("/hello/test", json={
        "birthday": "1996-03-30",
    })
    assert resp.status_code ==  204
    resp = client.put("/hello/test", json={
        "birthday": "2000-03-30"
    })
    assert resp.status_code == 204
    resp = client.get("/hello/test")
    assert resp.status_code == 200


