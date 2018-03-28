# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django_web.django_bill import home_dao
import json

result_type = 'application/json'


def home(request):
    """初始化首页"""
    return render(request, 'page/login/index.html')


def user_login(request):
    """用户登录"""
    user_dict = request.GET
    result = home_dao.user_login(user_dict)
    return HttpResponse(json.dumps(result), content_type=result_type)


def forget(request):
    """初始化用户名验证页面"""
    return render(request, 'page/login/forget_password.html')


def confirm_username(request):
    """验证用户名"""
    username = request.GET['username']
    result = home_dao.update_forget_password(username)
    return HttpResponse(json.dumps(result), content_type=result_type)


def get_id_question(request):
    """初始化验证密码问题页面"""
    username = request.GET.get('username', '')
    result = dict()
    if username:
        user_id, question = home_dao.get_id_question(username)
        result = {'user_id': user_id, 'question': question}
        page = 'page/login/check_answer.html'
    else:
        page = 'page/error/500.html'
    return render(request, page, result)


def check_answer(request):
    """验证密码答案"""
    user_dict = request.GET
    result = home_dao.check_user_answer(user_dict)
    return HttpResponse(json.dumps(result), content_type=result_type)


def user_add(request):
    """用户注册"""
    user_dict = request.POST
    result = home_dao.user_add(user_dict)
    return HttpResponse(json.dumps(result), content_type=result_type)


def reset_password(request):
    """初始化重置密码页面"""
    user_id = request.GET.get('user_id', '')
    user_dict = dict()
    if user_id:
        user_dict = {'user_id': user_id}
        page = 'page/login/reset_password.html'
    else:
        page = 'page/error/500.html'
    return render(request, page, user_dict)


def reset_user_password(request):
    user_dict = request.POST
    result = home_dao.reset_password_dao(user_dict)
    return HttpResponse(json.dumps(result), content_type=result_type)


def page_error(request):
    return render_to_response('page/error/500.html')
