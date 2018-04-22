import requests
from bs4 import BeautifulSoup
from song import Song
from time import sleep
CONST_IP_OF_SPEAKER = 'http://192.168.1.251:8090'

def play(song):
    data = '<ContentItem source="SPOTIFY" type="uri" sourceAccount="mikegiannella" location="spotify:track:{}"><itemName>{}</itemName></ContentItem>'.format(song.info['uri'],song.info['name'])
    requests.post(CONST_IP_OF_SPEAKER+'/select', data)

# Gets time remaining in seconds
def getTime():
    r = requests.get(CONST_IP_OF_SPEAKER+'/now_playing')
    soup = BeautifulSoup(r.text, 'lxml')
    time=soup.find('time')
    totalTime = int(time['total'])
    timeElapsed = int(time.text)
    return (totalTime-timeElapsed)
