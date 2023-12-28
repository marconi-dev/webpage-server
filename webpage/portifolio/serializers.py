from rest_framework import serializers
from . import models as proj_models


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model  = proj_models.ProfileLink
        fields = ('url', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    links = LinksSerializer(many=True)

    class Meta:
        model  = proj_models.Profile
        fields = ('image', 'name', 'titles', 'links')


class ProjectSerializer(serializers.ModelSerializer):
    tecnologies = serializers.StringRelatedField(many=True)

    class Meta:
        model   = proj_models.Project
        exclude = ('id',)
