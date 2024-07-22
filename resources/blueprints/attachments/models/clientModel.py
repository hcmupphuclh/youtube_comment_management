from sqlalchemy import create_engine, Column, String, Integer, CHAR
from base.declarative import DeclartiveBase

declarative = DeclartiveBase()
Base = declarative.base

class ClientModel(Base):
    __tablename__ = "clientfiles"
    
    ssn = Column("ssn", Integer, primary_key=True, autoincrement=True)
    accountName = Column("accountname", String)
    fileName = Column("filename", String)
    role = Column("role", String)
    
    def __init__(self, accountname, filename, role):
        self.accountName = accountname
        self.fileName = filename
        self.role = role
        
    def __repr__(self):
        return f"({self.ssn}) {self.accountName} {self.fileName} {self.role}"