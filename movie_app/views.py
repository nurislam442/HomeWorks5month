from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(http_method_names=['GET', 'POST'])
def director_list_api_view(request):
    if request.method == "GET":
        directors = Director.objects.all()
        list_ = Director_serializer(instance=directors, many=True).data
        return Response(data=list_)
    elif request.method == "POST":
        validator = DirectorValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})
        name = validator.validated_data.get('name')
        director = Director.objects.create(name=name)
        return Response(status=status.HTTP_201_CREATED, data=Director_item_serializer(director).data)
    
@api_view(http_method_names=["GET","PUT", "DELETE"])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "director not found"})
    if request.method == "GET":
        data = Director_serializer(instance=director).data
        return Response(data=data)
    elif request.method == "PUT":
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = request.data.get("name")
        director.save()
        return Response(data=Director_item_serializer(director).data, 
                        status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', "POST"])
def movie_list_api_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        list_ = Movie_serializer(instance=movies, many=True).data
        return Response(data=list_)
    elif request.method == "POST":
        validator = MoviesValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})
        title = request.data.get("title")
        description = request.data.get("description")
        duration = request.data.get("duration")
        director_id = request.data.get("director_id")
        movie = Movie.objects.create(title=title,
        description=description, duration=duration, director_id=director_id)
        return Response(status=status.HTTP_201_CREATED, data=Movie_item_serializer(movie).data)

@api_view(http_method_names=["GET", "PUT", "DElETE"])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "movie not found"})
    if request.method == "GET":
        data = Movie_serializer(instance=movie).data
        return Response(data=data)
    elif request.method == "PUT":
        serializer = MoviesValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get("description")
        movie.duration = serializer.validated_data.get("duration")
        movie.director_id = serializer.validated_data.get("director_id")
        movie.save()
        return Response(data=Movie_item_serializer(movie).data, 
                        status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', "POST"])
def review_list_api_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        list_ = Review_serializer(instance=reviews, many=True).data
        return Response(data=list_)
    elif request.method == "POST":
        validator = ReviewsValidateSerilizer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})
        text = validator.validated_data.get("text")
        movie_id = validator.validated_data.get("movie_id")
        stars = validator.validated_data.get("stars")
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=Review_item_serializer(review).data)

@api_view(http_method_names=["GET","PUT", "DELETE"])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "review not found"})
    if request.method == "GET":
        data = Review_serializer(instance=review).data
        return Response(data=data)
    elif request.method == "PUT":
        serializer = ReviewsValidateSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = serializer.validated_data.get("text")
        review.stars = serializer.validated_data.get("stars")
        review.movie_id = serializer.validated_data.get("movie_id")
        review.save()
        return Response(data=Review_item_serializer(review).data, 
                        status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(http_method_names=["GET",])
def review_movie_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        list_ = Review_Movie_serializer(instance=movies, many=True).data
        return Response(data=list_)

