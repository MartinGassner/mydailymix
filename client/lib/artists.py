import requests, json
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None
}

def topTracks(token, id):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = "/artists/" + id + "/top-tracks?country=DE"
    queryParams["token"] = token
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)