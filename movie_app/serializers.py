from rest_framework import serializers
from .models import *
from datetime import timedelta

class Director_serializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'name movies_count id'.split()
    def get_movies_count(self, director):
        return Movie.objects.filter(director=director).count()


class Movie_serializer(serializers.ModelSerializer):
    director = Director_serializer()
    class Meta:
        model = Movie
        fields = '__all__'

class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class Review_Movie_serializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = Review_serializer(many=True)
    class Meta:
        model = Movie
        fields = 'title description duration director reviews rating'.split()
    def get_rating(self, stars):
        return stars.rating()

class Director_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
    
class Movie_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "title description duration director".split()

class Review_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"