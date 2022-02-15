from dataclasses import field
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm

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
    
    # username 중복 방지 함수
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username:
            qs = User.objects.filter(username='post')
            if qs.exists():
                raise forms.ValidationError("지정할 수 없는 아이디입니다.")
            
            return username

    
    # email 중복 방지 함수
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
            
            return email

            
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'profile', 'first_name', 'last_name', 'phone_number', 'gender'
        ]


class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        # 기존 암호
        old_password = self.cleaned_data.get('old_password')
        
        # 새로운 암호
        new_password1 = self.cleaned_data.get('new_password1')
        
        # 만약 기존 암호와 새로운 암호가 같다면
        if old_password and new_password1:    
            if old_password == new_password1:
                raise forms.ValidationError("변경할 암호가 기존 암호와 달라야 합니다")
        
        return new_password1

