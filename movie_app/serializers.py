from rest_framework import serializers
from .models import *

class Director_serializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'name movies_count'.split()
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
    movie = Movie_serializer()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = 'text stars movie rating rating'.split()
    def get_rating(self, stars):
        stars = Review.objects.values_list('stars', flat=True)
        return sum(stars)/len(stars)
