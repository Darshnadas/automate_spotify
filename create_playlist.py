import json
import requests





class CreatePlaylist:
    
    def __init__(self):
        pass

#Step 1: Log Into YouTube
    def get_youtube_client(self):
        pass

#Step 2: Grab our liked videos
    def get_liked_videos(self):
        pass

#Step 3: Create A New Playlist
    def create_playlist(self):
        
        request_body = json.dumps({
            "name": "YouTube Songs",
            "description":"All liked YouTube songs",
            "public": True

        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = request.post(
            query,
            data = request_body,
            headers = {
                "Content-Type":"application/jason",
                "Authorization":"Bearer {}".format(spotify_id)
            }
        )
        response_json = response.jason()

        return response._jason("id")
        



#Step 4: Search For The Song
    def get_spotify_url(self):
        pass


