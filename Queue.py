from song import Song

class Queue: 
    def __init__(self): 
        self.queue = []
        self.size = 0
        self.nowPlaying = None

    def add(self, Song): 
        if self.size == 0: 
            self.nowPlaying = Song
        else: 
            duplicate = False
            for item in self.queue: 
                song_uri = item.info['uri']
                if Song.info['uri'] == song_uri: 
                    item.info['score'] += 1
                    duplicate = True
            if duplicate == False: 
                self.queue.append(Song)
                self.size +=1 
            self.queue.sort(key = lambda s: s.info['score'], reverse = True)
    
    def get(self): 
        return self.queue[0]
    
    def upvote(self, URI): 
        for item in self.queue: 
            if item.info['uri'] == URI.info['uri']: 
                item.info['score'] += 1
        self.queue.sort(key = lambda s: s.info['score'], reverse = True)
    
    def downvote(self, URI): 
        for item in self.queue: 
            if item.info['uri'] == URI.info['uri']: 
                item.info['score'] -= 1
        self.queue.sort(key = lambda s: s.info['score'], reverse = True)

    def size(self): 
        return self.size
    
