from flask import Blueprint
from abc import ABC, abstractmethod

class AbstractionOfBlueprints(ABC):
    
    name: str = None
    import_name: str = None
    template_folder: str = None
    static_folder: str = None
    
    @property
    def progress(self) -> Blueprint:
        return self._progress
    
    @progress.setter
    def progress(self, progress: Blueprint):
        self._progress = progress
        
    def __init__(self) -> None:
        pass
     
    def blueprint_adjustment(self):
        self.progress = Blueprint(self.name, self.import_name,
                                  template_folder=self.template_folder,
                                  static_folder= self.static_folder)