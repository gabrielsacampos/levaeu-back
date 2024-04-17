from sqlalchemy import Column, String, DateTime, Integer, Float
from src.models.database.settings.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.sql import func


class Users(Base):
    __tablename__: str = 'users'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    email = Column(String, nullable=False)
    global_score = Column(Float, nullable=False)
    week_score = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    ratings = relationship("Ratings", back_populates="user")
    establishments = relationship("Establishments", back_populates="user")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "email": self.email,
            "global_score": self.global_score,
            "week_score": self.week_score,
        }


    
