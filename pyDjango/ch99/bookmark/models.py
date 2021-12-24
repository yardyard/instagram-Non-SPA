from django.db import models 

# 장고에서는 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수로 매핑합니다.
# 각 클래스의 변수와 타입도 장고에서 미리 정의해 둔 필드 클래스를 사용합니다.
# models.py에서는 테이블을 정의합니다

class Bookmark(models.Model):

    #title 컬럼은 공백을 가질 수 있습니다.
    title = models.CharField('TITLE', max_length=100, blank=True)
    #URL필드 클래스의 첫 번쨰 파라미터인 'URL'문구는 url 컬럼에 대한 별칭이며, admin 사이트에서 보여지는 부분입니다.
    url = models.URLField('URL', unique=True)

    # __set__() 함수를 정의하지 않으면 레코드명이 제대로 표현되지 않습니다.
    def __str__(self):
        return self.title

