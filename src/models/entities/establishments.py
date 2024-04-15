from src.models.database.settings.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, String, ForeignKey, DateTime, Enum
from datetime import datetime

class Establishments(Base):
    __tablename__: str = 'establishments'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    description = Column(String, nullable=False)
    id_type = Column(String, ForeignKey('establishment_types.id'), nullable=False) 
    id_sponsor = Column(String, ForeignKey('users.id'), nullable=False)
    tag = Column(Enum('none', 'advertising', 'popular', name='tag'), nullable=False, default='none')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    establishment_type = relationship("EstablishmentTypes", back_populates="establishments")
    ratings = relationship("Ratings", back_populates="establishment")
    user = relationship("Users", back_populates="establishments")
    establishment_images = relationship("EstablishmentImages", back_populates="establishment")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
            "id_type": self.id_type,
            "id_sponsor": self.id_sponsor,
            "tag": self.tag,
        }