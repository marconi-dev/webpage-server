from rest_framework import serializers
from .models import ProfileLink, Profile


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ProfileLink
        fields = ('url', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True)

    class Meta:
        model  = Profile
        fields = ('image', 'name', 'titles', 'links')
