from sqlalchemy.orm import relationship
from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint

class EstablishmentTypes(Base):
    __tablename__: str = 'establishment_types'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    establishments = relationship("Establishments", back_populates="establishment_type")
    

    