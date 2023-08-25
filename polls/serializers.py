from rest_framework import serializers 
from .models import poll, choice, vote
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token 


class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model= vote
        fields = '__all__'

class ChoiceSerializers(serializers.ModelSerializer):
    votes = VoteSerializers(many=True, required=False)
    class Meta:
        model= choice
        fields = '__all__'


class PollSerializers(serializers.ModelSerializer):
    choices = ChoiceSerializers(many=True, read_only=True, required=False)

    class Meta:
        model= poll
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
     
     class Meta:
         model = User 
         fields = ('username', 'email', 'password')
         extra_kwargs = {'password': {'write_only':True}}
    
     def create(self, validated_date):
         user = User(
            email = validated_date['email'],
            username = validated_date['username']
         )
         user.set_password(validated_date['password'])
         user.save()
         Token.objects.create(user=user)
         return user 
     

       
