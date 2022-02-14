from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Tag

from django.http import HttpResponseRedirect
from django.shortcuts import redirect


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
            return redirect("/")  # TODO: get_absolute_url 모델단에 구현하기
    
    else:
        form = PostForm()

    return  render(request, "insta/post_form.html", {
        "form" : form,
    })