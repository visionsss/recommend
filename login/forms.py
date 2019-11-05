from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    sex_gender = (
        ('male', "男"),
        ('female', "女"),
    )
    province_gender = (
        ('GuangDong', '广东'),
    )
    subject_gender = (
        ('science', '理科'),
        ('art', '文科'),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # sex = forms.ChoiceField(label='性别', choices=sex_gender)
    # province = forms.ChoiceField(label='省份', choices=province_gender)
    # subject = forms.ChoiceField(label='科别', choices=subject_gender)
    # score = forms.IntegerField(label='高考分数', max_value=900, min_value=0, widget=forms.NumberInput)
    # captcha = CaptchaField(label='验证码')
