import requests, json, random
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
        "limit": 10
    }
}

def getRandTracks(topTracks):
    seedTracks = []
    for j in xrange(3):
        seedTracks = random.choice(topTracks)
    return seedTracks

def getRelated(token, topTracks):
    queryParams = rootParams.copy()
    queryParams["token"] = token
    queryParams["endpoint"] = "/recommendations"
    for i in xrange(5):
        queryParams["payload"]["seed_tracks"] = getRandTracks(topTracks)
        query = buildQuery(queryParams)
        res = requests.get(url=query["url"], headers=query["header"])
        return json.loads(res.text)