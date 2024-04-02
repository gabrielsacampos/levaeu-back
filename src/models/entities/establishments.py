from src.models.setting.base import Base
from sqlalchemy import Column, Integer, String

class Establishments(Base):
    __tablename__: str = 'establishments'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    type = Column(String, nullable=False)
    

    