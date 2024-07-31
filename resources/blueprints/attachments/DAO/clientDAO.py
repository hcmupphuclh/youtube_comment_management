from sqlalchemy.orm import sessionmaker
from resources.abstractions.DAO import DAO
from resources.blueprints.attachments.models.clientModel import Client

class ClientDAO(DAO):
    
    @property
    def storage(self) -> dict[str, str]:
        return self._storage
    
    @storage.setter
    def storage(self, storage:dict[str, str]):
        self._storage = storage
    
    @property
    def storageForPresent(self) -> list[str]:
        return self._storageForPresent
    
    @storageForPresent.setter
    def storageForPresent(self, storageForPresent:list[str]):
        self._storageForPresent = storageForPresent
    
    @property
    def item(self) -> str:
        return self._item
    
    @item.setter
    def item(self, item:str):
        self._item = item
    
    @property
    def listItem(self) -> list[str]:
        return self._listItem
    
    @listItem.setter
    def listItem(self, listItem:list[str]):
        self._listItem = listItem
    
    def __init__(self, DACore: sessionmaker) -> None:
        super().__init__(DACore)
    
    def storageGeneration(self):
        self.storage = {}
        records = self.DACore.query(Client).all()
        
        for record in records:    
            self.storage.update({record.accountName:record.fileName})
    
    def regenerationByRole(self, role:str):
        self.storage = {}
        self.index = 0
        records = self.DACore.query(Client).filter_by(role = role)
        
        for record in records:
            self.index = self.index + 1
            dictObj = {"accountName":record.accountName,"isRequired":record.isRequired}
            self.storage.update({self.index:dictObj})
    
    def regenerationByRequiration(self):
        self.storage = {}
        self.index = 0
        records = self.DACore.query(Client).filter_by(isRequired = 1)
        
        for record in records:
            self.index = self.index + 1
            dictObj = {"accountName":record.accountName, "fileName":record.fileName}
            self.storage.update({self.index:dictObj})
    
    def getItem(self, index:str):
        self.item = self.storage[index]
    
    def storageRegeneration(self):
        self.storage = {}
        
        records = self.DACore.query(Client).all()
        
        for record in records:    
            self.storage.update({record.accountName:record.fileName})
    
    def storageUpdate(self, accountName, fileName, role, isRequired):
        self.storageForPresent = []
        
        self.storageForPresent.append(accountName)
        self.storageForPresent.append(fileName)
        self.storageForPresent.append(role)
        self.storageForPresent.append(isRequired)
        
    def present(self):
        for item in self.storage:
            print(item, ":", self.storage[item])
    
    def save(self):
        client = Client(self.storageForPresent[0], self.storageForPresent[1], 
                        self.storageForPresent[2], self.storageForPresent[3])
        self.DACore.add(client)
        self.DACore.commit()
        
    def switchOn(self, accounts:list[str]):
        for item in range(len(accounts)):
            self.DACore.query(Client).filter(Client.accountName == accounts[item], Client.role == "performance").update({"isRequired":1})
            self.DACore.commit()
        
    def switchOff(self, accounts:list[str]):
        for item in range(len(accounts)):
            self.DACore.query(Client).filter(Client.accountName == accounts[item], Client.role == "performance").update({"isRequired":0})
            self.DACore.commit()