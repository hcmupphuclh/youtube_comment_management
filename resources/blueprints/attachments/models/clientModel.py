from sqlalchemy import create_engine, Column, String, Integer, CHAR
from resources.blueprints.attachments.base.declarative import DeclartiveBase

declarative = DeclartiveBase()
Base = declarative.base

class Client(Base):
    __tablename__ = "clientfiles"
    
    ssn = Column("ssn", Integer, primary_key=True, autoincrement=True)
    accountName = Column("accountname", String)
    fileName = Column("filename", String)
    role = Column("role", String)
    isRequired = Column("isRequired", Integer)
    
    def __init__(self, accountname, filename, role, isRequired):
        self.accountName = accountname
        self.fileName = filename
        self.role = role
        self.isRequired = isRequired
        
    def __repr__(self):
        return f"({self.ssn}) {self.accountName} {self.fileName} {self.role} {self.isRequired}"