from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from pandas.io.pytables import format_doc
from .models import Post
from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import DetailView


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



"""
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk) # 앞 pk는 필드 종류, 뒷 pk는 실제 pk 값을 의미
    return render(request, 'instagram/post_detail.html', {
        'post' : post,
    })
"""

post_detail = DetailView.as_view(
    model = Post,
    queryset = Post.objects.all()
)

post_list = ListView.as_view(model=Post, paginate_by= 10)

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
    