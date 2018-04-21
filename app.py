import requests
from flask import Flask, render_template, request
from song import Song
import json
import spotify
app = Flask(__name__)
songs = []
searchResults = []

@app.route('/') #Queue
def index():
    songs.append(Song('Nice', 'Drake', 'Drake', 'URIex'))
    songs.append(Song('Nice', 'Drake', 'Drake', 'URIex'))
    return render_template('queue.html', songArray=songs)

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

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=8000, debug=True)