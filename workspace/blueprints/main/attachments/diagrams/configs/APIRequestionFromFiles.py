import google_auth_oauthlib
import googleapiclient.discovery
from workspace.abstractions.APIRequestion import AbstractionOfYoutubeCredential

class AttachmentOfBlueprints_APIRequestionFromFiles(AbstractionOfYoutubeCredential):
    
    scopes: str = [
            "https://www.googleapis.com/auth/youtube.force-ssl",
            "https://www.googleapis.com/auth/youtubepartner",
            "https://www.googleapis.com/auth/youtube"
    ]
    api_service_name:str = "youtube"
    api_version:str = "v3"
    
    def __init__(self, allowance: str) -> None:
        super().__init__(allowance)
    
    def credientialRequestion(self):
        
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        self.allowance, self.scopes)
        
        credentials = flow.run_local_server(host='localhost', port=8088, open_browser=True)
        
        self.core = googleapiclient.discovery.build(
        self.api_service_name, self.api_version, credentials=credentials)