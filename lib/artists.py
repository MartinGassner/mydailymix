import requests, json, random
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
    }
}

def topTracks(token, id):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = "/artists/" + id + "/top-tracks"
    queryParams["token"] = token
    queryParams["params"]["country"] = "DE"
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)


def getRandArtists(topArtists):
    seedArtists = ""
    for j in xrange(3):
        if j != 0:
            seedArtists += ","
        seedArtists += random.choice(topArtists)
    return seedArtists

def getRandGenres(topWhiteListGenres):
    seedGenres = ""
    for j in xrange(2):
        if j != 0:
            seedGenres += ","
        seedGenres += random.choice(topWhiteListGenres)
    return seedGenres


def getRelated(token, topArtists, topWhiteListGenres, numReq, numTrPerReq):
    queryParams = rootParams.copy()
    queryParams["token"] = token
    queryParams["endpoint"] = "/recommendations"
    relatedArtists = []
    for i in xrange(numReq):
        queryParams["params"]["seed_artists"] = getRandArtists(topArtists)
        queryParams["params"]["seed_genres"] = getRandGenres(topWhiteListGenres)
        query = buildQuery(queryParams)
        res = requests.get(url=query["url"], headers=query["header"])
        resJson = json.loads(res.text)
        for i, track in enumerate(resJson["tracks"]):
            if i < numTrPerReq and not track["uri"] in relatedArtists:
                try:
                    relatedArtists.append(track["uri"])
                except:
                    continue
    return relatedArtists
