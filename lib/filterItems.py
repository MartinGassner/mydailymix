def genres(items, excludedGenres):
    filteredGenres = []
    for item in items:
        for genre in item["genres"]:
            if len(list(set(genre.split()).intersection(excludedGenres))) == 0:
                genre = genre.replace(' ', '-').lower()
                if not genre in filteredGenres:
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
