baseUrl = "https://api.spotify.com/v1"

def setHeader(token):
    header = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
    return header

def setUrl(queryParams):
    url = baseUrl + queryParams["endpoint"]
    if "params" in queryParams:
        url += "?"
        for i, (pk, pv) in enumerate(queryParams["params"].iteritems()):
            if i != 0:
                url += "&"
            url += pk + "=" + str(pv)
    return url

def setPayload(payload):
    data = {}
    if "uris" in payload:
        data["uris"] = payload["uris"]
    return data

def buildQuery(queryParams):
    query = {
        "header": setHeader(queryParams["token"]),
        "url": setUrl(queryParams)
    }
    if "payload" in queryParams:
        query["payload"] = setPayload(queryParams["payload"])
    return query

