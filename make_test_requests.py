# this is a file that tries to make a post request and fails miserably


import random
import requests
import secrets



url = 'http://127.0.0.1:8000/user/123/'
resp = requests.delete(url=url)
print('user delete', resp)
url = 'http://127.0.0.1:8000/media/123123123/'
resp = requests.delete(url=url)
print('media delete', resp)
url = 'http://127.0.0.1:8000/room/7767667/'
resp = requests.delete(url=url)
print('room delete', resp)


data = {'userId': 123,
        'name': 'asdf qwer'}

# Create a user
url = 'http://127.0.0.1:8000/user/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())



data = {'title': 'Harry Potter',
        'mediaId': 123123123, #random.randint(1,2**31)-1,
        'genre': 'Fantasy',
        'releaseDate': '2000-01-01',
        'coverArtUrl': secrets.token_urlsafe(32),
        'runningTime': random.randint(0,60)+random.randint(0,120)+45,
        'director': 'me',
        'isMovie': True, # For some reason the isMovie parameter is unseen
}

# Create a media
url = 'http://127.0.0.1:8000/media/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())


data = {'roomId': 7767667,
        'passcode': 'passcode',
        'hostId': 123}

# Create a room
url = 'http://127.0.0.1:8000/room/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())


data = {'mediaId': 123123123,
        'userId': 123,
        'likes': True}

# Create a response
url = 'http://127.0.0.1:8000/response/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())


data = {'mediaId': 123123123,
        'userId': 123,
        'rating': 10,
        'comment': "worst movie i've ever watched"}

# Create a review
url = 'http://127.0.0.1:8000/review/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())




data = {'roomId': 7767667,
        'userId': 123}

# Join a room
url = 'http://127.0.0.1:8000/join/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())



data = {'roomId': 7767667,
        'userId': 123}

# Leave a room
url = 'http://127.0.0.1:8000/leave/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())


import time

data = {'userId': 123,
        'mediaId': 123123123,
        'time': 1616161616}

# Blacklist a media from showing up again
url = 'http://127.0.0.1:8000/blacklist/'
resp = requests.post(url=url, data=data)

print(resp)
print(resp.content.decode())

