from rest_framework import serializers
from . import models as proj_models


class ProjectTechnologySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='technology.name')

    class Meta:
        model   = proj_models.ProjectTechnology
        fields  = ('id', 'description', 'name')


class ProjectAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = proj_models.ProjectAsset
        exclude = ('id',)


class ProjDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model   = proj_models.ProjectDetail
        exclude = ('id',)
