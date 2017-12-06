import requests, json
from dotenv import Dotenv
from utils import buildQuery

dotenv = Dotenv('.env')
playlistID = dotenv['PLAYLIST_ID']
userID = dotenv['USER_ID']

rootParams = {
    "endpoint": "",
    "token": None,
    "payload": {
        "uris": []
    }
}

def setUris(items):
    uriList = []
    for item in iter(items):
        uriList.append(item['uri'])
    return uriList

def replaceTracks(token, tracks):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = ("/users/" + userID + "/playlists/" + playlistID + "/tracks")
    queryParams["token"] = token
    queryParams["payload"]["uris"] = setUris(tracks["items"])
    query = buildQuery(queryParams)
    requests.put(url=query["url"], headers=query["header"], data=json.dumps(query["payload"]))