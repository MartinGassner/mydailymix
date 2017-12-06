baseUrl = "https://api.spotify.com/v1"

def setHeader(token):
    header = {"Authorization": "Bearer %s" % token, "Content-Type": "application/json"}
    return header

def setUrl(endpoint):
    return baseUrl + endpoint

def setPayload(payload):
    data = {}
    if "limit" in payload:
        data["limit"] = payload["limit"]
    if "timeRange" in payload:
        data["time_range"] = payload["timeRange"]
    if "uris" in payload:
        data["uris"] = payload["uris"]
    return data

def buildQuery(params):
    return {
        "header": setHeader(params["token"]),
        "url": setUrl(params["endpoint"]),
        "payload": setPayload(params["payload"])
    }