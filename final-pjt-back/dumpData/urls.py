from django.urls import path
from . import views

app_name = 'dumpData'

urlpatterns = [
    path('genre_data', views.genre_data),
    path('movie_data', views.movie_data),
]