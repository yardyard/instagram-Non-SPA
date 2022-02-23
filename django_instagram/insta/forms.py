from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =  [
            'photo', 'caption', 'location'
        ]

        # 장고에서는 widgets 를 통해 특정 필드 위젯을 변경할 수 있다.
        widgets = {
            "caption" : forms.Textarea,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
