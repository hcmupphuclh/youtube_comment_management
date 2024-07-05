from resources.abstractions.blueprints import AbstractionOfBlueprints
from resources.blueprints.main.attachments.diagrams.endpoints.home.graphOfHomeEndpoint import AttachmentOfBlueprints_HomeEndpointGraph
from resources.blueprints.main.attachments.diagrams.endpoints.home.graphOfDataRequestion import AttachmentOfBlueprints_DataRequestionEndpointGraph
from resources.blueprints.main.attachments.diagrams.endpoints.home.graphOfCommentExecution import AttachmentOfBlueprints_CommentExecutionEndpointGraph
from resources.blueprints.main.attachments.diagrams.endpoints.upload.performancefiles_upload import UploadHandleForPerformance
from resources.blueprints.main.attachments.diagrams.endpoints.upload.audiancefiles_upload import UploadHandleForAudiance


class AttachmentOfBlueprints_IndexDiagram(AbstractionOfBlueprints):
    
    def __init__(self) -> None:
        
        self.name = "main"
        self.import_name = "__name__"
        self.template_folder = "resources/blueprints/main/attachments/diagrams/endpoints/templates"
        self.static_folder = "resources/blueprints/main/attachments/diagrams/endpoints/templates/static"
        
        self.blueprint_adjustment()
        self.endpoints_adjustment()
        
    def endpoints_adjustment(self):
        home = AttachmentOfBlueprints_HomeEndpointGraph(self)
        home.endpoint_adjustment()
        
        performanceUploadHandler = UploadHandleForPerformance(self)
        performanceUploadHandler.endpoint_adjustment()
        
        audianceUploadHandler = UploadHandleForAudiance(self)
        audianceUploadHandler.endpoint_adjustment()
        
        dataRequestionHandler = AttachmentOfBlueprints_DataRequestionEndpointGraph(self)
        dataRequestionHandler.endpoint_adjustment()
        
        commentExecutionHandler = AttachmentOfBlueprints_CommentExecutionEndpointGraph(self)
        commentExecutionHandler.endpoint_adjustment()
        
        