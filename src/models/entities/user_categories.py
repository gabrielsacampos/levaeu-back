from src.models.database.settings.base import Base
from sqlalchemy import Column, String, DateTime, Integer, PrimaryKeyConstraint
from datetime import datetime
from sqlalchemy.sql import func

class UserCategories(Base):
    __tablename__: str = 'user_categories'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    checkpoint = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def to_dict(self):      
        return {
            "id": self.id,
            "name": self.name,
            "checkpoint": self.checkpoint
        }