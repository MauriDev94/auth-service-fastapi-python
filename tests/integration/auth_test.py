import pytest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_hello_world():
    response = client.get("/auth")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from auth router"}
