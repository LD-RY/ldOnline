"""ldOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import xadmin
from django.urls import path,include,re_path
from django.views.static import serve
from ldOnline.settings import MEDIA_ROOT
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView,LogoutView
from organization.views_bak01 import OrgView
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 处理图片显示的url，使用django自带的server，传入参数告诉他去哪个路径找，我们有配置好的路径MEDIAROOT
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),# 静态文件
    path('ueditor/',include("DjangoUeditor.urls")),
    path('captcha/',include('captcha.urls')),


    path('',TemplateView.as_view(template_name='index.html'),name='index'),# 首页
    path('login/',LoginView.as_view(),name='login'),# 登录
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name='register'),#注册
    re_path("active/(?P<active_code>.*)/",ActiveUserView.as_view(),name='user_active'),#激活用户
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),# 忘记密码
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),# 修改密码get方式的提交地址
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),# 修改密码post方式的提交地址

    path('users/',include('users.urls',namespace='users')),
    path("org/",include('organization.urls',namespace='org')),
    path('course/',include('course.urls',namespace='course'))

]
