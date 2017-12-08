from lib import filterItems, tracks

rootParams = {
    "endpoint": "",
    "token": None,
    "payload": {}
}

def find(accessToken, topTracks):
    filteredTracks = filterItems.tracks(topTracks["items"])
    relatedTracks = tracks.getRelated(accessToken, filteredTracks)
    return relatedTracks
