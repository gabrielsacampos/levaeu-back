from src.models.database.repository.user_categories_repository import UserCategoriesRespository   


user_category_mock = {
    "uuid": "random-uuid-user-category-001",
    "name": "Movie Lovers",
    "reviews_checkpoint": 2
}

def test_insert_user_category():
    result = UserCategoriesRespository().insert(user_category_mock)
    print(result)

def test_get_all_user_categories():
    result = UserCategoriesRespository().get_all()
    print(result)

def test_delete_user_category():
    result = UserCategoriesRespository().delete(user_category_mock["uuid"])
    print(result)