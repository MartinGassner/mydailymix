
def genres(items):
    filteredGenres = []
    for item in items:
        for genre in item["genres"]:
            if not genre in filteredGenres:
                filteredGenres.append(genre)
    return filteredGenres
