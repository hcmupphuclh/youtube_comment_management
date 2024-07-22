from abc import ABC, abstractmethod
from sqlalchemy.orm import sessionmaker

class DAO(ABC):
    
    @property
    def DACore(self) -> sessionmaker:
        return self._DACore
    
    @DACore.setter
    def DACore(self, DACore:sessionmaker):
        self._DACore = DACore
       
    @property 
    @abstractmethod
    def storage(self) -> dict[str, str]:
        return self._storage

    @storage.setter
    def storage(self, storage:dict[str, str]):
        self._storage = storage
    
    def __init__(self, DACore:sessionmaker) -> None:
        self.DACore = DACore
        self.storage = self.storageGeneration()
        
    def find(self, index:str):
        return self.storage[index]
    
    @abstractmethod
    def all(self):
        results = []
        
        for index in self.storage:
            results.append(index)
            
        return results
    
    def search(self, index:str):
        for item in self.storage:
            if(item == index):
                return True
            else:
                return False
            
    @abstractmethod
    def present(self):
        for item in self.storage:
            print(item, ":", self.storage[item])
            
    @abstractmethod
    def storageGeneration(self):
        pass
    
    @abstractmethod
    def storageRegeneration(self):
        pass
    
    @abstractmethod
    def save(self, accountName:str, fileName:str):
        pass