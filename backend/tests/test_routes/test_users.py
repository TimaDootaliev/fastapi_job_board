import json


def test_create_user(client):
    data = {"username": "testuser", "email": "testuser@testmail.com", "password": "testpassword"}
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@testmail.com"
    assert response.json()["is_active"] == True