from flask import request, Response

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_RequirationSwitchEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/requirationSwitch"
        self.endpoint = "RequirationSwitch"
        self.callback_function = self.requirationSwitch
        self.methods = ["POST", "GET"]
        
    def requirationSwitch(self):
        jsonData = request.get_json()
        accountSelection = jsonData["accountSelection"]
        accountRejection = jsonData["accountRejection"]
        
        DACore = Session()
        client = ClientDAO(DACore.session)
        client.switchOff(accountRejection)
        client.switchOn(accountSelection)
        
        
        return Response()
        
    