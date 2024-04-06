from .ratings_repository import RatingsRepository
import pytest

rating_mock = {
    "uuid": "random-uuid-rating-001",
    "stars": 5,
    "review": "Nice place to go with friends and family.",
    "id_establishment": "uuid-the-great-cinema",
    "id_user": "uuid-jack"
}


def test_insert_rating():
    ratings_repository = RatingsRepository()
    result = ratings_repository.insert(rating_mock)
    print(result)

def test_find_by_id():
    ratings_repository = RatingsRepository()
    result = ratings_repository.find_by_id(rating_mock["uuid"])
    print(result)

def test_delete_rating():
    ratings_repository = RatingsRepository()
    result = ratings_repository.delete(rating_mock["uuid"])
    print(result)
