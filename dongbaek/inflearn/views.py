from django.shortcuts import render
from .models import Post
# Create your views here.


def Post_list(request):
    # qs는 QureySet이라는 뜻
    qs = Post.objects.all()
    return render(request, 'inflearn/post_list.html', {
        'Post_list' : qs,
    })