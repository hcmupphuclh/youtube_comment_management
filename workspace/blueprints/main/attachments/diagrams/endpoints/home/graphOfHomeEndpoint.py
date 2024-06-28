from flask import render_template

from workspace.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from workspace.abstractions.endpoints import AbstractionOfEndpoints
from workspace.blueprints.main.attachments.diagrams.configs.file_configuration import ConfigurationOfFiles

class AttachmentOfBlueprints_HomeEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/"
        self.endpoint = "index"
        self.callback_function = self.home
        self.methods = ["GET"]
        
    def home(self):
        fileConfig = ConfigurationOfFiles()
        
        performanceAccounts = fileConfig.performancePath
        audianceAccounts = fileConfig.audiancePath
        return render_template("index.html", performanceAccounts=performanceAccounts, audianceAccounts=audianceAccounts)