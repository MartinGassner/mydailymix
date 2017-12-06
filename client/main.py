import requests, json
from lib import token, tracks, playlist, favorites
from recommender import randTopRelatedArtists

if __name__ == '__main__':
    accessToken = token.newAccessToken()
    randTopRelatedArtistsTracks = randTopRelatedArtists.find(accessToken)
    playlist.replaceTracks(accessToken, randTopRelatedArtistsTracks)
    print "ready"