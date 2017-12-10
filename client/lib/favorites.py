import requests, json
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
        "limit": 30
    }
}

def getFavs(token, type, tr):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = ("/me/top/" + type)
    queryParams["token"] = token
    queryParams["params"]["time_range"] = tr
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)
