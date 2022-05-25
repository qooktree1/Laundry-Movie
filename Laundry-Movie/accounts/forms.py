from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Profile, User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

class LoginForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)


# 
class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)
   	# 위의 내용을 정의하지 않아도 상관없지만, 화면에 출력될 때 label이 영문으로 출력되는 것이 싫어서 수정한 것이다..
    class Meta:
        model = Profile
        exclude = ('user',)