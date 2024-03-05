from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    processed = serializers.ReadOnlyField()

    class Meta:
        model = File
        fields = "__all__"
