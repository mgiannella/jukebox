import requests
from flask import Flask, render_template, request, redirect, make_response
from song import Song
import json
import spotify
from Queue import Queue
import datetime
import random, string
from threading import Thread
from bosesoundhooks import play, getTime
import webbrowser
from time import sleep

access_token = ''
app = Flask(__name__)
songs = Queue()
searchResults = []

def generateUname():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@app.route('/') #Queue
def index():
    if request.cookies.get('username') == None:
        resp = make_response(render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying, error=None, errorone=None,errortwo=None))
        resp.set_cookie('username', generateUname(), expires=datetime.datetime.now() + datetime.timedelta(days=30)) 
        return resp 
    return render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying, error=None, errorone=None, errortwo=None)
        
@app.route('/search', methods=['GET', 'POST'])
def search():
    global searchResults
    if request.method == 'POST':
        query = request.form['SongSearch']
        if query == '':
            return render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying, error=None, errorone=None, errortwo='e1')
        url = 'https://api.spotify.com/v1/search'
        header = {'Authorization': 
        'Bearer {}'.format(access_token)}
        payload = {'q':query, 'type':'track', 'market':'US', 'limit':5}
        try:
            r = requests.get(url, params = payload, headers = header)
        except Exception as e:
            print(str(e))
            return redirect('/',code=302)
        searchResultshere = spotify.saveResults(r.json())
        for obj in searchResultshere:
            searchResults.append(obj)
    return render_template('search.html', searchArray=searchResultshere)

@app.route('/add/<uri>')
def add(uri):
    global searchResults
    for song in searchResults:
        if song.info['uri'] == uri:
            name = request.cookies.get('username')
            if songs.add(song, name) == None:
                return redirect("/", code=302)
            else:
               return render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying, error=None, errorone='e1', errortwo=None) 
    

@app.route('/downvote/<uri>')
def downvote(uri):
    if songs.downvote(uri, request.cookies.get('username')) != 'e1':
        return redirect("/", code=302)
    else:
        return render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying, error='e1', errorone=None, errortwo=None)

@app.route('/upvote/<uri>')
def upvote(uri):
    if songs.upvote(uri, request.cookies.get('username')) != 'e1':
        return redirect("/", code=302)
    else:
        return render_template('queue.html', songArray=songs.queue, size=songs.size, nowPlaying=songs.nowPlaying, error='e1', errorone=None, errortwo=None)


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

@app.route('/qrcode')
def displayQR():
    return render_template('qrcode.html')

def worker(x=0):
    if x ==0:
        sleep(10)
    print('working')
    while songs.nowPlaying == None:
        print('Nothing playing')
        sleep(1)
    play(songs.nowPlaying)
    sleep(3)
    a = getTime()
    if (a - 10) > 0:
        sleep(a-10)
    while getTime() > 5:
        sleep(1)
    if songs.size >= 1:
        songs.nowPlaying = songs.get()
        return worker(x+1)
    else:
        return


if __name__ == '__main__':
    print('Starting thread')
    t = Thread(target=worker)
    t.start()
    webbrowser.open('https://accounts.spotify.com/authorize/?client_id=def27a12301844df8891ddab406ef2a3&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Flogin')
    app.run(host = '0.0.0.0', port=8000, debug=False)
    
    