from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Feeds
from .serializers import FeedSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def feed_list(request):
    """
    List all feeds, or create a new feed.
    """
    if request.method == 'GET':
        feeds = Feeds.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def feed_detail(request, pk):
    """
    Retrieve, update or delete induvidial feed.
    """
    try:
        feed = Feeds.objects.get(pk=pk)
    except Feeds.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedSerializer(feed)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedSerializer(feed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
