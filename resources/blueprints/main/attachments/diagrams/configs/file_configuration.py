from os import listdir
from os.path import isfile, join, abspath

class ConfigurationOfFiles():
    
    performancePath:str = None
    audiancePath:str = None
    
    def __init__(self) -> None:
        self.performancePath()
        self.audiancePath()
    
    def performancePath(self):
        path = abspath("resources/blueprints/main/attachments/diagrams/client_secret_files/performance/")
        self.performancePath = [f for f in listdir(path) if isfile(join(path, f))]
    
    def audiancePath(self):
        path = abspath("resources/blueprints/main/attachments/diagrams/client_secret_files/audiance/")
        self.audiancePath = [f for f in listdir(path) if isfile(join(path, f))]