# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_web.django_bill import type_dao
import json

result_type = 'application/json'


def get_type(request):
    type_data = type_dao.get_type_data()
    return HttpResponse(json.dumps(type_data), content_type=result_type)
