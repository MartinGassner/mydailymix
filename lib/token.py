import requests, base64, json, os
from dotenv import Dotenv

dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
refreshToken = dotenv['REFRESH_TOKEN']
clientID = dotenv['CLIENT_ID']
clientSecret = dotenv['CLIENT_SECRET']

def newAccessToken():
    base64Val = base64.b64encode(clientID + ":" + clientSecret)
    headers = {"Authorization": "Basic %s" % base64Val}
    tokenRefreshUrl = "https://accounts.spotify.com/api/token"
    payload = {"grant_type": "refresh_token", "refresh_token": refreshToken, }
    res = requests.post(tokenRefreshUrl, headers=headers, data=payload)
    return str(json.loads(res.text)["access_token"])
