from library.app import app
from fastapi.testclient import TestClient


def test_read_items():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
