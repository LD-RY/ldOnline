from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField


# 登陆表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


# 注册验证
class RegisterForm(forms.Form):
    '''注册验证表单'''
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    # 验证码，字段里面可以自定义错误提示信息
    captcha = CaptchaField()


# 忘记密码
class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


# 修改密码
class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)


class UploadImageForm(forms.ModelForm):
    '''用户更改图像'''
    class Meta:
        model=UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    '''个人中心信息修改'''
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender','birthday','address','mobile']
