from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model


User = get_user_model()
# 리뷰 리스트 시리얼라이즈 해버리기 (전체 필드 다 출력해야 함 글 작성 수정 시간 유저 번호 제목 등 )
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        # 내용은 리스트에서 안뽑아도 될듯?
        exclude = ('content')

class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'comments', 'content')



class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'title', 'content', 'rank')
