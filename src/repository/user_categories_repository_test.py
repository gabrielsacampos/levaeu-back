from src.repository.user_categories_repository import UserCategoriesRespository   


user_category_mock = {
    "uuid": "random-uuid-user-category-001",
    "name": "Movie Lovers",
    "checkpoint": 2
}

def test_insert_user_category():
    UserCategoriesRespository().insert(user_category_mock)
    

def test_get_all_user_categories():
    UserCategoriesRespository().get_all()
    

def test_delete_user_category():
    UserCategoriesRespository().delete(user_category_mock["uuid"])
    