import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    payload = {
        "name": "Alice",
        "email": "maureen@example.com",
        "password": "password123"
    }
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"
    assert "id" in response.json()["data"]



def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Users retrieved successfully"
    assert isinstance(data["data"], list)




def test_get_user_by_id():
    response = client.post("/users", json={
        "name": "Bob",
        "email": "bob@example.com",
        "password": "secret"
    })
    user_id = response.json()["data"]["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


def test_update_user():
    response = client.post("/users", json={
        "name": "Charlie",
        "email": "charlie@example.com",
        "password": "initial"
    })
    user_id = response.json()["data"]["id"]
    update = {
        "name": "Charlie Updated",
        "email": "charlie_updated@example.com",
        "password": "newpassword"
    }
    response = client.put(f"/users/{user_id}", json=update)
    assert response.status_code == 200
    assert response.json()["message"] == "User updated successfully"
    assert response.json()["data"]["name"] == "Charlie Updated"


def test_delete_user():
    response = client.post("/users", json={
        "name": "David",
        "email": "david@example.com",
        "password": "topsecret"
    })
    user_id = response.json()["data"]["id"]
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "User deleted successfully"
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404


