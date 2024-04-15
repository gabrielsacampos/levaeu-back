from .ratings_repository import RatingsRepository

rating_mock = {
    "uuid": "random-uuid-rating-001",
    "stars": 5,
    "review": "Nice place to go with friends and family.",
    "id_establishment": "uuid-cinelandia",
    "id_user": "uuid-jane-silva"
}


def test_insert_rating():
    ratings_repository = RatingsRepository()
    result = ratings_repository.insert(rating_mock)
    print(result)


def test_find_by_id():
    ratings_repository = RatingsRepository()
    result = ratings_repository.get_by_id(rating_mock["uuid"])
    print(result)


def test_delete_rating():
    ratings_repository = RatingsRepository()
    result = ratings_repository.delete_by_id(rating_mock["uuid"])
    print(result)
