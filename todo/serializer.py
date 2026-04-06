from rest_framework import serializers 

class TodoSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.BooleanField()
    priority = serializers.CharField()