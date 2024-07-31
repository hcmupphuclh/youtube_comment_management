from flask import render_template

from resources.applications.protocols.blueprints_main_stub import ProgressOfMainStub
from resources.abstractions.endpoints import AbstractionOfEndpoints

class AttachmentOfBlueprints_InformationRequestieEnpointGraph(AbstractionOfEndpoints):
    
    def __init__(self, progressOfMainStub: ProgressOfMainStub) -> None:
        super().__init__(progressOfMainStub)
        
        self.route = "/informationRequestie"
        self.endpoint = "InformationRequestie"
        self.callback_function = self.informationRequestie
        self.methods = ["POST", "GET"]
        
    def informationRequestie(self):
        return render_template("gridview.html")
        
    