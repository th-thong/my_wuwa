from rest_framework import serializers
from .models import WebAccount

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebAccount
        fields = ('email', 'password')