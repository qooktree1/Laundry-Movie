from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields


class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)