from django.shortcuts import render
from .serializers import RoomsSerializer
from rest_framework import generics
from .models import Room


class Roomview(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomsSerializer
