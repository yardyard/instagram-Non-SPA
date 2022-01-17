from django.conf import settings
from django.contrib.admin.decorators import register
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    # Tag를 문자열로 적은 이유는, Tag Class가 맨 아래 있기 때문에 참조하는데 있어서 오류가 생기기 때문이다.
    # blank는 Tag가 없는 상황을 허용할건지 (True)를 물어보는 인자 옵션이다. 
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    # Java의 toString과 같은 역할
    def __str__(self):
        return self.message
    
    # id의 역순으로 정렬함.
    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True}) # post_id 필드가 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True) # 태그는 해당 태그 테이블 내에서 유일해야 하기에 unique 사용
    #post_set = models.ManyToManyField(Post) # reverse 방법
    
    def __str__(self):
        return self.name



    """
    def message_length(self): # 매개변수를 주면 안됌
        return len(self.message)
    message_length.short_description = "메세지 글자 수"
    """

    """
    uuid를 통해 파일명 정하기
    def uuid_name_upload_to(instance, filename):
        app_label = instance.__class__._meta.app_label # 앱 별로
        cls_name = instance.__class__.__name__.lower() # 모델 별로
        ymd_path = timezone.now().strftime('%Y/%m/%d') # 업로드하는 년 / 월 / 일 별로
        uuid_name = uuid4().hex
        extenstion = os.path.splittext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환
        return '/'.join([
            app_label,
            cls_name,
            ymd_path,
            uuid_name[:2],
            uuid_name + extenstion,
        ])
    """

