from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='reviews'),
    # create/ 시에 어떠한 영화의 리뷰를 작성할 것인지 ... >> 이걸 movies에 연결해야할듯..?
    path('review/create/', views.create_review, name='create_review'),
    # path('<int:review_pk>/delete', views.delete_review, name='delete_review'),
    path('review/<int:review_pk>/', views.detail_review, name="detail_review"),

]   