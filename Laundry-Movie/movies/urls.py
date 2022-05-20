from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('detail/<int:movie_pk>', views.movie_detail),
]   