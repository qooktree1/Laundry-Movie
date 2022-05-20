from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index),
    path('detail/<int:movie_pk>', views.movie_detail),
]