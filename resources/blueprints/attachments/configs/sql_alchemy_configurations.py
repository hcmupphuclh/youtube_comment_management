from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class SqlAlchemyDeparture():
    
    Base: declarative_base = declarative_base()
    
    @property
    def session(self) -> sessionmaker:
        return self._session
    
    @session.setter
    def session(self, session: sessionmaker):
        self._session = session
    
    def __init__(self) -> None:
        engine = create_engine("sqlite:///youtube.db", echo=True)
        self.Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()