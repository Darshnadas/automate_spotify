import os
import json

import requests

import google_auth_outhlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

from exceptions import ResponseException
from secrets import spotify_token,spotify_user_id

class CreatePlaylist:
    
    def __init__(self):
        self.youtube_client = self.get_youtube_client()
        

#Step 1: Log Into YouTube
    def get_youtube_client(self):
        """Log into Youtube"""
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        #Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_outhlib.flow.InstalledAppFlow.from_client_secrets.file(
            client_secrets_file, scopes
        )
        credentials = flow.run_console()

        #from Youtube Data API
        youtube_client = googleapiclient.discovery.build(
            api_service_name,api_version,credentials=credentials
        )

        return youtube_client  


        

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

        query = "https://api.spotify.com/v1/users/{}/playlists".format(spotify_user_id)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type":"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        return response_json("id")
        



#Step 4: Search For The Song
    def get_spotify_uri(self, song_name, artist):

        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers = {
                "Content-Type":"application/jason",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )    
        response_json = response.json()
        songs = response_json['tracks']['items']

        uri = songs[0]['uri']

        return uri  
