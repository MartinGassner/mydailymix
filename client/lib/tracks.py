import requests, json, random
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
        "limit": 30
    }
}

def getRandTracks(topTracks):
    seedTracks = ""
    for j in xrange(3):
        if j != 0:
            seedTracks += ","
        seedTracks += random.choice(topTracks)
    return seedTracks

def getRelated(token, topTracks):
    queryParams = rootParams.copy()
    queryParams["token"] = token
    queryParams["endpoint"] = "/recommendations"
    relatedTracks = []
    for i in xrange(5):
        queryParams["params"]["seed_tracks"] = getRandTracks(topTracks)
        query = buildQuery(queryParams)
        res = requests.get(url=query["url"], headers=query["header"])
        resJson = json.loads(res.text)
        for i, track in enumerate(resJson["tracks"]):
            if i < 3 and not track["uri"] in relatedTracks:
                relatedTracks.append(track["uri"])
    return relatedTracks