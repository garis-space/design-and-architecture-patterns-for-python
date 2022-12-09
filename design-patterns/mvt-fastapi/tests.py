from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_user_view():
    response = client.get("/user?username=foo")
    assert response.status_code == 200
    assert response.text == "<h1>foo</h1>"
