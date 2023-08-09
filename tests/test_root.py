from fastapi.testclient import TestClient
from app.main import app



client = TestClient(app)



def test_root_status():
    response = client.get("/")
    # print(response.json())
    assert response.json()['status'] == 200


