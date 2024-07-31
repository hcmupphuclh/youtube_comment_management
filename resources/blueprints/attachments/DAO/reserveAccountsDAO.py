from sqlalchemy.orm import sessionmaker
from resources.abstractions.DAO import DAO
from resources.blueprints.attachments.models.reserveAccountsModel import ReserveAccounts

class ReserveAccountsDAO(DAO):
    
    @property
    def storage(self) -> list[str]:
        return self._storage
    
    @storage.setter
    def storage(self, storage:list[str]):
        self._storage = storage
    
    @property
    def item(self) -> str:
        return self._item
    
    @item.setter
    def item(self, item:str):
        self._item = item
    
    def __init__(self, DACore: sessionmaker) -> None:
        super().__init__(DACore)
        
    def present(self):
        for index in range(len(self.storage)):
            print(index, ":", self.storage[index])
            
    def storageGeneration(self):
        self.storage = []
        records = self.DACore.query(ReserveAccounts).all()
        
        for record in records:    
            self.storage.append(record.accountName)

    
    def storageRegeneration(self):
        self.storage = []
        
        records = self.DACore.query(ReserveAccounts).all()
        
        for record in records:    
            self.storage.append(record.accountName)
    
    def save(self, accountName: str):
        account = ReserveAccounts(accountName)
        self.DACore.add(account)
        self.DACore.commit()