from rest_framework import serializers
from .models import Feeds


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = ['id', 'title', 'link', 'updated', 'summary', 'content']

