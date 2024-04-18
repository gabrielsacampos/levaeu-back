from .ratings_repository import RatingsRepository

rating_mock = {
    "stars": 5,
    "review": "Nice place to go with friends and family.",
    "id_establishment": "uuid-cinelandia",
    "id_user": "uuid-jane-silva"
}


def test_insert_rating():
    ratings_repository = RatingsRepository()
    result = ratings_repository.insert(rating_mock)
    print(result)

