from fastapi.testclient import TestClient
from fastapi import HTTPException, status
from app.main import app
from .mockData import user_login_success, user_login_failuer, new_User_success,new_User_failuer
import pytest



client = TestClient(app)



def test_auth_login_success():
    response = client.post("/auth/login",data=user_login_success).json()
    assert response['status'] == 200

def test_auth_login_failuer():
    response = client.post("/auth/login", data=user_login_failuer)
    assert response.status_code == 403

def test_auth_create_user_success():
    response = client.post("/auth/newUser", json=new_User_success).json()
    assert response['status'] == 200

def test_auth_create_user_failuer():
    response = client.post("/auth/newUser", json=new_User_failuer)
    assert response.status_code == 400




