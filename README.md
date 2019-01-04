# MyDailyMix

MyDailyMix is a python recommender to create a daily mix according to the spotify feature [Discover Weekly](https://support.spotify.com/uk/using_spotify/playlists/discover-weekly/). Several features of the spotify api are used to retrieve relevant tracks (e.g. [Get a User's Top Artists and Tracks](https://developer.spotify.com/web-api/get-users-top-artists-and-tracks/))

## Requirements
The following steps are needed to use this project.

1. make sure you have a spotify account
2. get Client ID and Client Secret by creating a [new application](https://beta.developer.spotify.com/dashboard/)
3. retrieve a refresh token and a access token by following [this tutorial](https://developer.spotify.com/web-api/tutorial/)

Note: it's necessary that you set `user-top-read user-read-recently-played playlist-modify-private playlist-read-private user-library-read` as scope.

4. create a playlist called "mydailymix" and query its ID 
```
curl -X GET "https://api.spotify.com/v1/me/playlists" -H "Authorization: Bearer {your access token}"
```

5. create a .env file in the root directory:
```
REFRESH_TOKEN = "your refresh token"
CLIENT_ID = "your client id token"
CLIENT_SECRET = "your client secret"
PLAYLIST_ID = "the playlist id of 'mydailymix'"
USER_ID = "should be your user name"
```
## Usage
Run the recommender with `python main.py` from the root directory.

To configure **MyDailyMix** you can edit the `config.json`.
