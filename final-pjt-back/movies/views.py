from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from .models import Movie
from .serializers import MovieSerializer



@api_view(['GET'])
def index(request):    
    movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')
    serializer = MovieSerializer(data=movies, many=True)
    if serializer.is_valid():
        return Response(serializer.data)