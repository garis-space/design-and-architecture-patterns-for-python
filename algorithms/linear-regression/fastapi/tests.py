from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_predict():
    response = client.get("/predict/4")
    assert response.status_code == 200
    assert response.json() == [8.0]
