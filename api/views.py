from django.shortcuts import render
from rest_framework import viewsets
from api import serializers
from core import models
from django.http import Http404


class ThingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ThingSerializer

    def get_queryset(self):
        if self.request.headers['X-Company'] != 'kaleido':
            raise Http404
        return models.Thing.objects.all()
