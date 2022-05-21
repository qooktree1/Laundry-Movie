from django.http import JsonResponse
from django.views.decorators.http import require_safe
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_list_or_404, render
from .models import Movie, Genre
from .serializers import GenreSerializer, MovieDetailSerializer, MovieSerializer




@require_safe
def index(request):
    return render(request, 'movies/index.html')


@require_safe
def home(request):
    highscore_movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')[:12]
    highscore_serializer = MovieSerializer(data=highscore_movies, many=True)
    highscore_serializer.is_valid()

    context = {
        'highscore_serializer': highscore_serializer.data,
    }
    return render(request, 'movies/home.html', context)


def selected(request):
    highscore_movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')
    highscore_serializer = MovieSerializer(data=highscore_movies, many=True)
    # 유효성 검사
    highscore_serializer.is_valid()
    context = {
        'highscore_serializer': highscore_serializer.data,
    }
    return render(request, 'movies/selected.html', context)


def tips(request):
    return render(request, 'movies/tips.html')


# Home 로그인 상황 - 빨래 시간 순삭! - 영화 구분하는 알고리즘!
@api_view(['POST'])
@require_POST
def movie_list(request):
    highscore_movies = Movie.objects.order_by('-vote_average').prefetch_related('genres')  # 평점 높은 순

    # 빨래 색깔 serialize
    # 흰색(white) - 다큐멘터리(99), 음악(10402), 로맨스(10749), 가족(10751), 코미디(35), 드라마(18)
    # 검은색(black) - 공포(27), 범죄(80), 미스터리(9648), 전쟁(10752), 스릴러(53), 역사(36), 서부(37), 액션(28)
    # 나머지색(other) - TV 영화(10770), 모험(12), 판타지(14), 애니메이션(16), SF(878)

    # 세탁모드(runtime 별)
    # 쾌속 50분 ~ 1시간 40분 (50~100)  short
    # 표준 1시간 30분~ 2시간 (90~ 120)  normal
    # 이불세탁 2시간 ~ 3시간이상 (120~180)  long

    white_color_movie = {99: True, 10402: True, 10749: True, 10751: True, 35: True, 18: True}
    black_color_movie = {27: True, 80: True, 9648: True, 10752: True, 53: True, 36: True, 37: True, 38: True}
    other_color_movie = {10770: True, 12: True, 14: True, 16: True, 878: True}
    white = set()
    black = set()
    other = set()
    
    short = set()
    normal = set()
    long = set()
    
    for movie in highscore_movies:
        if movie.runtime <= 100:
            short.add(movie)
        if 90 <= movie.runtime <= 120:
            normal.add(movie)
        if 120 <= movie.runtime <= 180:
            long.add(movie)

        for each_genre in movie.genres.all():
            if white_color_movie.get(each_genre.id, 0):
                white.add(movie)
            if black_color_movie.get(each_genre.id, 0):
                black.add(movie)
            if other_color_movie.get(each_genre.id, 0):
                other.add(movie)
    
    highscore_serializer = MovieSerializer(data=highscore_movies, many=True)
    white_movie_serializer = MovieSerializer(data=white, many=True)
    black_movie_serializer = MovieSerializer(data=black, many=True)
    other_movie_serializer = MovieSerializer(data=other, many=True)
    short_movie_serializer = MovieSerializer(data=short, many=True)
    normal_movie_serializer = MovieSerializer(data=normal, many=True)
    long_movie_serializer = MovieSerializer(data=long, many=True)


    # 유효성 검사
    highscore_serializer.is_valid()
    white_movie_serializer.is_valid()
    black_movie_serializer.is_valid()
    other_movie_serializer.is_valid()
    short_movie_serializer.is_valid()
    normal_movie_serializer.is_valid()
    long_movie_serializer.is_valid()

    context = {
        'short_movie_serializer': short_movie_serializer.data,
        'normal_movie_serializer': normal_movie_serializer.data,
        'long_movie_serializer': long_movie_serializer.data,
        'white_movie_serializer': white_movie_serializer.data,
        'black_movie_serializer': black_movie_serializer.data,
        'other_movie_serializer': other_movie_serializer.data,
        'highscore_serializer': highscore_serializer.data,
    }
    return JsonResponse(context)
    

# 영화 상세 페이지
# 선택한 영화의 정보들을 출력
# 선택한 영화의 정보와 비슷한 영화 즉, 선택한 영화의장르를 가진 영화들?
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie_list = [movie]  # iterable 하게 만들기
    movie_serializer = MovieDetailSerializer(data=movie_list, many=True)
    # 영화의 장르 목록 (genres)에서 찾고자하는 장르를 갖고있는 모든 영화들을 출력하기
    
    genres = movie.genres.all().values_list('id', flat=True) # 영화의 모든 genre를 id 객체로 가져오기 (flat=true) : 튜플 아닌 리스트 형식으로 가져오는것
    movies_same_genre = Movie.objects.filter(genres__id__in=genres).prefetch_related('genres').distinct()[:5]
    same_genre_serializer = MovieSerializer(data = movies_same_genre, many=True)
    
    # 유효성 검사
    movie_serializer.is_valid()
    same_genre_serializer.is_valid()
    
    context = {
        'movie': movie_serializer.data,
        'same_genres': same_genre_serializer.data,
    }
    return render(request, 'movies/movie_detail.html', context)
    return Response(context)