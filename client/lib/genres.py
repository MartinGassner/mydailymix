import requests, json
from utils import buildQuery
from lib import filterItems

rootParams = {
    "endpoint": "",
    "token": None
}

def getGenreWhitelist(token):
    queryParams = rootParams.copy()
    queryParams["token"] = token
    queryParams["endpoint"] = "/recommendations/available-genre-seeds"
    query = buildQuery(queryParams)
    res = requests.get(url=query["url"], headers=query["header"])
    return json.loads(res.text)

def getTopWhiteGenres(topArtists, whiteListGenres):
    topWhiteListGernres = []
    filteredGenres = filterItems.genres(topArtists["items"])
    for whiteListGenre in whiteListGenres["genres"]:
        if whiteListGenre in filteredGenres:
            topWhiteListGernres.append(whiteListGenre)
    return topWhiteListGernres

def getTopFilteredGenres(topArtists, whiteListGenres):
    filteredGenres = filterItems.genres(topArtists["items"])
    for filteredGenre in filteredGenres:
        if filteredGenre in whiteListGenres["genres"]:
            filteredGenres.remove(filteredGenre)
    return filteredGenres
