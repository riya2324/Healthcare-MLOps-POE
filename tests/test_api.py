from fastapi.testclient import TestClient
from app.main import app
from sklearn.datasets import load_breast_cancer

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "running" in response.json()["message"]

def test_prediction_endpoint():
    dataset = load_breast_cancer(as_frame=True)
    sample = dataset.data.iloc[0].to_dict()
    response = client.post("/predict", json={"features": sample})
    assert response.status_code == 200
    assert response.json()["class_name"] in ["benign", "malignant"]

def test_prediction_rejects_missing_features():
    response = client.post("/predict", json={"features": {"mean radius": 14.0}})
    assert response.status_code == 400
