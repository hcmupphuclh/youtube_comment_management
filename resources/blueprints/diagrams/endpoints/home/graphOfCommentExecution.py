from os.path import abspath
from flask import request, Response

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.main.attachments.diagrams.configs.APIRequestionFromFiles import AttachmentOfBlueprints_APIRequestionFromFiles 
from resources.blueprints.main.attachments.diagrams.programs.YoutubeAPIRequestion import YoutubePortion


class AttachmentOfBlueprints_CommentExecutionEndpointGraph(AbstractionOfEndpoints):
    
     def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/commentExecution"
        self.endpoint = "CommentExecution"
        self.callback_function = self.comment_execution
        self.methods = ["POST", "GET"]
        
        
     def comment_execution(self):
        pathToChosenClientSecretFolder = abspath("resources/blueprints/main/attachments/diagrams/client_secret_files/audiance/")
        jsonData = request.get_json()
        
        youtubeAPIRequestion = AttachmentOfBlueprints_APIRequestionFromFiles(pathToChosenClientSecretFolder+"/"+jsonData["audianceChosenAccount"])
        youtubePortion = YoutubePortion(youtubeAPIRequestion.core)
        youtubePortion.doComments(jsonData["comment"], jsonData["videoIDs"])
        
        return Response()