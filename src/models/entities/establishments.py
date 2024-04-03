from src.models.settings.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey

class Establishments(Base):
    __tablename__: str = 'establishments'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    description = Column(String, nullable=True)
    id_type = Column(String, ForeignKey('establishment_types.id'), nullable=False) 
    establishment_type = relationship("EstablishmentTypes", back_populates="establishments")
