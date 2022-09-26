from .models import Stock,User
from rest_framework.authtoken.admin import *

from rest_framework import serializers
from rest_framework.authtoken.admin import *



class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'
