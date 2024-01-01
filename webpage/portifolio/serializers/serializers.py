from rest_framework import serializers
from . import detail
from . import models as proj_models


class BaseTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model  = proj_models.Technology
        fields = ('name', 'id')


class TechnologySerializer(serializers.ModelSerializer):
    tech_count = serializers.IntegerField()

    class Meta:
        model = proj_models.Technology
        fields = ('name', 'id', 'tech_count')


class ProjectSerializer(serializers.ModelSerializer):
    tecnologies = BaseTechnologySerializer(many=True)

    class Meta:
        model  = proj_models.Project
        fields = '__all__'


class ProjectDetailSerializer(serializers.ModelSerializer):
    assets  = detail.ProjectAssetsSerializer(many=True)
    techs   = detail.ProjectTechnologySerializer(many=True)
    details = detail.ProjDetailSerializer(many=True)

    class Meta:
        model   = proj_models.Project
        exclude = ('tecnologies',)


class LatestArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = proj_models.Article
        fields = ('title', 'created_at', 'description', 'url')


class LatestStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = proj_models.Study
        fields = ('title', 'created_at', 'description', 'url')
