from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler: 
    def __init__(self):
        self.__connection_path = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )
        self.__engine = None
        self.__session = None

    def connect(self):
        self.__engine = create_engine(self.__connection_path)
        return self.__engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()