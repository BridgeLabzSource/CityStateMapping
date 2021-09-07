import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestFastApiFunction:
    def test_get_state_name_for_given_city_name(self):
        data = {"city_name": "Pune"}
        response = client.post("/states/", json=data)
        data = json.loads(response.content)
        assert response.status_code == 200 and data['state'] == "Maharashtra"

    def test_state_name_with_misspelled_city_name(self):
        data = {"city_name": "dlh"}
        response = client.post("/states/", json=data)
        data = json.loads(response.content)
        assert response.status_code == 200 and data['state'] == "Delhi"

    def test_state_name_with_empty_city_name(self):
        data = {"city_name": ""}
        response = client.post("/states/", json=data)
        assert response.status_code == 400 and b"give a proper city name" in response.content
