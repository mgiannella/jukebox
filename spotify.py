import secrets
from song import Song
import json
def auth():
    header = {'Authorization': 
        'Bearer {}'.format(secrets.access_token)
        }
    return header

def saveResults(r):
    results = []
    json = r
    songs=json["tracks"]["items"]
    for i in range(0,5):
        title = songs[i]["name"]
        album = songs[i]["album"]["name"]
        artwork = songs[i]["album"]["images"][0]["url"]
        artist = songs[i]["artists"][0]["name"]
        uri = songs[i]["id"]
        explicit = songs[i]["explicit"]
        results.append(Song(title, album, artwork, artist, uri, explicit))
    return results
