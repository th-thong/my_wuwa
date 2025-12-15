from rest_framework import serializers
from .models import GameAccount

class GameAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for representing a GameAccount.
    """
    class Meta:
        model = GameAccount
        fields = ['id','uid','oauth_code']
        extra_kwargs = {
            'uid': {'read_only': True},
            'id': {'read_only': True},
            'oauth_code': {'read_only': True},
        }


class CreateGameAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for creating or updating a GameAccount.
    'oauth_code' is optional.
    """
    oauth_code = serializers.CharField(
        allow_blank=True, 
        required=False, 
        write_only=False,
        help_text="Optional authorization code."
    )

    class Meta:
        model = GameAccount
        fields = ('id','uid', 'oauth_code')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):

        user = validated_data.pop('user')

        game_account, created = GameAccount.objects.get_or_create(
            user=user,
            uid=validated_data.get('uid'),
            defaults={'oauth_code': validated_data.get('oauth_code', None)}
        )
        return game_account
    
class ChangeGameAccountInfo(serializers.ModelSerializer):
    class Meta:
        model = GameAccount
        fields = ['id','uid', 'oauth_code']
        extra_kwargs = {
            'uid': {'read_only': True},
            'id': {'read_only': True},
        }
