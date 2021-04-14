from rest_framework import serializers

from .models import Media

class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ('m_id', 'title', 'genre', 'release_date', 'cover_art_url')
