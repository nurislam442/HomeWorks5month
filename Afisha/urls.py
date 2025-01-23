from django.contrib import admin
from django.urls import path
from movie_app import views
from users.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListCreateAPIView.as_view()),
    path("api/v1/directors/<int:id>/", views.Director_detail_view.as_view()),
    path('api/v1/movies/', views.Movie_list_api_view.as_view()),
    path("api/v1/movies/<int:id>/", views.Movie_detail_view.as_view()),
    path('api/v1/reviews/', views.Review_list_api_view.as_view()),
    path("api/v1/reviews/<int:id>/", views.Review_detail_view.as_view()),
    path("api/v1/directors/<int:id>/", views.Review_detail_view.as_view()),
    path("api/v1/movies/reviews/", views.Review_movie_view.as_view()),
    path('api/v1/users/registration/', register_api_view),
    path('api/v1/users/authorization/', auth_api_view),
    path("api/v1/users/confirm/", confirm_api_view),
]
