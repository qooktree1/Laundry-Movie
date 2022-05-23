from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Review, Comment
from movies.models import Movie
from .forms import ReviewForm, CommentForm
from rest_framework.decorators import api_view

from django.views.decorators.http import require_GET,require_POST, require_http_methods

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

# @api_view(['POST'])
# def create_review(request):
#     serializer = ReviewSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return render(request, 'community/review_create.html')

@require_http_methods(['GET', 'POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.filter(pk=movie_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie[0] # 추가됨
            review.save()
            return redirect('community:reviews')
    else:
        form = ReviewForm()
    context = {
        'form': form,
        'movie': movie[0],
    }
    return render(request, 'community/review_create.html', context)


@require_GET
def detail_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    movie = Movie.objects.filter(pk=review.movie_id)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
        'movie': movie[0],
    }
    return render(request, 'community/review_detail.html', context)

@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail_review', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail_review.html', context)


# 리뷰 삭제
@require_POST
def delete_review(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        review.delete()
        return redirect('community:reviews')
    return render(request, 'community/detail_review.html', review.pk)


# 댓글 삭제
@require_POST
def delete_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    review = Review.objects.get(pk = comment.review.pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('community:detail_review', review.pk)
    return render(request, 'coummunity/detail_review.html', review.pk)