import requests, json
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
        "limit": 50
    }
}

def getFavs(token, type, tr, limit):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = ("/me/top/" + type)
    queryParams["token"] = token
    queryParams["params"]["time_range"] = tr
    queryParams["params"]["limit"] = limit
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)
