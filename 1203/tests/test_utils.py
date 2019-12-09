from flask import Flask
from app import app


def test_base_route():
    # app = Flask(__name__)
    # configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
