from django.shortcuts import render
from rest_framework import viewsets
from api import serializers
from core import models

# Create your views here.

class ThingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ThingSerializer
    
    def get_queryset(self):
        return models.Thing.objects.all()
    
