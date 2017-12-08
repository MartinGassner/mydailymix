import requests, json
from lib import token, tracks, playlist, favorites
from recommender import randTopRelatedArtists, browseRelatedTracks

if __name__ == '__main__':
    tracks = []
    accessToken = token.newAccessToken()
    topArtists = favorites.getFavs(accessToken, "artists")
    topTracks = favorites.getFavs(accessToken, "tracks")
    tracks += randTopRelatedArtists.find(accessToken, topArtists)
    tracks += browseRelatedTracks.find(accessToken, topTracks)
    playlist.replaceTracks(accessToken, tracks)
    print "ready"