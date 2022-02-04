from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    # 회원가입시 새로운 필드들을 커스텀 하고 싶을 때 생성자 호출
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) # 부모를 호출함.
        # form에 적용시키고 싶은 필드들을 오버라이딩을 통해 True로 지정
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True     

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name'
        ]
    
    # email 중복 방지 함수
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
            
            return email

            