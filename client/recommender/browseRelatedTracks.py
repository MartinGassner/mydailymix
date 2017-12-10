from lib import filterItems, tracks

def find(accessToken, topTracks):
    filteredTracks = filterItems.tracks(topTracks["items"])
    relatedTracks = tracks.getRelated(accessToken, filteredTracks)
    return relatedTracks
