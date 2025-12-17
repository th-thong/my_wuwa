from rest_framework import serializers
from .models import ConvenesLog

class ConvenesLogListSerializer(serializers.ListSerializer):
    
    def create(self, validated_data):
        convene_logs = []

        if not validated_data:
            return []

        for item in validated_data:
            game_account = item.get('game_account')
            time = item.get('time')

            count = ConvenesLog.objects.filter(
                game_account=game_account, 
                time=time
            ).count()

            if count >= 10: 
                continue

            convene_logs.append(ConvenesLog(**item))

        return ConvenesLog.objects.bulk_create(convene_logs)

class ResponseToConveneLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ConvenesLog
        fields = '__all__'
        list_serializer_class = ConvenesLogListSerializer
        extra_kwargs = {
            'game_account': {'read_only': True}
        }

    def create(self, validated_data):
        game_account = validated_data.get('game_account')
        time_val = validated_data.get('time')

        count = ConvenesLog.objects.filter(
            game_account=game_account,
            time=time_val
        ).count()

        if count >= 10:
            return None

        return ConvenesLog.objects.create(**validated_data)