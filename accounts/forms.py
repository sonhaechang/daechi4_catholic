from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm,
    PasswordChangeForm as AuthPasswordChangeForm,
    PasswordResetForm as AuthPasswordResetForm
)
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from accounts.models import Profile
from accounts.services import profile_create, profile_save


check_last_name = RegexValidator(r"[ㄱ-힣]{1,2}", "한글 성을 1자 혹은 2자 입력해주세요.")
check_first_name = RegexValidator(r"[ㄱ-힣]{2,3}", "한글 이름을 2자 혹은 3자 입력해주세요.")


class SignupForm(UserCreationForm):
    baptism = forms.CharField()
    birthday = forms.CharField()
    last_name = forms.CharField(validators=[check_last_name])
    first_name = forms.CharField(validators=[check_first_name])

    phone1 = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select'}), choices = ([('010','010')]), required=True)
    phone2 = forms.CharField(
        widget=forms.TextInput(attrs={'type':'number', 'class': 'form-control'}), required=True)
    phone3 = forms.CharField(
        widget=forms.TextInput(attrs={'type':'number', 'class': 'form-control'}), required=True)


    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('last_name', 'first_name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        class_fields = {
            'username': _('아이디'), 'password1': _('비밀번호'), 'password2': _('비밀번호 확인'), 
            'last_name': _('성'), 'first_name': _('이름'), 'email': _('이메일'), 
            'baptism': _('세례명'), 'birthday': _('생년월일')
        }

        for field_name in list(class_fields.keys()):
            self.fields[field_name].label = class_fields[field_name]
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': class_fields[field_name],
            })

        self.fields['email'].help_text = _('비밀번호 분실시 필요하니 정확히 입력해주세요.')

    def save(self):
        user = super().save()
        profile_create(user, self.cleaned_data)
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['username'].label = _('아이디')
        self.fields['password'].label = _('비밀번호')


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()
    last_name = forms.CharField(validators=[check_last_name])
    first_name = forms.CharField(validators=[check_first_name]) 

    phone1 = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select'}), choices = ([('010','010')]), required=True)
    phone2 = forms.CharField(
        widget=forms.TextInput(attrs={'type':'number', 'class': 'form-control'}), required=True)
    phone3 = forms.CharField(
        widget=forms.TextInput(attrs={'type':'number', 'class': 'form-control'}), required=True)

    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'email', 'baptism', 'phone1', 'phone2', 'phone3', 'birthday']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        class_fields = {
            'last_name': _('성'), 'first_name': _('이름'), 
            'email': _('이메일'), 'baptism': _('세례명'), 
            'birthday': _('생년월일')
        }

        for field_name in list(class_fields.keys()):
            self.fields[field_name].label = class_fields[field_name]
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': class_fields[field_name],
            })

        self.fields['email'].help_text = _('비밀번호 분실시 필요하니 정확히 입력해주세요.')

    def save(self):
        user = self.user
        profile_save(user, self.cleaned_data)


class ProfileDetailForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'disabled': 'True'})


class PasswordChangeForm(AuthPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['old_password', 'new_password1', 'new_password2']
        self.fields['old_password'].widget.attrs.pop("autofocus", None)

        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field_name,
                'oninput': "checkChangePasswordInput(this)",
            })


class PasswordResetForm(AuthPasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_fields = {'email': _('이메일')}

        for field_name in list(class_fields.keys()):
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field_name,
            })