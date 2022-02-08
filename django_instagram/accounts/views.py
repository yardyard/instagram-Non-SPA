import imp
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView as AuthPasswordChangeView
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


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


@login_required
def profile_edit(request):
    if request.method == 'POST': 
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필이 수정 되었습니다!")
            return redirect("profile_edit")
    
    else:
        # 프로필, 암호 수정 함수에서 빈 form 객체를 바로 만들면 안됨 
        # 그 이유는 폼이 모델에 대한 모델 폼이기에 수정이 아닌 새로운 걸 생성 하려 함
        form = ProfileForm(instance=request.user)

    
    return render(request, "accounts/profile_edit_form.html", {
        "form" : form,
    })
   


class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    # reverse_lazy는 CBV에서 사용하는 reverse 함수이다.
    success_url = reverse_lazy("password_change")
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm

    # CBV에서도 form 객체를 사용할 수 있다.
    # form_valid 하다면 아래 함수가 실행된다.
    def form_valid(self, form):
        messages.success(self.request, "암호를 성공적으로 변경했습니다!")
        return super().form_valid(form)


password_change = PasswordChangeView.as_view()