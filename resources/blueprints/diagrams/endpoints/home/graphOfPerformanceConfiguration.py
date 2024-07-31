from flask import render_template

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.DAO.reserveAccountsDAO import ReserveAccountsDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_PerformanceConfigurationEnpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/performanceConfiguration"
        self.endpoint = "PerformanceConfiguration"
        self.callback_function = self.performanceConfiguration
        self.methods = ["POST", "GET"]
        
    def performanceConfiguration(self):
        DACore = Session()
        client = ClientDAO(DACore.session)
        
        client.regenerationByRole("performance")
        performanceFilesNode = client.storage
        
        return render_template("performanceConfiguration.html", performanceAccounts=performanceFilesNode)
        
    