import random
from lib import token, playlist, favorites, genres
from recommender import randTopRelatedArtists, browseRelatedTracks, browseRelatedArtists

if __name__ == '__main__':
    tracks = []
    accessToken = token.newAccessToken()
    topArtists = favorites.getFavs(accessToken, "artists")
    topTracks = favorites.getFavs(accessToken, "tracks")
    whiteListGenres = genres.getGenreWhitelist(accessToken)
    topFilteredGenres = genres.getTopFilteredGenres(topArtists, whiteListGenres)
    topWhitelistGenres = genres.getTopWhiteGenres(topArtists, whiteListGenres)
    tracks += browseRelatedArtists.find(accessToken, topArtists, topWhitelistGenres)
    tracks += randTopRelatedArtists.find(accessToken, topFilteredGenres)
    tracks += browseRelatedTracks.find(accessToken, topTracks)
    random.shuffle(tracks)
    playlist.replaceTracks(accessToken, tracks)
    print "ready"