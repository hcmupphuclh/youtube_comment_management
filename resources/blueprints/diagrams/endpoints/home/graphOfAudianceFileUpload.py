import os
from os.path import abspath
from flask import request, Response
from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.programs import stringrandom
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_AudianceFileUploadEnpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/audianceFileUpload"
        self.endpoint = "AudianceFileUpload"
        self.callback_function = self.audianceFileUpload
        self.methods = ["POST", "GET"]
        
    def audianceFileUpload(self):
        jsonData = request.get_json()
        accountName = jsonData["audianceAccount"]
        
        DACore = Session()
        client = ClientDAO(DACore.session)
        
        client.save(accountName, stringrandom.randomWords(64), "performance")
        client.regenerationByRole("audiance")
        client.getItem(accountName)
        
        uploaded_file = request.files["userfile"]
        uploaded_file.save(os.path.join(abspath("resources/blueprints/attachments/client_secret_files/audiance/"), client.item))
        
        return Response()