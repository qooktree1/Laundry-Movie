from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from .models import Movie
from .serializers import MovieSerializer



@api_view(['GET'])
def index(request):    
    highscore_movies = Movie.objects.order_by('-vote_average')
    hightscore_serializer = MovieSerializer(data=highscore_movies, many=True)
    hightscore_serializer.is_valid()  # 왜 이렇게 사용할까??
    context = {
        'hightscore_serializer': hightscore_serializer.data,
    }
    return Response(context)


@api_view(['GET'])
def movie_detail(request):
    pass