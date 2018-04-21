import requests

CONST_IP_OF_SPEAKER = 'http://192.168.1.251:8090'

def play(uri):
    return 'hi'

def getTime():
    r = requests.get(CONST_IP_OF_SPEAKER+'/now_playing')
    print(r.text)

getTime()