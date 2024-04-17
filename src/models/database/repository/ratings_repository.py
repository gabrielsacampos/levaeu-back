from typing import Dict
from src.models.database.settings.connection import connection_handler
from src.models.entities.ratings import Ratings
from src.models.entities.users import Users
from src.models.entities.establishments import Establishments
from src.models.entities.user_categories import UserCategories
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.errors.http_conflict import HttpConflictException
from src.errors.http_not_found import HttpNotFoundException
from termcolor import colored
from sqlalchemy import text

class RatingsRepository:
    def insert(self, rating_data: Dict) -> Dict:
        with connection_handler as database:
            try:
                rating = Ratings(
                    stars=rating_data.get("stars"),
                    review=rating_data.get("review"),
                    id_establishment=rating_data.get("id_establishment"),
                    id_user=rating_data.get("id_user")
                )
                database.add(rating)
                database.commit()
                return rating.to_dict()

            except IntegrityError:
                database.rollback()
                raise HttpConflictException("Rating id already exists or not found foreign keys")

            except Exception as error:
                database.rollback()
                raise error

    def get_by_id(self, rating_id: Dict) -> Dict:
        with connection_handler as database:
            rating = database.query(Ratings).filter_by(id=rating_id).first()
            if rating is None:
                raise HttpNotFoundException("Rating not found.")
            return rating.to_dict()

    def delete_by_id(self, rating_id: Dict) -> Dict:
        with connection_handler as database:
            try:
                rating = database.query(Ratings).filter_by(id=rating_id).first()
                database.delete(rating)
                database.commit()
            except UnmappedInstanceError:
                database.rollback()
                raise HttpNotFoundException("Could not delete rating while is not found.")
            return rating

    def get_all(self) -> Dict:
        with connection_handler as database:
            sql = """
                SELECT 
                    u.name AS user_name,
                    u.image_url AS user_image_url,
                    uc.name AS user_category,
                    r.review AS review, 
                    r.updated_at AS date,
                    r.stars AS stars,
                    e.name as establishment_name
                FROM ratings AS r
                INNER JOIN users AS u ON r.id_user = u.id
                INNER JOIN establishments AS e ON r.id_establishment = e.id
                INNER JOIN user_categories AS uc ON uc.checkpoint = CAST(u.global_score AS INTEGER)
                ORDER BY r.updated_at DESC;
            """

            ratings = database.execute(text(sql))

            result_list = []
            for row in ratings:
                result_list.append({
                    "user_name": row.user_name,
                    "user_category": row.user_category,
                    "user_image_url": row.user_image_url,   
                    "review": row.review,
                    "date": row.date,
                    "stars": row.stars,
                    "establishment_name": row.establishment_name

                })
            return result_list
