from rest_framework import serializers

from core import models


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thing
        fields = '__all__'
