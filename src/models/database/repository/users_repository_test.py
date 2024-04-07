from src.models.database.repository.users_repository import UsersRepository


user_mock = {
    "uuid": "uuid-new-user",
    "name": "Kaik The New",
    "email": "kaik@email.com"
}

def test_create_user():
    response = UsersRepository().insert(user_mock)
    print(response)

def test_get_user_by_id():
    user = UsersRepository().get_user_by_id(user_mock["uuid"])
    assert user["id"] == user_mock["uuid"]
    assert user["name"] == user_mock["name"]
    assert user["email"] == user_mock["email"]

def test_get_all_users():
    response = UsersRepository().get_all()
    print(response)
    

def test_delete_user():
    response = UsersRepository().delete_user(user_mock["uuid"])
    print(response)
    