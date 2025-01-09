from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(http_method_names=['GET',])
def director_list_api_view(request):
    if request.method == "GET":
        directors = Director.objects.all()
        list_ = Director_serializer(instance=directors, many=True).data
        return Response(data=list_)
    
@api_view(http_method_names=["GET",])
def director_detail_view(request, id):
    director = Director.objects.get(id=id)
    data = Director_serializer(instance=director).data
    return Response(data=data)


@api_view(http_method_names=['GET',])
def movie_list_api_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        list_ = Movie_serializer(instance=movies, many=True).data
        return Response(data=list_)

@api_view(http_method_names=["GET",])
def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    data = Movie_serializer(instance=movie).data
    return Response(data=data)

@api_view(http_method_names=['GET',])
def review_list_api_view(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        list_ = Review_serializer(instance=reviews, many=True).data
        return Response(data=list_)

@api_view(http_method_names=["GET",])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    data = Review_serializer(instance=review).data
    return Response(data=data)
    
@api_view(http_method_names=["GET",])
def review_movie_view(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        list_ = Review_Movie_serializer(instance=movies, many=True).data
        return Response(data=list_)

