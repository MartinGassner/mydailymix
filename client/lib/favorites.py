import requests, json
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "params": {
        "limit": 20
    }
}

def getFavs(token, type):
    queryParams = rootParams.copy()
    queryParams["endpoint"] = ("/me/top/" + type)
    queryParams["token"] = token
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)