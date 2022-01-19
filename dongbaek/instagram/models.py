from http import server
from django.conf import settings
from django.contrib.admin.decorators import register
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse

from django.core.validators import MinLengthValidator

# validators 객체는 함수를 반환하여준다.
# 만약 3글자 미만의 문자열을 입력받으면 forms.ValidationError를 반환한다.
min_length_Validators = MinLengthValidator(3)




# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    message = models.TextField(
        validators=[min_length_Validators]
    )
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


