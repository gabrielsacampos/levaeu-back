from sqlalchemy.orm import relationship
from src.models.database.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from datetime import datetime
from sqlalchemy.sql import func

class Ratings(Base):
        __tablename__: str = 'ratings'
        
        id = Column(String, primary_key=True)
        stars = Column(Integer, nullable=False)
        review = Column(String, nullable=False)
        id_establishment = Column(String, ForeignKey("establishments.id"), nullable=False)
        id_user = Column(String, ForeignKey("users.id"))
        created_at = Column(DateTime, default=func.now())
        updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
        
        establishment = relationship("Establishments", back_populates="ratings")
        user = relationship("Users", back_populates="ratings")

        def to_dict(self):
                return {
                        "id": self.id,
                        "stars": self.stars,
                        "review": self.review,
                        "id_establishment": self.id_establishment,
                        "id_user": self.id_user
                }