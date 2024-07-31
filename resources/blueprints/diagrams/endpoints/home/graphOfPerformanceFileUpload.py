import os
from os.path import abspath
from flask import request, Response
from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.programs import stringrandom
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_PerformanceFileUploadEnpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/performanceFileUpload"
        self.endpoint = "PerformanceFileUpload"
        self.callback_function = self.performanceFileUpload
        self.methods = ["POST", "GET"]
        
    def performanceFileUpload(self):
        accountName = request.form["performanceAccount"]
        
        DACore = Session()
        client = ClientDAO(DACore.session)
        
        client.storageUpdate(accountName, stringrandom.randomWords(64), "performance", 0)
        client.save()
        client.storageRegeneration()
        client.getItem(accountName)
        
        uploaded_file = request.files["userfile"]
        uploaded_file.save(os.path.join(abspath("resources/blueprints/attachments/client_secret_files/performance/"), client.item))
        
        return Response()