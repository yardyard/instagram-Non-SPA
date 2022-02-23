from urllib import request
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .forms import PostForm, CommentForm
from .models import Tag, Post

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404


from datetime import timedelta
from django.utils import timezone

@login_required
def index(request):
    # 현재를 기준으로 3일 이내라면
    timesince = timezone.now() - timedelta(days=3)

    # TimeLine에 Follow하는 유저들의 포스팅 만을 노출하기
    post_list = Post.objects.all()\
        .filter( 
            Q(author=request.user) | 
            Q(author__in=request.user.following_set.all())
            )\
        .filter(
            #created_at__lte = timesince # 3일 이내의 게시글
            created_at__gte = timesince # 3일 이외의 게시글
        ) 
         
         

    #    Q는 or을 의미한다.
    #    .filter(
    #    # 작성자가 본인 또는
    #        Q(author=request.user)) |
    #
    #        # 유저의 following_set에 들어있는 유저만 보이도록
    #        Q(author__in=request.user.following_set.all()) 
    #    )
    #    


    #like_user_set = Post.like_user_set

    suggested_user_list = get_user_model().objects.all()\
        .exclude(pk=request.user.pk)\
        .exclude(pk__in=request.user.following_set.all())[:3] # 이미 팔로잉 하고 있는 유저들을 제외함.
        
    # 유저 본인 pk를 제외하고 나머지 유저가 suggested_user이다.
    return render(request, "insta/index.html", {
        #"like_user_set" : like_user_set,
        "post_list" : post_list,
        "suggested_user_list" : suggested_user_list,       
    })
    



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
    # 해당 글 작성자 객체 저장 
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    
    # 해당 유저가 쓴 글만을 filter 처리하여서 저장
    post_list = Post.objects.filter(author=page_user)
    post_list_cnt = post_list.count() # 실제 DB에 count 쿼리를 던짐
    
        # 로그인이 되어있으면 User 객체, or Not AnonymousUser  
    if request.user.is_authenticated:
        # 로그인이 되어있으면, Following_set의 작성자 pk가 존재하면 유저 객체를 가져온다.
        is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
    else:
        is_follow = False

    return render(request, "insta/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_cnt": post_list_cnt,
        "is_follow": is_follow,
    })


# 포스팅 좋아요
@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # like_user_set에 글 작성자(=request.user)를 추가해준다.
    post.like_user_set.add(request.user)

    messages.success(request, f"포스팅 {post.pk}를 좋아합니다.")
    
    redirect_url = request.META.get("HTTP_REFERER", "root") # HTTP_REFERER은 request 요청을 한 웹페이지의 주소를 보여준다.
    # 만약 HTTP_REFERER가 없으면 root 주소를 가져온다.
    return redirect(redirect_url)


# 포스팅 싫어요
@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # like_user_set에 글 작성자(=request.user)를 제거해준다.
    post.like_user_set.remove(request.user)

    messages.success(request, f"포스팅 {post}의 좋아요를 취소합니다.")
    
    redirect_url = request.META.get("HTTP_REFERER", "root") # HTTP_REFERER은 request 요청을 한 웹페이지의 주소를 보여준다.
    # 만약 HTTP_REFERER가 없으면 root 주소를 가져온다.
    return redirect(redirect_url)


# 댓글 쓰기
@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # 내부적으로 comment가 save되는 것을 막음 
            # 그 이유는 댓글 폼은 message 필드만 받기 때문에, 나머지 필드에서 오류가 생기기 때문이다.
            # 그러기에 나머지 필드를 채워준 상태에서 form을 저장 시켜야한다.
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.post)    
    else:
        form = CommentForm()
    return render(request, "insta/comment_form.html", {
        "form" : form,
    })   