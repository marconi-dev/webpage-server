from rest_framework import serializers


class LinksSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.URLField()


class ProfileSerializer(serializers.Serializer):
    image = serializers.ImageField()
    name = serializers.CharField()
    titles = serializers.CharField()
    links = LinksSerializer(many=True)
