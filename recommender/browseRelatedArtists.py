from lib import filterItems, artists

def find(accessToken, topFilteredArtists, topWhiteListGenres, numReq, numTrPerReq):
    uniqueArtists = filterItems.tracks(topFilteredArtists)
    relatedArtists = artists.getRelated(accessToken, uniqueArtists, topWhiteListGenres, numReq, numTrPerReq)
    return relatedArtists
