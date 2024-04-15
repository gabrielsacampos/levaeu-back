from src.models.database.settings.base import Base
from sqlalchemy.sql import func
from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class EstablishmentImages(Base):
    __tablename__: str = 'establishment_images'

    id = Column(String, primary_key=True)
    id_establishment = Column(String, ForeignKey("establishments.id"))
    img_description = Column(String, nullable=False)
    cover = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    establishment = relationship("Establishments", back_populates="establishment_images")


    def to_dict(self):
        return {
            "id": self.id,
            "id_establishment": self.id_establishment,
            "img_description": self.img_description,
            "cover": self.cover,
        }