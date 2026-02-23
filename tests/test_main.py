from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    response = client.post("/signup", json={
        "name": "TestUser",
        "email": "testuser@example.com",
        "password": "strongpass123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_login():
    response = client.post("/login", data={
        "username": "testuser@example.com",
        "password": "strongpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_class():
    # login first
    login = client.post("/login", data={
        "username": "testuser@example.com",
        "password": "strongpass123"
    })

    token = login.json()["access_token"]

    response = client.post(
        "/classes",
        json={
            "name": "Test Class",
            "dateTime": "2026-03-01T10:00:00Z",
            "instructor": "Instructor",
            "availableSlots": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Test Class"

def test_booking_flow():
    # login
    login = client.post("/login", data={
        "username": "testuser@example.com",
        "password": "strongpass123"
    })
    token = login.json()["access_token"]

    # book class id 1
    response = client.post(
        "/book",
        json={
            "class_id": 1,
            "client_name": "TestUser",
            "client_email": "testuser@example.com"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200

    # duplicate booking should fail
    response2 = client.post(
        "/book",
        json={
            "class_id": 1,
            "client_name": "TestUser",
            "client_email": "testuser@example.com"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response2.status_code == 400