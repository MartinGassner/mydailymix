import requests, json
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
        "limit": 50
    }
}


def querySaved(token, trackIds):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = "/me/tracks/contains"
    queryParams["token"] = token
    queryParams["params"]["ids"] = ','.join(trackIds)
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)


def filterUnsaved(token, tracks):
    saved = querySaved(token, tracks)
    return ["spotify:track:" + trackId for idx, trackId in enumerate(tracks) if not saved[idx]]



def getUnsaved(token, tracks):
    trackIDs = [trackUri.split(':')[-1] for trackUri in tracks]
    unsavedTracks = []
    n = 0

    for idx, trackID in enumerate(trackIDs):
        if ((idx + 1) % 50) == 0 or (idx + 1) == len(trackIDs):
            unsavedTracks += filterUnsaved(token, trackIDs[n:idx])
            n = idx

    return unsavedTracks
