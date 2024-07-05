from os.path import abspath
from flask import request, Response
import jsonpickle

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.configs.APIRequestionFromFiles import AttachmentOfBlueprints_APIRequestionFromFiles
from resources.blueprints.attachments.programs.YoutubeAPIRequestion import YoutubePortion


class AttachmentOfBlueprints_DataRequestionEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/dataReceivement"
        self.endpoint = "DataReceivement"
        self.callback_function = self.get_data
        self.methods = ["POST", "GET"]
        
    def get_data(performanceChosenAccount):
        pathToChosenClientSecretFolder = abspath("resources/blueprints/attachments/client_secret_files/performance/")
        jsonData = request.get_json()
        
        # youtubeAPIRequestion = APIsOfYoutubeFromClientSecret(pathToChosenClientSecretFolder+"/"+jsonData["performanceChosenAccount"])
        youtubeAPIRequestion = AttachmentOfBlueprints_APIRequestionFromFiles(pathToChosenClientSecretFolder+"/"+jsonData["performanceChosenAccount"])
        youtubePortion = YoutubePortion(youtubeAPIRequestion.core)
    
        results = youtubePortion.getAllItems()
        
        return Response(jsonpickle.encode(results), mimetype="application/json")