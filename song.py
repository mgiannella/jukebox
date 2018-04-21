class Song:
    def __initi__(self, name, album, artist, URI):
        self.name = name,
        self.album = album,
        self.artist = artist,
        self.uri = URI,
        self.score = 1,
    def upvote(self):
        self.score +=1
    def downvote(self):
        self.score -=1
