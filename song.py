class Song:
    def __init__(self, name, album, artwork, artist, URI, explicit):
        self.info = {
            'album': album,
            'artwork': artwork,
            'artist': artist,
            'name': name,
            'uri': URI,
            'score': 1,
            'explicit': explicit
        }

