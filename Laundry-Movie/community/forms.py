from django import forms
from .models import Review, Comment


# 평점의 선택지
REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


# class starWidget(forms.TextInput):
#     input_type = 'rating'
#     template_name = 'community/star_rate.html'

#     class Media:
#         css = {
#             'all': [
#                 'widgets/rateit/rateit.css',
#             ],
#         }
#         js = [
#              "//code.jquery.com/jquery-3.4.1.min.js",
#             'widgets/rateit/jquery.rateit.min.js',
#         ]
#     def buildattrs(self, *args, **kwargs):
#         attrs = super().build_attrs(*args, **kwargs)
#         attrs.update({
#             'min': 0,
#             'max': 5,
#             'step': 1,
#         })




class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'rank', 'content']
        widgets = {
            'rank': forms.Select(choices=REVIEW_POINT_CHOICES),  # 선택지를 인자로 전달
            # 'rank': starWidget,
            'title': forms.TextInput(attrs={'class': 'my-title form-control', 'placeholder': '영화를 한 줄로 표현한다면?'}),
            'content': forms.Textarea(attrs={'class': 'my-content form-control','placeholder': '자세한 후기를 작성해주세요'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']