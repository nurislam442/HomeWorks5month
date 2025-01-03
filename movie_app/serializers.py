from rest_framework import serializers
from .models import *

class Director_serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class Movie_serializer(serializers.ModelSerializer):
    director = Director_serializer()
    class Meta:
        model = Movie
        fields = '__all__'

class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'