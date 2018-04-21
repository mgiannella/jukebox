class Song:
    def __init__(self, name, album, artist, URI):
        self.info = {
            'album': album,
            'artist': artist,
            'name': name,
            'uri': URI,
            'score': -1
        }
    def upvote(self):
        self.info['score']+=1
    def downvote(self):
        self.info['score']-=1