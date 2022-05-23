from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='reviews'),
    path('create/<int:movie_pk>', views.create_review, name='create_review'),
    path('<int:review_pk>', views.detail_review, name='detail_review'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),


    path('<int:review_pk>/review/delete/', views.delete_review, name='delete_review'),
    path('<int:comment_pk>/comment/delete/', views.delete_comment, name='delete_comment'),
]
