from audioop import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import User, Profile

from .forms import CustomUserCreationForm, LoginForm, ProfileForm
from rest_framework.decorators import api_view

from .serializers import ProfileSerializer

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe

from community.models import Review, Comment


@require_safe
def people(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/people.html', context)


'''
프로필 내용 확인할 때 headers => Token 토큰값 보내기
'''

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
            return redirect('movies:home')

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:home')
    return redirect('movies:index')


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:home')
    return redirect('movies:index')


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


# @api_view(['GET', 'POST'])
@login_required
@require_http_methods(['GET', 'POST'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:people', user.username)
        return redirect('accounts:profile')
    else:
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'accounts/profile.html',context)