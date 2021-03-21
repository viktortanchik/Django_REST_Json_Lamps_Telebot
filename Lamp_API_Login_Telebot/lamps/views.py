from django.shortcuts import render
from rest_framework import generics
from .serializers import LampsDetailSerializer, LampslistSerializer,ProgramLamps1DetailSerializer,ProgramLamps1listSerializer
from .models import Lamps,ProgramLamps1
# Create your views here.

class LampsCreateView(generics.CreateAPIView):
    serializer_class = LampsDetailSerializer,

class LampsListView(generics.ListAPIView):
    serializer_class =LampslistSerializer
    queryset = Lamps.objects.all()

class LampsDtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LampslistSerializer
    queryset = Lamps.objects.all()

