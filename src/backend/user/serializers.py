from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the active User model
User = get_user_model()

    
class RegisterSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='username',max_length=255)
    
    class Meta:
        model = User
        fields = ['user_name','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class UserInfoSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='username',max_length=255)
    class Meta:
        model = User
        fields = ['id','user_name','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
class ChangeUserInfoSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = ['id','email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True}
        }