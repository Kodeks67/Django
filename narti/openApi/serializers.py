from rest_framework import serializers
from account.models import Comics


class ComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ('id', 'title')
