import requests, json
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "payload": {
        "timeRange": None,
        "limit": 10
    }
}

def getFavs(token):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = "/me/top/tracks"
    queryParams["token"] = token
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"], data=query["payload"])
    return json.loads(res.text)