# 클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView 클래스를 임포트합니다.
from django.views.generic import ListView, DetailView

# 테이블 조회를 위해 모델 클래스를 임포트합니다.
from bookmark.models import Bookmark

# BookmarkLV는 Bookmark 테이블의 레코드 리스트를 보여주기 위한 뷰로서, ListView 제네릭 뷰를 상속
# 받습니다. ListView를 상속 받는 경우는 객체가 들어있는 리스트를 구성해서 이를 컨텍스트 변수로
# 템플릿 시스템에 넘겨주면 됩니다. 
class BookmarkLV(ListView):

    model = Bookmark

# BookmarkDV는 Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰로서, DetailView
# 제네릭 뷰를 상속 받습니다. DetailView를 상속받는 경우는 특정 객체 하나를 컨텍스트 변수에 담아서
# 템플릿 시스템에 넘겨주면 됩니다. 만일 테이블에서 Primary Key로 조회해서 특정 객체를 가져오는 경우에는
# 테이블명, 즉 모델 클래스 명만 지정해주면 됩니다. 조회시 사용할 Primary Key값은 URLconf에서 추출해 
# 뷰로 넘어온 인자를 (ex:pk=99)를 사용합니다.
class BookmarkDV(DetailView):

    model = Bookmark


# Create your views here.

