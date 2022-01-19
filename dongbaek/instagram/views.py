
from urllib import request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.base import Model
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ArchiveIndexView, DetailView
from django.views.generic.dates import YearArchiveView
from django.views.generic.list import ListView

from .forms import PostForm
from .models import Post

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # 현재 로그인한 유저 Instance
            post.save()
            # post의 detail.html로 이동함.
            return redirect(post)
    else:         
        form = PostForm()
        
    return render(request, 'instagram/post_form.html',{
        'form' : form,
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 이렇게 반복되는 코드가 있다면 장식자로 만드는 것도 좋은 방법
    # 작성자만 수정할 수 있도록 
    if post.author != request.user:
        messages.error(request, '작성자만 수정 가능합니다!')
        return redirect(post)


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # post의 detail.html로 이동함.
            return redirect(post)
    else:         
        form = PostForm(instance=post)
        
    return render(request, 'instagram/post_form.html',{
        'form' : form,
    })




@login_required
def post_list(request):
    # QuerySet을 의미함.
    qs = Post.objects.all()
    
    # 전달 받은 인자 중에서 'q'라는 이름의 인자를 가져오겠다는 의미
    # 두번째 매개변수는 만약 'q'라는 인자가 없을시 반환할 값을 의미
    # https://velog.io/@sdk1926/request.GET.getq
    q = request.GET.get('q', '')
    
    # 'q'라는 인자가 있었을 경우
    if q:
        #  filter를 통해서 message 필드 중 q인 필드들만 qs에 저장함.
        qs = qs.filter(message__icontains=q)
    
    # render를 통해서 HTML 응답을 쉽게 만들 수 있다.
    # render의 첫번째 인자는 view 함수의 인자를 넘겨받는다.
    # 두번째 인자는 app이름을 써주고 뒤에 원하는 템플릿(HTML) 이름을 써준다.
    # 세번쨰 인자로 템플릿 내에서 참조할 것과 참조할 이름을 적어준다.
    
    # 위치는 instagram(app)/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q' : q,
    })


# post_list = ListView.as_view(model=Post, paginate_by= 10)
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()


post_detail = DetailView.as_view(
    model = Post,
    queryset = Post.objects.all()
)


post_archive = ArchiveIndexView.as_view(model= Post , date_field='created_at')

post_archive_year = YearArchiveView.as_view(model= Post, date_field='created_at', make_object_list=True)

