import secrets
def auth():
    header = {'Authorization': 
        'Bearer {}'.format(secrets.access_token)
        }
    print(header)
    return header
    