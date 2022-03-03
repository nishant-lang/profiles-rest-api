



from rest_framework import serializers

from profile_api import models
class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIview"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer a user profile object"""

    class Meta:  
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}

            }
        }

    def create(self,validated_data):
        """Create and return a new user"""
        user=models.UserProfile.objects.create_user(
           email=validated_data['email'],
           name=validated_data['name'],
           password=validated_data['password']

        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProfilefeedItem
        fields=('id','User_Profile','status_text','created_on')
        
        extra_kwargs={'User_profile':{'read_only':True}}