from rest_framework import serializers
from . import Technology


class BaseTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Technology
        fields = ('name', 'id')


class TechnologySerializer(serializers.ModelSerializer):
    tech_count = serializers.IntegerField()

    class Meta:
        model = Technology
        fields = ('name', 'id', 'tech_count')
