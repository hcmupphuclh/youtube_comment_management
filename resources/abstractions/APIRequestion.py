import googleapiclient.discovery
from abc import ABC, abstractmethod

class AbstractionOfYoutubeCredential(ABC):
    
    allowance:str = None
    
    @property
    def core(self) -> googleapiclient.discovery:
        return self._core
    
    @core.setter
    def core(self, core: googleapiclient.discovery):
        self._core = core
        
    def __init__(self, allowance: str) -> None:
        self.allowance = allowance
        self.credientialRequestion()
    
    @abstractmethod
    def credientialRequestion(self):
        pass
        