from flask import render_template

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_AudianceConfigurationEnpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/audianceConfiguration"
        self.endpoint = "AudianceConfiguration"
        self.callback_function = self.audianceConfiguration
        self.methods = ["POST", "GET"]
        
    def audianceConfiguration(self):
        DACore = Session()
        client = ClientDAO(DACore.session)
        
        client.regenerationByRole("audiance")
        audianceFilesNode = client.storage
        
        return render_template("audianceConfiguration.html", audianceAccounts = audianceFilesNode)
        
    