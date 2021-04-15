import json
import time

import requests

from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all().order_by('title')
    serializer_class = MediaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('roomId')
    serializer_class = RoomSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('mediaId')
    serializer_class = ReviewSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all().order_by('userId')
    serializer_class = ResponseSerializer

class BlacklistViewSet(viewsets.ModelViewSet):
    queryset = Last_Showed.objects.all().order_by('userId')
    serializer_class = BlacklistSerializer

class RoomMemberViewSet(viewsets.ModelViewSet):
    queryset = RoomMember.objects.all().order_by('userId')
    serializer_class = RoomMemberSerializer
    
    def destroy(self, request, *args, **kwargs):
        entry = RoomMember.objects.filter(userId = kwargs['pk'])
        if entry:
            entry.delete()
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=404)

class ResultsViewSet(viewsets.ViewSet):
    # Sorts all media based off how many users in that room liked it
    # minus the amount that disliked it

    def retrieve(self, request, pk):
        # Get the room
        count = {}
        room = Room.objects.filter(roomId = pk)
        for member in RoomMember.objects.filter(roomId = room[0]).iterator():
            user = member.userId
            # Iterate over users in that room
            for response in Response.objects.filter(userId = user).iterator():
                # Iterate over responses by those users
                inc = 1 if response.isLike else -1
                # Note that .mediaId is actually the Media object, not the id
                if response.mediaId in count:
                    count[response.mediaId] += inc
                else:
                    count[response.mediaId] = inc

        top3 = list(sorted(count.items(), key=lambda x: x[1], reverse=True))[:3]
        datalist = []
        for media, count in top3:
            data = MediaSerializer(media).data
            data['likeCount'] = count
            datalist.append(data)
    
        return HttpResponse(json.dumps({'top3':datalist}, indent=4), status=200)
    

@api_view(['POST', 'DELETE'])
def blacklist(request):
    if request.method == 'POST':
        entry = Last_Showed(userId = request['userId'],
                            mediaId = request['mediaId'],
                            time = request['time'])
        entry.save()

@api_view(['POST', 'DELETE'])
def join(request):
    if request.method == 'POST':
        entry = RoomMember(userId = request['userId'],
                           roomId = request['roomId'])
        entry.save()

@api_view(['POST', 'PUT', 'DELETE'])
def media(request):
    if request.method == 'POST':
        try:
            entry = Media(mediaId = request['mediaId'],
                          title = request['title'],
                          genre = request['genre'],
                          releaseDate = request['releaseDate'],
                          coverArtUrl = request['coverArtUrl'],
                          runningTime = request['runningTime'],
                          director = request['director'],
                          seasons = 0,
                          episodeCount = 0,
                          isMovie = True)
            entry.save()
        except KeyError:
            entry = Media(mediaId = request['mediaId'],
                          title = request['title'],
                          genre = request['genre'],
                          releaseDate = request['releaseDate'],
                          coverArtUrl = request['coverArtUrl'],
                          runningTime = 0,
                          director = '',
                          seasons = request['seasons'],
                          episodeCount = request['episodeCount'],
                          isMovie = False)
            entry.save()
    elif request.method == 'PUT':
        entry = Media.objects.filter(mediaId = request['mediaId'])
        try:
            entry.title = request['title']
            entry.genre = request['genre']
            entry.releaseDate = request['releaseDate']
            entry.coverArtUrl = request['coverArtUrl']
            entry.runningTime = request['runningTime']
            entry.director = request['director']
            entry.seasons = 0
            entry.episodeCount = 0
            entry.isMovie = True
            
        except KeyError:
            entry.title = request['title']
            entry.genre = request['genre']
            entry.releaseDate = request['releaseDate']
            entry.coverArtUrl = request['coverArtUrl']
            entry.runningTime = 0
            entry.director = ''
            entry.seasons = request['seasons']
            entry.episodeCount = request['episodeCount']
            entry.isMovie = False
        entry.save()

@api_view(['POST'])
def response(request):
    if request.method == 'POST':
        entry = Response(mediaId = request['mediaId'],
                         userId = request['userId'],
                         isLike = request['isLike'])
        entry.save()

@api_view(['POST'])
def review(request):
    if request.method == 'POST':
        entry = Review(mediaId = request['mediaId'],
                       userId = request['userId'],
                       rating = request['rating'],
                       comment = request['comment'])
        entry.save()
    elif request.method == 'DELETE':
        entry = Review.objects.filter(mediaId = request['mediaId'],
                                      userId = request['userId'])
        entry.delete()

@api_view(['POST', 'DELETE'])
def room(request):
    if request.method == 'POST':
        entry = Room(roomId = request['roomId'],
                     passcode = request['passcode'],
                     hostId = request['hostId'])
        entry.save()

@api_view(['POST', 'DELETE'])
def user(request):
    if request.method == 'POST':
        entry = User(userId = request['userId'],
                     name = request['name'])
        entry.save()

def results(request, *args, **kwargs):
    pass
