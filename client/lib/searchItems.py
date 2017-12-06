import requests, json, random
from utils import buildQuery

rootParams = {
    "endpoint": "",
    "token": None,
    "payload": {}
}

def getSearchQuery(searchList):
    return ('genre:"' + random.choice(searchList) + '"')

def by(token, type, searchList):
    queryParams = rootParams.copy()
    res = []
    for i in xrange(20):
        searchQuery = getSearchQuery(searchList)
        queryParams["endpoint"] = ("/search?type=" + type + "&q=" + searchQuery)
        queryParams["token"] = token
        query = buildQuery(queryParams)
        response = requests.get(url=query["url"], headers=query["header"])
        responseJson = json.loads(response.text)
        if str(type + "s") in responseJson:
            res.append(random.choice(responseJson["artists"]["items"]))
    return res