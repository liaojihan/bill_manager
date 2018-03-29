# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_web.django_bill.bill_dao import GetBillData
import json


def bill(request):
    """初始化账单总览页面"""
    user_id = request.session.get('user_id', '')
    if user_id:
        return render(request, 'page/bill/overview.html')
    else:
        return HttpResponseRedirect('home')


def get_bill_data(request):
    user_id = request.session.get('user_id', '')
    if user_id:
        bill_object = GetBillData(user_id=user_id)
        bill_type = bill_object.get_bill_data()
        data = {
            "bill_type": bill_type
        }
        return json.dumps(data)


def detailed(request):
    """初始化账单明细页面"""
    user_id = request.session.get('user_id', '')
    if user_id:
        return render(request, 'page/bill/detailed.html')
    else:
        return HttpResponseRedirect('home')


def get_table_data(request):

    return None