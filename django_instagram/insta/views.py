from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import PostForm
from .models import Tag, Post

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404


# 포스팅 쓰기
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # 현재 로그인 유저를 작성자에 저장
            post.author = request.user
            # manytomany는 실제 pk 값이 있어야하기에 form이 저장된 상태로 해야한다.
            post.save()
            # post의 tag_list를 호출하여 Post 모델의 tag_set에 저장한다.
            post.tag_set.add(*post.extract_tag_list())

            messages.success(request, "포스팅을 저장했습니다.")
           
            # 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출
            # -> get_absolute_url() 함수에서 지정한 위치로 이동하게 된다.
            return redirect(post) 
    
    else:
        form = PostForm()

    return  render(request, "insta/post_form.html", {
        "form" : form,
    })

# 포스팅 detail
def post_detail(request, pk):
    # 해당 pk의 포스팅 객체가 없을 경우 404 에러 반환
    post = get_object_or_404(Post, pk=pk)
    return render(request, "insta/post_detail.html", {
        "post" : post,
    })


# 유저 페이지
def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    # 해당 유저가 쓴 글만을 filter 처리하여서 저장
    post_list = Post.objects.filter(author=page_user)
    return render(request, "insta/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
    })