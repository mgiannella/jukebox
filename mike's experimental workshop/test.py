from song import Song
from flask import Flask, render_template, request
 
app = Flask(__name__)
songs = []
@app.route('/downvote/<uri>')
def downvote(uri):
    for song in songs:
        if(song.info['uri'] == uri):
            song.downvote()
    return render_template('base.html', songArray=songs)
@app.route('/')
@app.route('/queue')
def hello_world():
    songs.append(Song('Nice for Waht', 'No', 'Drake', 'hi'))
    songs.append(Song('Nice for Waht', 'No', 'Drake', 'eh'))
    songs.append(Song('Nice for Waht', 'No', 'Drake', 'no'))
    return render_template('base.html', songArray=songs)

if __name__ == '__main__':
    app.run()