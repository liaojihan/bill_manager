# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_web.django_bill import type_dao
import json

result_type = 'application/json'


def get_type(request):
    type_data = type_dao.get_type_data()
    return HttpResponse(json.dumps(type_data), content_type=result_type)


def type_add(request):
    type_name = request.POST.get('name', '')
    result = type_dao.add_type_data(type_name)
    return HttpResponse(json.dumps(result), content_type=result_type)


def get_edit_type(request):
    bill_id = request.GET.get('bill_id', '')
    result = type_dao.get_edit_type_data(bill_id)
    return HttpResponse(json.dumps(result), content_type=result_type)
