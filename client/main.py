import random, time
from lib import token, playlist, favorites, genres
from recommender import randTopRelatedArtists, browseRelatedTracks, browseRelatedArtists

time_ranges = ["short_term", "medium_term", "long_term"]

if __name__ == '__main__':
    start_time = time.time()
    tracks = []
    accessToken = token.newAccessToken()
    for tr in time_ranges:
        topArtists = favorites.getFavs(accessToken, "artists", tr)
        topTracks = favorites.getFavs(accessToken, "tracks", tr)
        whiteListGenres = genres.getGenreWhitelist(accessToken)
        topFilteredGenres = genres.getTopFilteredGenres(topArtists, whiteListGenres)
        topWhitelistGenres = genres.getTopWhiteGenres(topArtists, whiteListGenres)
        tracks += browseRelatedArtists.find(accessToken, topArtists, topWhitelistGenres)
        tracks += randTopRelatedArtists.find(accessToken, topFilteredGenres)
        tracks += browseRelatedTracks.find(accessToken, topTracks)
        random.shuffle(tracks)
    playlist.replaceTracks(accessToken, tracks)
    print "Your playlist is ready!"
    print("Execution took %s seconds" % (time.time() - start_time))
