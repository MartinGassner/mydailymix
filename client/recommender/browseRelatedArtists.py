from lib import filterItems, artists

def find(accessToken, topArtists, topWhiteListGenres):
    filteredArtists = filterItems.tracks(topArtists["items"])
    relatedArtists = artists.getRelated(accessToken, filteredArtists, topWhiteListGenres)
    return relatedArtists
