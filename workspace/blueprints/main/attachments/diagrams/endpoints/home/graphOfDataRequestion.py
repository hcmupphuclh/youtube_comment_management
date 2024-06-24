from os.path import abspath
from flask import request, Response
import jsonpickle

from workspace.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from workspace.abstractions.endpoints import AbstractionOfEndpoints
from workspace.blueprints.main.attachments.diagrams.configs.cliensecret_youtube_api import APIsOfYoutubeFromClientSecret
from workspace.blueprints.main.attachments.diagrams.configs.APIRequestionFromFiles import AttachmentOfBlueprints_APIRequestionFromFiles
from workspace.blueprints.main.attachments.diagrams.configs.APIRequestionFromKeys import AttachmentOfBlueprints_APIRequestionFromKeys 
from workspace.blueprints.main.attachments.diagrams.programs.YoutubeAPIRequestion import YoutubePortion


class AttachmentOfBlueprints_DataRequestionEndpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/dataReceivement"
        self.endpoint = "DataReceivement"
        self.callback_function = self.get_data
        self.methods = ["POST", "GET"]
        
    def get_data(performanceChosenAccount):
        pathToChosenClientSecretFolder = abspath("workspace/blueprints/main/attachments/diagrams/client_secret_files/performance/")
        jsonData = request.get_json()
        
        # youtubeAPIRequestion = APIsOfYoutubeFromClientSecret(pathToChosenClientSecretFolder+"/"+jsonData["performanceChosenAccount"])
        youtubeAPIRequestion = AttachmentOfBlueprints_APIRequestionFromFiles(pathToChosenClientSecretFolder+"/"+jsonData["performanceChosenAccount"])
        youtubePortion = YoutubePortion(youtubeAPIRequestion.core)
    
        results = youtubePortion.getAllItems()
        
        return Response(jsonpickle.encode(results), mimetype="application/json")