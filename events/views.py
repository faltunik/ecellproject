from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .models import *
from rest_framework.response import Response
import datetime


# our serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

# Create your views here.
@api_view(['GET'])
def get_events(request):
    events = Events.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_event(request, pk):
    try:
        event = Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EventSerializer(event, data=request.data,  partial=True)
    if serializer.is_valid():
        event.modified_at =  datetime.timedelta(seconds=1)
        serializer.save()        
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request, pk):
    try:
        event = Events.objects.get(pk=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_events_yearwise(request, year):
    events = Events.objects.filter(year=year)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


