"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from api import views as apiviews
from cmdb import views as cmdbviews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', apiviews.Root.as_view()),
    # 认证模块
    url(r'^api/v1/auth/$', apiviews.AuthView.as_view()),
    # 用户信息
    url(r'^api/v1/user_info/$', apiviews.UserInfo.as_view()),
    # 获取虚拟机信息
    url(r'^api/v1/get_vm_info/$', cmdbviews.VirtualMachineView.as_view()),
    # 获取宿主机信息
    url(r'^api/v1/get_pm_info/$', cmdbviews.PhysicalMachineView.as_view()),
    # 虚机匹配自己的宿主机
    url(r'^api/v1/vm_match_pm/$', cmdbviews.VirtualMatchPhysicalView.as_view()),
]