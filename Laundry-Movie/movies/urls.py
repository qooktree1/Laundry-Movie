from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('tips/', views.tips, name='tips'),
    path('selected/', views.selected, name='selected'),
    
    path('allmovie/', views.movie_list, name='movie_list'),
    path('detail/<int:movie_pk>', views.movie_detail, name='movie_detail'),
    
]   