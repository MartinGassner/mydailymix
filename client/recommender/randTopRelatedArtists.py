from lib import searchItems, filterItems, artists

def find(accessToken, topArtists):
    filteredGenres = filterItems.genres(topArtists["items"])
    randRelatedArtists = searchItems.by(accessToken, "artist", filteredGenres)
    topTracks = []
    for artist in randRelatedArtists:
        topArtistTracks = artists.topTracks(accessToken, artist["id"])
        topTracks.append(topArtistTracks["tracks"][0]["uri"])
    return topTracks