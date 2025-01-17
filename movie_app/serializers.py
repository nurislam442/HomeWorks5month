from rest_framework import serializers
from .models import *
from datetime import timedelta
from rest_framework.exceptions import ValidationError

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

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)

class MoviesValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    duration = serializers.CharField(max_length=255)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            director = director.objects.get(id=director_id)
        except:
            raise ValidationError('director does not exist!')
        return director_id

class ReviewsValidateSerilizer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.CharField()
    GRADES = (
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *')
    )
    stars = serializers.ChoiceField(choices=GRADES, default=1)

    def validate_movie(self, value):
        if value is None:
            raise serializers.ValidationError("Movie cannot be null.")
        return value