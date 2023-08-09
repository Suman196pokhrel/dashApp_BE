from .mockData import user_login_success, user_login_failuer, new_User_success,new_User_failuer






def test_auth_create_user_success(client):
    response = client.post("/auth/newUser", json=new_User_success).json()
    assert response['status'] == 200


def test_auth_login_success(client):
    response = client.post("/auth/login",data={"username":new_User_success["email"],"password":new_User_success["password"]}).json()
    assert response['status'] == 200


def test_auth_login_failuer(client):
    response = client.post("/auth/login", data=user_login_failuer)
    assert response.status_code == 403



def test_auth_create_user_failuer(client):
    response = client.post("/auth/newUser", json=new_User_failuer)
    assert response.status_code == 422




