# tests/test_model.py
import pytest
from fastapi.testclient import TestClient
from src.app import app  # Pointing to src/app.py

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_prediction_endpoint():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/prediction-service", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
