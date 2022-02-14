import re
from django.db import models
from django.urls import reverse

# User 외래키로 삼는 법
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="insta/post/%Y%m%d")
    # 내용
    caption = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)
    location = models.CharField(max_length=100) 

    # Post 객체가 생성되면 아래 __str__함수가 호출된다.
    def __str__(self):
        return self.caption


    # 태그 기능
    def extract_tag_list(self):
        # "#"이 붙고 뒤에 문자가 오면 태그로 분류 저장한다.
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.caption)
        
        # tag가 저장될 list
        tag_list = []
        
        # caption(본문)에서 #이 들어간 문자열을 TAG의 name에 저장해준다.
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    # detail view
    def get_absolute_url(self):
        return reverse("insta:post_detail", args=[self.pk])
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name