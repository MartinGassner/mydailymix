import requests, json
from lib import token, tracks, playlist, favorites
from recommender import randTopRelatedArtists, browseRelatedTracks

if __name__ == '__main__':
    accessToken = token.newAccessToken()
    topArtists = favorites.getFavs(accessToken, "artists")
    randTopRelatedArtistsTracks = randTopRelatedArtists.find(accessToken, topArtists)
    #topTracks = favorites.getFavs(accessToken, "tracks")
    #browseRelatedTracks = browseRelatedTracks.find(accessToken, topTracks)
    playlist.replaceTracks(accessToken, randTopRelatedArtistsTracks)
    print "ready"