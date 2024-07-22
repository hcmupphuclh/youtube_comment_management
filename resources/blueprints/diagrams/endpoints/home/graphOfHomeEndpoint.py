from flask import render_template

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_HomeEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/"
        self.endpoint = "index"
        self.callback_function = self.home
        self.methods = ["GET"]
        
    def home(self):
        DACore = Session()
        client = ClientDAO(DACore.session)
        
        client.regenerationByRole("audiance")
        audianceFilesNode = client.storage
        
        client.regenerationByRole("performance")
        performanceFilesNode = client.storage
        
        return render_template("index.html", performanceAccounts=performanceFilesNode, audianceAccounts=audianceFilesNode)