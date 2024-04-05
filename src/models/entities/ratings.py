from sqlalchemy.orm import relationship
from src.database.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Integer
from datetime import datetime

class Ratings(Base):
        __tablename__: str = 'ratings'
        
        id = Column(String, primary_key=True)
        stars = Column(Integer, nullable=False)
        comment = Column(String, nullable=False)
        id_establishment = Column(String, ForeignKey("establishments.id"))
        id_user = Column(String, ForeignKey("users.id"))
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
        
        establishment = relationship("Establishments", back_populates="ratings")
        user = relationship("Users", back_populates="ratings")

        def to_dict(self):
                return {
                        "id": self.id,
                        "stars": self.stars,
                        "comment": self.comment,
                        "id_establishment": self.id_establishment,
                        "id_user": self.id_user
                }