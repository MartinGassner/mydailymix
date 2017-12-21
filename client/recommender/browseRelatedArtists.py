from lib import filterItems, artists

def find(accessToken, topArtists, topWhiteListGenres, numReq, numTrPerReq):
    filteredArtists = filterItems.tracks(topArtists["items"])
    relatedArtists = artists.getRelated(accessToken, filteredArtists, topWhiteListGenres, numReq, numTrPerReq)
    return relatedArtists
