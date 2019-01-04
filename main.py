import random, time, json, os, requests
from lib import token, playlist, favorites, genres, filterItems, saved
from recommender import randTopRelatedArtists, browseRelatedTracks, browseRelatedArtists

def loadConfig():
    with open(os.path.join(os.path.dirname(__file__), 'config.json')) as json_file:
        return json.load(json_file)

def getTimeRanges(timeRanges):
    trs = []
    for tr, trv in timeRanges.iteritems():
        if trv == True:
            trs.append(tr)
    return trs


if __name__ == '__main__':
    start_time = time.time()
    config = loadConfig()
    timeRanges = getTimeRanges(config["timeRanges"])
    limit = config["limit"]
    tracks = []
    accessToken = token.newAccessToken()
    genreSeeds = genres.getGenreWhitelist(accessToken)
    for tr in timeRanges:
        topArtists = favorites.getFavs(accessToken, "artists", tr, limit)
        topFilteredArtists = filterItems.artists(topArtists["items"], config["excludedGenres"])
        topTracks = favorites.getFavs(accessToken, "tracks", tr, limit)
        filteredGenres = filterItems.genres(topArtists["items"], config["excludedGenres"])
        topFilteredGenres = genres.getTopFilteredGenres(filteredGenres, genreSeeds)
        topGenreSeeds = genres.getTopGenreSeeds(filteredGenres, genreSeeds)
        if config["recommender"]["browseRelatedArtists"]["status"] == True:
            recommender = config["recommender"]["browseRelatedArtists"]
            tracks += browseRelatedArtists.find(accessToken, topFilteredArtists, topGenreSeeds, recommender["numRequests"], recommender["numTracksPerRequest"])
        if config["recommender"]["browseRelatedTracks"]["status"] == True:
            recommender = config["recommender"]["browseRelatedTracks"]
            tracks += browseRelatedTracks.find(accessToken, topTracks, recommender["numRequests"], recommender["numTracksPerRequest"])
        if config["recommender"]["randTopRelatedArtists"]["status"] == True:
            recommender = config["recommender"]["randTopRelatedArtists"]
            tracks += randTopRelatedArtists.find(accessToken, topFilteredGenres, recommender["numRequests"])
        random.shuffle(tracks)
    if config["excludeSaved"]:
        tracks = saved.getUnsaved(accessToken, tracks)
    if len(tracks) > config["maxNumOfTracks"]:
        tracks = tracks[0:config["maxNumOfTracks"]-1]
    playlist.replaceTracks(accessToken, tracks)
    print "Your playlist is ready!"
    print("Execution took %s seconds" % (time.time() - start_time))
