from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .base import Base
import src.models.entities
from sqlalchemy import text
from typing import List


class DBConnectionHandler: 
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///storage.sqlite3")
        self.session = None
        self.settup_database()
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
    

    def settup_database(self):
        with self.engine.connect() as connection:
            connection.execute(text("PRAGMA foreign_keys=ON"))
        Base.metadata.create_all(self.engine)


    def __enter__(self):
        return self.Session()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Session.remove()


connection_handler = DBConnectionHandler()