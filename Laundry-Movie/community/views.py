from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment
from movies.models import Movie
from .serializers import ReviewSerializer, CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/review_page.html', context)

@api_view(['POST'])
def create_review(request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
model이랑 serializer 부터 다시 해봐야할듯
drf로 정보 보내서 게시글 작성될 수 있도록 하기
영화 리뷰인데 어떠한 영화인지 확인할 수 있게 str 표현해두기
아...모르겠다 진짜 머리가 꼬이는중입니다...
'''