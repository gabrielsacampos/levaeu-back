from src.database.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from datetime import datetime
from sqlalchemy.sql import func

class UserCategories(Base):
    __table__: str = 'user_categories'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    reviews_checkpoint = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())