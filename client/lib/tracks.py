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

def getRelated(token, topTracks, numReq, numTrPerReq):
    queryParams = rootParams.copy()
    queryParams["token"] = token
    queryParams["endpoint"] = "/recommendations"
    relatedTracks = []
    for i in xrange(numReq):
        queryParams["params"]["seed_tracks"] = getRandTracks(topTracks)
        query = buildQuery(queryParams)
        res = requests.get(url=query["url"], headers=query["header"])
        resJson = json.loads(res.text)
        for i, track in enumerate(resJson["tracks"]):
            if i < numTrPerReq and not track["uri"] in relatedTracks:
                try:
                    relatedTracks.append(track["uri"])
                except:
                    continue
    return relatedTracks
