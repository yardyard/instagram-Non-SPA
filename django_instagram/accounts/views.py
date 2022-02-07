from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.contrib.auth import login as auth_login


login = LoginView.as_view(template_name= "accounts/login_form.html")

def logout(request):
    messages.success(request, '로그아웃 되었습니다!')
    return logout_then_login(request)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            next_url = request.GET.get('next', '/') # next 인자를 가져오고, 없으면 / 주소로 이동
            signed_user = form.save()
            auth_login(request, signed_user)
            signed_user.send_welcome_email() # 추후 비동기 Celery로 처리하기.
            messages.success(request, "회원가입이 되었습니다~!")
            return redirect(next_url)
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })

