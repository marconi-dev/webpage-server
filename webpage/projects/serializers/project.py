from rest_framework import serializers
from . technology import BaseTechnologySerializer
from . import Project, ProjectAsset, ProjectDetail, ProjectTechnology 


class ProjectSerializer(serializers.ModelSerializer):
    technologies = BaseTechnologySerializer(many=True)

    class Meta:
        model  = Project
        fields = '__all__'


class ProjectTechnologySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='technology.name')

    class Meta:
        model   = ProjectTechnology
        fields  = ('id', 'description', 'name')


class ProjectAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ProjectAsset
        exclude = ('id',)


class ProjDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ProjectDetail
        exclude = ('id',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    details = ProjDetailSerializer(many=True)
    assets = ProjectAssetsSerializer(many=True)
    techs = ProjectTechnologySerializer(many=True)

    class Meta:
        model   = Project
        exclude = ('technologies',)
