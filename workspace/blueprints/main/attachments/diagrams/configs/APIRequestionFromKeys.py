import google_auth_oauthlib
import googleapiclient.discovery
from workspace.abstractions.APIRequestion import AbstractionOfYoutubeCredential

class AttachmentOfBlueprints_APIRequestionFromKeys(AbstractionOfYoutubeCredential):
    
    api_service_name:str = "youtube"
    api_version:str = "v3"
    api_key: str = "AIzaSyBKaPv5JVvF6oYrhjQ-1F56m3tE7sZbHnQ"
    
    def __init__(self, allowance: str = None) -> None:
        super().__init__(allowance)
        
    def credientialRequestion(self):
        self.core = googleapiclient.discovery.build(self.api_service_name, 
                                                       self.api_version, 
                                                       developerKey=self.api_key)