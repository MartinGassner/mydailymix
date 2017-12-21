from lib import filterItems, tracks

def find(accessToken, topTracks, numReq, numTrPerReq):
    filteredTracks = filterItems.tracks(topTracks["items"])
    relatedTracks = tracks.getRelated(accessToken, filteredTracks, numReq, numTrPerReq)
    return relatedTracks
