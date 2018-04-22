from song import Song

class Queue: 
    def __init__(self): 
        self.queue = []
        self.size = 0
        self.nowPlaying = None

    def add(self, Song): 
        if self.size == 0:
            self.nowPlaying = Song
            self.size+=1
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
        if self.size == 0:
            return
        else:
            return self.queue.pop(0)
    
    def upvote(self, URI, name): 
        for item in self.queue: 
            if item.info['uri'] == URI: 
                if name not in item.users:
                    item.info['score'] += 1
                    item.users.append(name)
                else:
                    return 'e1'
        self.queue.sort(key = lambda s: s.info['score'], reverse = True)
        return None
    
    def downvote(self, URI, name): 
        for item in self.queue: 
            if item.info['uri'] == URI: 
                if name not in item.users:
                    item.info['score'] -= 1
                    item.users.append(name)
                else:
                    return 'e1'
        self.queue.sort(key = lambda s: s.info['score'], reverse = True)
        return None


    
