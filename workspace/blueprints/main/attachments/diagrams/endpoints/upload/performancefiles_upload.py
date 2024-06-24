import os
from os.path import abspath
from flask import request, Response
from workspace.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from workspace.abstractions.endpoints import AbstractionOfEndpoints

class UploadHandleForPerformance(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/performanceFileUpload"
        self.endpoint = "performanceFileUploadResolvation"
        self.callback_function = self.performanceFileUpload
        self.methods = ["POST"]
        
    def performanceFileUpload():
        uploaded_file = request.files["userfile"]
        uploaded_file.save(os.path.join(abspath("workspace/blueprints/main/attachments/diagrams/client_secret_files/audiance/"), uploaded_file.filename))
        return Response()