import requests, json, random
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "payload": {},
    "params": {
        "type": None,
        "q": None
    }
}

def getSearchQuery(searchList):
    return ('genre:"' + random.choice(searchList) + '"')

def by(token, type, searchList):
    queryParams = rootParams.copy()
    res = []
    for i in xrange(4):
        queryParams["params"]["q"] = getSearchQuery(searchList)
        queryParams["params"]["type"] = type
        queryParams["endpoint"] = "/search"
        queryParams["token"] = token
        query = buildQuery(queryParams)
        response = requests.get(url=query["url"], headers=query["header"])
        responseJson = json.loads(response.text)
        if str(type + "s") in responseJson:
            try:
                res.append(random.choice(responseJson["artists"]["items"]))
            except:
                continue
    return res
