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

def getTopGenreSeeds(filteredGenres, genreSeeds):
    topGenreSeeds = []
    for genreSeed in genreSeeds["genres"]:
        if genreSeed in filteredGenres:
            try:
                topGenreSeeds.append(genreSeed)
            except:
                continue
    return topGenreSeeds

def getTopFilteredGenres(filteredGenres, genreSeeds):
    topFilteredGenres = []
    for filteredGenre in filteredGenres:
        if not filteredGenre in genreSeeds["genres"]:
            try:
                topFilteredGenres.append(filteredGenre)
            except:
                continue
    return topFilteredGenres
