import requests, json
from lib import token, tracks, playlist

if __name__ == '__main__':
    accessToken = token.newAccessToken()
    topTracks = tracks.getFavs(accessToken)
    playlist.replaceTracks(accessToken, topTracks)
    print "test"