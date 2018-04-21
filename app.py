import requests
from flask import Flask, render_template, request
from song import Song
import spotify
app = Flask(__name__)

@app.route('/') #Queue
def index():
    return render_template('index.html')
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['SongSearch']
        print(query)
        url = 'https://api.spotify.com/v1/search'
        payload = {'q':query, 'type':'track', 'market':'US', 'limit':5}
        print(requests.get(url, params = payload, headers = spotify.auth()).content)
    return render_template('search.html') 
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=8000, debug=True)
