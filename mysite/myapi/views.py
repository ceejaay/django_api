from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import HeroSerializer, VillianSerializer
from .models import Hero, Villian

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class VillianViewSet(viewsets.ModelViewSet):
    queryset = Villian.objects.all().order_by('name')
    serializer_class = VillianSerializer
