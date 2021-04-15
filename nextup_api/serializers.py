from rest_framework import serializers

from .models import *

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('mediaId', 'title', 'genre', 'releaseDate', 'coverArtUrl',
                  'isMovie', 'runningTime', 'director', 'seasons', 'episodeCount')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'name', 'isAdmin')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('roomId', 'passcode', 'hostId')

class RoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMember
        fields = ('roomId', 'userId')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('mediaId', 'userId', 'rating', 'comment')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ('mediaId', 'userId', 'isLike')

class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Last_Showed
        fields = ('mediaId', 'userId', 'time')
