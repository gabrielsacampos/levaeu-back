from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
import src.models.entities


class DBConnectionHandler: 
    def __init__(self) -> None:
        self.__connection_path = "sqlite:///storage.sqlite3"
        self.__engine = None
        self.session = None

    def connect(self):
        self.__engine = create_engine(self.__connection_path)
        Base.metadata.create_all(self.__engine)
        return self.__engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

connection_handler = DBConnectionHandler()