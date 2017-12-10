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
    "comic"
]


def genres(items):
    filteredGenres = []
    for item in items:
        for genre in item["genres"]:
            if not genre in filteredGenres and not genre in excludedGenres:
                filteredGenres.append(genre)
    return filteredGenres


def tracks(items):
    filteredTracks = []
    for item in items:
        if not item["id"] in filteredTracks:
            filteredTracks.append(item["id"])
    return filteredTracks


def artists(items):
    filteredArtists = []
    for item in items:
        if not item["id"] in filteredArtists:
            filteredArtists.append(item["id"])
    return filteredArtists
