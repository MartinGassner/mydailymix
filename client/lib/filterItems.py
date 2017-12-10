excludedGenres = [
    "reading",
    "hoerspiel",
    "motivation",
    "poetry",
    "prank",
    "kabarett",
    "drama",
    "oratory",
    "spoken word",
    "kindermusik",
    "guidance",
    "deep comedy",
    "comedy",
    "comic",
    "christmas"
]


def genres(items):
    filteredGenres = []
    for item in items:
        for genre in item["genres"]:
            if not genre in filteredGenres and not genre in excludedGenres:
                try:
                    filteredGenres.append(genre)
                except:
                    continue
    return filteredGenres


def tracks(items):
    filteredTracks = []
    for item in items:
        if not item["id"] in filteredTracks:
            try:
                filteredTracks.append(item["id"])
            except:
                continue
    return filteredTracks


def artists(items):
    filteredArtists = []
    for item in items:
        if not item["id"] in filteredArtists:
            try:
                filteredArtists.append(item["id"])
            except:
                continue
    return filteredArtists
