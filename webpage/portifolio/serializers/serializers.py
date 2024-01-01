from rest_framework import serializers
from . import models as proj_models


class LatestArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = proj_models.Article
        fields = ('title', 'created_at', 'description', 'url')


class LatestStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = proj_models.Study
        fields = ('title', 'created_at', 'description', 'url')
