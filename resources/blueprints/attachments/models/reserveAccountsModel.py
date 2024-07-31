from sqlalchemy import create_engine, Column, String, Integer
from resources.blueprints.attachments.base.declarative import DeclartiveBase

declarative = DeclartiveBase()
Base = declarative.base

class ReserveAccounts(Base):
    __tablename__ = "reserveaccounts"
    
    ssn = Column("ssn", Integer, primary_key=True, autoincrement=True)
    accountName = Column("accountname", String)
    
    def __init__(self, accountname):
        self.accountName = accountname
        
    def __repr__(self):
        return f"({self.ssn}) {self.accountName}"