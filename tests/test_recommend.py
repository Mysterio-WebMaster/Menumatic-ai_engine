import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_recommend_success(client):
    response = client.get("/v1/test")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data["status"] == 200
    assert json_data["message"] == "Test is success"
    assert json_data["data"] == "test"
