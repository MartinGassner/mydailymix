from lib import favorites, searchItems, filterItems, artists

def find(accessToken):
    topArtists = favorites.getFavs(accessToken, "artists")
    filteredGenres = filterItems.genres(topArtists["items"])
    randRelatedArtists = searchItems.by(accessToken, "artist", filteredGenres)
    topTracks = {"items": []}
    for artist in randRelatedArtists:
        topArtistTracks = artists.topTracks(accessToken, artist["id"])
        for i, track in enumerate(topArtistTracks["tracks"]):
            if i < 3 and not track["uri"] in topTracks["items"]:
                topTracks["items"].append({"uri": track["uri"]})
    return topTracks