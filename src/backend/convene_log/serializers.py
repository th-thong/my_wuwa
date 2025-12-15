from rest_framework import serializers
from .models import ConvenesLog


class ConvenesLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ConvenesLog
        fields = '__all__'
