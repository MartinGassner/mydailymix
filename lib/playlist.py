import requests, json, os
from dotenv import Dotenv
from utils import buildQuery

dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
playlistID = dotenv['PLAYLIST_ID']
userID = dotenv['USER_ID']

rootParams = {
    "endpoint": "",
    "token": None,
    "payload": {
        "uris": []
    }
}

def replaceTracks(token, trackUris):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = ("/users/" + userID + "/playlists/" + playlistID + "/tracks")
    queryParams["token"] = token
    queryParams["payload"]["uris"] = trackUris
    query = buildQuery(queryParams)
    requests.put(url=query["url"], headers=query["header"], data=json.dumps(query["payload"]))
