from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""

    name = serializers.CharField(max_length = 10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        #To make password visible only when object is created not in viewing object
        extra_kwargs = {
            'password': {
                #'last_login': {'read_only': True},
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
