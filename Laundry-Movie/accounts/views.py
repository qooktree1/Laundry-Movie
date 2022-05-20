from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer


@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    profile_serializer = ProfileSerializer(user)
    return Response(profile_serializer.data)


'''
프로필 내용 확인할 때 headers => Token 토큰값 보내기
'''