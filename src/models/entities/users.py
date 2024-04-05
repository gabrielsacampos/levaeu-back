from sqlalchemy import Column, String, DateTime
from src.database.settings.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Users(Base):
    __tablename__: str = 'users'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    ratings = relationship("Ratings", back_populates="user")
    establishments = relationship("Establishments", back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }