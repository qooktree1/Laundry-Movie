from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment
from movies.models import Movie
from .serializers import ReviewSerializer, CommentSerializer, ReviewListSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 장고 페이지네이션
from django.core.paginator import Paginator

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    paginator = Paginator(reviews, '10') # Paginator(분할할 객체, 페이지 당 담길 객체 수)
    page_object = paginator.page(page)  # 페이지 번호 받아서 해당 페이지 리턴
    context = {
        'reviews': reviews,
        'pages' : page_object,
    }
    return render(request, 'community/review_page.html', context)

@api_view(['POST'])
def create_review(request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
'''
detail에서 review delete 요청이 오면 삭제되도록 함
@api_view(['delete'])
def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user.pk == review.user.pk:
        review.delete()
        data = {
            'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
'''
'''
model이랑 serializer 부터 다시 해봐야할듯
drf로 정보 보내서 게시글 작성될 수 있도록 하기
영화 리뷰인데 어떠한 영화인지 확인할 수 있게 str 표현해두기
아...모르겠다 진짜 머리가 꼬이는중입니다...
'''

@api_view(['GET', 'DELETE', 'PUT'])
def detail_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


