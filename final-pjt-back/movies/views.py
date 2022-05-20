from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from .models import Movie
from .serializers import MovieSerializer



@api_view(['GET'])
def index(request):    
    highscore_movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')
    hightscore_serializer = MovieSerializer(data=highscore_movies, many=True)
    hightscore_serializer.is_valid()  # 왜 이렇게 사용할까??
    context = {
        'hightscore_serializer': hightscore_serializer.data,
    }
    return Response(context)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    print(movie)
    # 여기서 빨래 색깔 관련 serialized data, 빨래 시간 관련 data 를 context에 삽입??!

    context = {

    }
    return Response(context)