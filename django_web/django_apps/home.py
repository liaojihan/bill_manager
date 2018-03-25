# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django_web.django_bill import home_dao
import json


def home(request):
    """初始化首页"""
    return render(request, 'page/login/index.html')


def user_login(request):
    """用户登录"""
    user_dict = request.GET
    result = home_dao.user_login(user_dict)
    return HttpResponse(json.dumps(result), content_type='application/json')


def forget(request):
    """初始化忘记密码页面"""
    return render(request, 'page/login/forget_password.html')

def confirm_username(request):
    """修改忘记密码"""
    username = request.GET['username']
    result = home_dao.update_forget_password(username)
    return HttpResponse(json.dump(result), content_type="application/json")


def user_add(request):
    """用户注册"""
    user_dict = request.POST
    result = home_dao.user_add(user_dict)
    return HttpResponse(json.dumps(result), content_type="application/json")

