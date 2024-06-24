from googleapiclient import errors
import googleapiclient.discovery

class YoutubePortion():
    
    channelID: str = None
    
    @property
    def youtubeCore(self) -> googleapiclient.discovery:
        return self._youtubeCore
    
    @youtubeCore.setter
    def youtubeCore(self, youtubeCore: googleapiclient.discovery):
        self._youtubeCore = youtubeCore
        
    def __init__(self, youtubeCore: googleapiclient.discovery) -> None:
        self.youtubeCore = youtubeCore
        self.channelListAPICall()
        
        
    def channelListAPICall(self):
        request = self.youtubeCore.channels().list(
            part="contentDetails",
            mine=True
        )
    
        response = request.execute()
    
        self.channelID = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        
    def getChannelIDFromDatabase(self, tableName: str):
        channels = self.sqlCore.query(tableName).all()
        results = []
        for channel in channels:
            results.append(channel.serialize())
        
        return results
    
    def doComments(self, comment: str, videoIDs: str):
        for videoID in videoIDs:
            request_body = {
                'snippet': {
                    'videoId': videoID,
                    'channelId': self.channelID,
                    'topLevelComment': {
                        'snippet': {
                            'textOriginal': comment
                        }
                    }
                }
            }
        
            request = self.youtubeCore.commentThreads().insert(
                part = 'snippet',
                body = request_body
            )
        
            try:
                response = request.execute()
                print(response)
            except errors.HttpError as err:
                print('There was an error creating the model. Check the details:')
                print(err._get_reason())
                pass
        
    def getAllItems(self):
        data = []
        pageToken = ""
        while True:
            # res = youtube.search().list(
            #     q='Fishing',
            #     part='snippet',
            #     type='channel',
            #     maxResults=50,
            #     pageToken = pageToken if pageToken!= '' else ''
            # ).execute()
            res = self.youtubeCore.playlistItems().list(
                part="snippet,contentDetails",
                maxResults=50,
                pageToken = pageToken if pageToken != "" else "",
                playlistId = self.channelID
            ).execute()
            v = res.get('items', [])
            if v:
                data.extend(v)
            pageToken = res.get('nextPageToken')
            if not pageToken:
                break
            
        return data