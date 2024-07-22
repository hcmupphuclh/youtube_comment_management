from sqlalchemy.orm import sessionmaker
from resources.abstractions.DAO import DAO
from resources.blueprints.attachments.models.clientModel import ClientModel

class ClientDAO(DAO):
    
    @property
    def storage(self) -> dict[str, str]:
        return self._storage
    
    @storage.setter
    def storage(self, storage:dict[str, str]):
        self._storage = storage
    
    @property
    def item(self) -> str:
        return self._item
    
    @item.setter
    def item(self, item:str):
        self._item = item
    
    def __init__(self, DACore: sessionmaker) -> None:
        super().__init__(DACore)
    
    def storageGeneration(self):
        results = {}
        records = self.DACore.query(ClientModel).all()
        
        for record in records:    
            results.update({record.accountName:record.fileName})
        
        return results
    
    def regenerationByRole(self, role:str):
        self.storage = {}
        
        records = self.DACore.query(ClientModel).filter_by(role = role)
        for record in records:
            self.storage.update({record.accountName:record.fileName})
    
    def all(self, role:str):
        results = []
        
        for index in self.storage:
            results.append(index)
            
        return results
    def getItem(self, index:str):
        self.item = self.storage[index]
    
    def storageRegeneration(self):
        records = self.DACore.query(ClientModel).all()
        
        for record in records:    
            self.storage.update({record.accountName:record.fileName})
            
    def present(self):
        for item in self.storage:
            print(item, ":", self.storage[item])
    
    def save(self, accountName: str, fileName: str, role:str):
        client = ClientModel(accountName, fileName, role )
        self.DACore.add(client)
        self.DACore.commit()