from os.path import abspath
from flask import request, Response

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints
from resources.blueprints.attachments.configs.APIRequestionFromFiles import AttachmentOfBlueprints_APIRequestionFromFiles 
from resources.blueprints.attachments.programs.YoutubeAPIRequestion import YoutubePortion
from resources.blueprints.attachments.DAO.clientDAO import ClientDAO
from resources.blueprints.attachments.sql.session import Session

class AttachmentOfBlueprints_CommentExecutionEndpointGraph(AbstractionOfEndpoints):
    
     def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/commentExecution"
        self.endpoint = "CommentExecution"
        self.callback_function = self.comment_execution
        self.methods = ["POST", "GET"]
        
        
     def comment_execution(self):
        jsonData = request.get_json()
        index = jsonData["audianceChosenAccount"]
        
        DACore = Session()
        client = ClientDAO(DACore.session)
        client.getItem(index)
        
        pathToChosenClientSecretFolder = abspath("resources/blueprints/attachments/client_secret_files/audiance/")
        
        
        youtubeAPIRequestion = AttachmentOfBlueprints_APIRequestionFromFiles(pathToChosenClientSecretFolder+"/"+client.item)
        youtubePortion = YoutubePortion(youtubeAPIRequestion.core)
        youtubePortion.doComments(jsonData["comment"], jsonData["videoIDs"])
        
        return Response()