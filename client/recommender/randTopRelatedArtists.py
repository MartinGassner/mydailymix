from lib import searchItems, artists

def find(accessToken, topGenres):
    randRelatedArtists = searchItems.by(accessToken, "artist", topGenres)
    topTracks = []
    for artist in randRelatedArtists:
        topArtistTracks = artists.topTracks(accessToken, artist["id"])
        try:
            topTracks.append(topArtistTracks["tracks"][0]["uri"])
        except:
            continue
    return topTracks
