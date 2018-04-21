import requests
from flask import Flask, render_template, request, redirect
from song import Song
import json
import spotify
from Queue import Queue

app = Flask(__name__)
songs = Queue()
searchResults = []

@app.route('/') #Queue
def index():
    print(songs.size)
    np = songs.get()
    songArra = songs.queue
    if np != None:
        songs.add(np)
    return render_template('queue.html', songArray=songArra, size=songs.size, nowPlaying=np)
        


@app.route('/search', methods=['GET', 'POST'])
def search():
    global searchResults
    if request.method == 'POST':
        searchResults.clear()
        query = request.form['SongSearch']
        url = 'https://api.spotify.com/v1/search'
        payload = {'q':query, 'type':'track', 'market':'US', 'limit':5}
        r = requests.get(url, params = payload, headers = spotify.auth())
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

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=8000, debug=True)