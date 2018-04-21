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
    songs=json['tracks']['items']
    for i in range(0,5):
        uri = songs[i]['id']
        album = songs[i]['album']['name']
        artist = songs[i]['artists']['name']
        title = songs[i]['name']
        results[i] = Song(title, album, artist, uri)
        print(uri)
        print(album)
        print(artist)
        print(title)
    return results
