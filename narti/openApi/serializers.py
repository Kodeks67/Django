from rest_framework import serializers
from account.models import Comics


class LanguageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)
    abbr = serializers.CharField(max_length=3)


class ComicsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    language = serializers.CharField(max_length=15)
    gender = serializers.CharField(max_length=4)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.language = validated_data.get("language", instance.language)
        instance.gender = validated_data.get("gender", instanse.gender)
        instance.save()
        return instance

    def create(self, validated_data):
        return Comics.objects.create(**validated_data)
