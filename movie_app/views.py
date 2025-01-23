from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = Director_serializer
    def create(self, request):
        validator = DirectorValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'errors': validator.errors})
        
        name = validator.validated_data.get('name')
        director = Director.objects.create(name=name)
        return Response(status=status.HTTP_201_CREATED
            ,data=Director_item_serializer(director).data)
    
class Director_detail_view(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = Director_serializer
    lookup_field = "id"


class Movie_list_api_view(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_serializer
    def create(self, request):
        validator = MoviesValidateSerializer(data=request.data)
        if not validator.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'errors': validator.errors})
        
        title = validator.validated_data.get('title')
        description = validator.validated_data.get("description")
        duration = validator.validated_data.get("duration")
        director_id = validator.validated_data.get("director_id")
        director = Movie.objects.create(title=title,description=description,
                                           duration=duration, director_id=director_id)

        return Response(status=status.HTTP_201_CREATED
            ,data=Movie_item_serializer(director).data)


class Movie_detail_view(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = Movie_serializer
    lookup_field = "id"
    
class Review_list_api_view(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = Review_serializer
    def create(self, request):
        validator = ReviewsValidateSerilizer(data=request.data)
        if not validator.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'errors': validator.errors})
        
        text = validator.validated_data.get("text")
        movie_id = validator.validated_data.get("movie_id")
        stars = validator.validated_data.get("stars")
        director = Review.objects.create(text = text, movie_id=movie_id, stars=stars)

        return Response(status=status.HTTP_201_CREATED
            ,data=Review_item_serializer(director).data)
    
class Review_detail_view(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = Review_serializer
    lookup_field = "id"
   
    
class Review_movie_view(ListAPIView):
    iqueryset = Review.objects.all()
    serializer_class = Review_Movie_serializer

