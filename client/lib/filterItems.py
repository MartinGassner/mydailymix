
def genres(items):
    filteredGenres = []
    for item in items:
        for genre in item["genres"]:
            if not genre in filteredGenres:
                filteredGenres.append(genre)
    return filteredGenres

def tracks(items):
    filteredTracks = []
    for item in items:
        if not item["id"] in filteredTracks:
            filteredTracks.append(item["id"])
    return filteredTracks