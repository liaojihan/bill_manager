from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'page/login/index.html')

def user_login(request):
    user_dict = request.POST
    print user_dict
