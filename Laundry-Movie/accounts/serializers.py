from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review, Comment
from .models import User

User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):

#     # serializing시 응답에 password 포함시키지 않음 -> 보안상 유출 방지
#     password = serializers.CharField(write_only=True)

#     class Meta : 
#         model = User
#         fields = ('username', 'password', 'email')


# class UserDetailSerializer(serializers.ModelSerializer):

#     class Meta : 
#         model = User
#         fields = ('username', 'email', 'id')


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ('nickname', 'email', 'name', 'password')


class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk', 'title', 'movie_review')
    # 프로필에서 영화 리뷰 어떤걸 썼는지 확인하기 위해 가져오는 것, pk, 리뷰제목, 리뷰한 영화 내용(역참조) 
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = User
        fields = ('pk', 'username')
