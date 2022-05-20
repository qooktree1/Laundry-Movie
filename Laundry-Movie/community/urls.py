from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name='reviews'),
    path('create/', views.create_review, name='create_review'),
    # path('')
]   