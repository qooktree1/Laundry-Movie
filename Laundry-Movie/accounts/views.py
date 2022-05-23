from audioop import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import User
from rest_framework import status
from .forms import CustomUserCreationForm, LoginForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

from community.models import Review, Comment

#def index(request):
#    return render(request, 'movies/home.html')


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    profile_serializer = ProfileSerializer(user)
    
    return Response(profile_serializer.data)


'''
프로필 내용 확인할 때 headers => Token 토큰값 보내기
'''

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
            return redirect('movies:home')

    if request.method == 'POST':

        # user_info = User.objects.all()
        # if request.POST['password1'] != request.POST['password2']:
        #     return redirect('movies:index')

        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:home')
    return render(request,'movies/index.html')


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:home')
    return render(request, 'movies/index.html', locals())


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


@login_required
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

