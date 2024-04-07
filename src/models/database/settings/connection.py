from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
import src.models.entities
from sqlalchemy import text
from typing import List


class DBConnectionHandler: 
    def __init__(self) -> None:
        self.__connection_path = "sqlite:///storage.sqlite3"
        self.engine = None
        self.session = None
        self.connect()
    
    def connect(self):
        self.engine = create_engine(self.__connection_path)

        with self.engine.connect() as connection:
            connection.execute(text("PRAGMA foreign_keys=ON"))
        
        self.create_schema()
        return self.engine

    def create_schema(self):
        Base.metadata.create_all(self.engine)

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


connection_handler = DBConnectionHandler()