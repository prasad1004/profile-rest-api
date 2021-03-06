from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIview"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializers a user profile object"""


    class Meta:
         model = models.UserProfile
         fields =('id', 'email', 'name' 'password')
         extra_kwargs = {
             'password': {
                 'write_only': True,
                 'style': {'input_type': 'password'}

             }
         }

    def create(self, validated_data):
        # sourcery skip: inline-immediately-returned-variable
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

