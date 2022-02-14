from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
from django.core.validators import RegexValidator
from django.shortcuts import resolve_url

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
    
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(blank=True, max_length=13, validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(blank=True, max_length=6, choices=GenderChoices.choices, default=GenderChoices.MALE
    , help_text="48px * 48px 크기의 png / jpg 파일을 업로드해주세요"
    )
    
    # upload_to="%Y/%m/%d" 는 업로드 되는 날짜에 따른 폴더가 생성이 된다.
    profile = models.ImageField(blank=True, upload_to="accounts/proflie/%Y/%m/%d")


    # name에 접근된 값에 이름 형태에 맞는 데이터 형태로 반환
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


    # profile이 있는지 검사하고 알맞은 값을 반환하는 로직
    @property
    def profile_url(self):
        if self.profile:
            return self.profile.url
        else:
            return resolve_url('pydenticon_image', self.username)


    def send_welcome_email(self):        
        Subject = render_to_string("accounts/welcome_email_subjects.txt", {
            "user": self,
        })
        content = render_to_string("accounts/welcome_email_contents.txt", {
            "user": self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail( Subject, content , sender_email , [self.email], fail_silently=False)


#class Profile(models.Model):
   # pass
