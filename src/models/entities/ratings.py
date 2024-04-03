from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.settings.base import Base

class Ratings(Base):
        __tablename__: str = 'ratings'
        
        id = Column(String, primary_key=True)
        stars = Column(Integer, nullable=False)
        comment = Column(String, nullable=False)
        id_establishment = Column(String, ForeignKey("establishments.id"))
        
        establishment = relationship("Establishments", back_populates="ratings")