from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_car():
    response = client.post("/api/car/", json={
        "model": "Model X",
        "manufacturer": "Tesla",
        "description": "Electric car",
        "year": 2023
    })
    assert response.status_code == 200
    assert response.json()["model"] == "Model X"

def test_read_cars():
    response = client.get("/api/car/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
