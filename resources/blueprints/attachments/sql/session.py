from resources.blueprints.attachments.base.declarative import DeclartiveBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Session:
    
    engine = create_engine("sqlite:///youtube.db", echo=True)
    declarative = DeclartiveBase()
    declarative.base.metadata.create_all(bind=engine)
    
    @property
    def session(self) -> sessionmaker:
        return self._session
    
    @session.setter
    def session(self, session:sessionmaker):
        self._session = session
    
    def __init__(self) -> None:
        Session = sessionmaker(bind=self.engine)
        self.session = Session()