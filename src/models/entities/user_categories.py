from src.database.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from datetime import datetime

class UserCategories(Base):
    __table__: str = 'user_categories'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    reviews_checkpoint = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())