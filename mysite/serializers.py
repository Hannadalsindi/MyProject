
from sre_constants import CATEGORY_DIGIT
from urllib import response
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GeeksModel , pro


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class GeeksSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = GeeksModel
        fields = ('title', 'description')





class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=pro
        fields=('id',' Category_id',' product_name','image','Sku','price')
        


    

    

        
