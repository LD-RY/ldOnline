from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from DjangoUeditor.models import UEditorField
# Create your models here.

class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField(max_length=50,default='',verbose_name='昵称')
    birthday = models.DateField(null=True,blank=True,verbose_name='生日')
    gender = models.CharField(max_length=10,choices=gender_choices,default='female',verbose_name='性别')
    address = UEditorField(max_length=100,default='',verbose_name='地址')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号',)
    image = models.ImageField(upload_to='images/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# EmailVerifyRecord   邮箱验证码
class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码'),
        ('update_email','修改邮箱')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=30)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name



# Banner 轮播图
class Banner(models.Model):
    title = models.CharField('标题',max_length=100)
    # image是图片的上传地址
    image = models.ImageField('轮播图',upload_to='banner/%Y%m',max_length=100)
    # url是图片的路径
    url = models.URLField('访问地址',max_length=200)
    # index控制轮播图的播放顺序
    index = models.IntegerField('顺序',default=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

