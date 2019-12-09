import pytest

from app import *
# from app import create_app
from tests.qplib import QpLib


@pytest.fixture
def app(mocker):
    mocker.patch(qpylib, return_value=QpLib)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    mocker.patch("example.database.get_all", return_value={})
    app = create_app()
    return app


def test_example(client):
    response = client.get("/")
    assert response.status_code == 200