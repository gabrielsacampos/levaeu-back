from sqlalchemy.orm import relationship
from src.database.settings.base import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint, DateTime
from datetime import datetime

class EstablishmentTypes(Base):
    __tablename__: str = 'establishment_types'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    establishments = relationship("Establishments", back_populates="establishment_type")
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    

    