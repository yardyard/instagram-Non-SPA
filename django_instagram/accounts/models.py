from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.template.loader import render_to_string
# Create your models here.

class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    
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
