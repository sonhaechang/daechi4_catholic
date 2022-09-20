from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as django_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from accounts.forms import (
    SignupForm,
    LoginForm, 
    ProfileDetailForm, ProfileForm, 
    PasswordChangeForm,
    PasswordResetForm
)
from accounts.services import profile_form_initial, get_birthday

from core.decorators import logout_required
from core.mixins import LogOutOnlyView


# Create your views here.
@logout_required
def agreement(request):
    request.session['agreement'] = False
    if request.method == 'POST':
        if request.POST.get('agree1', False) and request.POST.get('agree2', False):
            request.session['agreement'] = True
            return redirect('/accounts/signup')
        else:
            messages.info(request, "약관에 모두 동의해주세요.")
    return render(request, 'accounts/container/agreement.html')


@logout_required
def signup(request):
    # 약관 비동의로 접근시 약관동의 페이지로 redirect
    if not request.session.get('agreement', False):
        return redirect('/accounts/agreement')
    request.session['agreement'] = False

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            django_login(request, user) # 로그인 처리
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/container/signup_form.html', {'form': form,})

@logout_required
def login(request):
    if request.method == 'POST':
        # 로그인 성공 후 이동할 URL. 주어지지 않으면 None
        next_url = request.GET.get('next')

        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Django의 auth앱에서 제공하는 login함수를 실행해 앞으로의 요청/응답에 세션을 유지한다
            django_login(request, user)
            # next_url가 존재하면 해당 위치로, 없으면 메인 목록 화면으로 이동
            return redirect(next_url if next_url else '/')
        # 인증에 실패하면 login_form에 non_field_error를 추가한다
        form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        form = LoginForm()
        next_url = request.GET.get('next')
    return render(request, 'accounts/container/login_form.html', {'form': form})


@login_required
def profile(request):
    form = ProfileDetailForm(initial=profile_form_initial(request))

    return render(request, 'accounts/container/profile.html', {
        'form': form,
        'app_name': 'profile',
        'birthday': get_birthday(request.user),
        'disabled': 'True'
    })


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(
            request.POST, initial=profile_form_initial(request), user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = ProfileForm(initial=profile_form_initial(request), user=request.user)

    return render(request, 'accounts/container/profile_edit.html', {
        'form': form,
        'app_name': 'profile',
        'birthday': get_birthday(request.user),
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('profile')
        else:
            messages.error(request, '아래 오류를 수정하십시오.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/container/change_password.html', {
        'form': form,
        'app_name': 'change_password'
    })


class MyPasswordResetView(LogOutOnlyView, PasswordResetView):
    success_url = reverse_lazy('login')
    form_class = PasswordResetForm
    template_name = 'accounts/container/password_reset_form.html'
    # email_template_name = '...'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'password_reset'
        return context

    def form_valid(self, form):
        messages.info(self.request, '비밀번호 변경 이메일이 전송되었습니다.')
        return super().form_valid(form)


class MyPasswordResetConfirmView(LogOutOnlyView, PasswordResetConfirmView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/container/password_reset_confirm.html'
    # email_template_name = '...'

    def form_valid(self, form):
        messages.info(self.request, '비밀번호가 성공적으로 변경되었습니다.')
        return super().form_valid(form)