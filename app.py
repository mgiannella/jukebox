import requests
from flask import Flask, render_template, request, redirect
from song import Song
import json
import spotify
import webbrowser
from Queue import Queue
access_token = ''
app = Flask(__name__)
songs = Queue()
searchResults = []
webbrowser.open('https://accounts.spotify.com/authorize/?client_id=def27a12301844df8891ddab406ef2a3&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Flogin')
#Open for authentication

@app.route('/') #Queue
def index():
    #print(songs.nowPlaying.info['name'])
    return render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying)
        
@app.route('/search', methods=['GET', 'POST'])
def search():
    global searchResults
    if request.method == 'POST':
        searchResults.clear()
        query = request.form['SongSearch']
        url = 'https://api.spotify.com/v1/search'
        header = {'Authorization': 
        'Bearer {}'.format(access_token)}
        payload = {'q':query, 'type':'track', 'market':'US', 'limit':5}
        r = requests.get(url, params = payload, headers = header)
        searchResults = spotify.saveResults(r.json())
    return render_template('search.html', searchArray=searchResults)
@app.route('/add/<uri>')
def add(uri):
    global searchResults
    for song in searchResults:
        if song.info['uri'] == uri:
            songs.add(song)
    return redirect("/", code=302)

@app.route('/downvote/<uri>')
def downvote(uri):
    songs.downvote(uri)
    return redirect("/", code=302)

@app.route('/upvote/<uri>')
def upvote(uri):
    songs.upvote(uri)
    return redirect("/", code=302)

def nextSong():
    songs.nowPlaying = songs.get()
    redirect('/', code=302)

@app.route('/login')
def login():
    global access_token
    auth_code = request.args.get('code')
    payload = {'grant_type':'authorization_code', 'code':auth_code, 'redirect_uri':'http://localhost:8000/login',
            'client_id': 'def27a12301844df8891ddab406ef2a3', 'client_secret':'0fce580315d64fc589cfd858a3319614'
        }
    token = requests.post('https://accounts.spotify.com/api/token', data = payload)
    data = token.json()
    access_token = data['access_token']
    print(access_token)
    return redirect("http://localhost:8000")

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=8000, debug=False)