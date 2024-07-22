from sqlalchemy.ext.declarative import declarative_base

class DeclartiveBase():
    
    @property
    def base(self) -> declarative_base:
        return self._base
    
    @base.setter
    def base(self, base:declarative_base):
        self._base = base
    
    def __init__(self) -> None:
        self.base = declarative_base()