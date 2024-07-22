from os.path import abspath
from flask import request, Response
import jsonpickle

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.configs.APIRequestionFromFiles import AttachmentOfBlueprints_APIRequestionFromFiles
from resources.blueprints.attachments.programs.YoutubeAPIRequestion import YoutubePortion
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_DataRequestionEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/dataReceivement"
        self.endpoint = "DataReceivement"
        self.callback_function = self.get_data
        self.methods = ["POST", "GET"]
        
    def get_data(performanceChosenAccount):
        jsonData = request.get_json()
        index = jsonData["performanceChosenAccount"]
        
        DACore = Session()
        client = ClientDAO(DACore.session)
        client.getItem(index)
        
        pathToChosenClientSecretFolder = abspath("resources/blueprints/attachments/client_secret_files/performance/")
        
        youtubeAPIRequestion = AttachmentOfBlueprints_APIRequestionFromFiles(pathToChosenClientSecretFolder+"/" + client.item)
        youtubePortion = YoutubePortion(youtubeAPIRequestion.core)
    
        results = youtubePortion.getAllItems()
        
        return Response(jsonpickle.encode(results), mimetype="application/json")