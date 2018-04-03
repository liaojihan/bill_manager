# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django_web.django_bill.bill_dao import GetBillData
from django_web.django_bill import bill_dao
import json

result_type = 'application/json'


def bill(request):
    """初始化账单总览页面"""
    user_session = request.session.get('user_dict', '')
    if user_session:
        user_dict = {'user_name': user_session['user_name']}
        return render(request, 'page/bill/overview.html', user_dict)
    else:
        return HttpResponseRedirect('home')


def get_bill_data(request):
    user_id = request.session.get('user_dict', '').get('user_id', '')
    if user_id:
        bill_object = GetBillData(user_id=user_id)
        bill_type = bill_object.get_bill_data()
        data = {
            "bill_type": bill_type
        }
        return json.dumps(data)


def detailed(request):
    """初始化账单明细页面"""
    user_session = request.session.get('user_dict', '')
    if user_session:
        user_dict = {'user_name': user_session['user_name']}
        return render(request, 'page/bill/detailed.html', user_dict)
    else:
        return HttpResponseRedirect('home')


def get_table_data(request):
    result, result_count = bill_dao.get_bill_data()
    data = {
        "recordsTotal": result_count,
        "recordsFiltered": result_count,
        "data": result
    }
    return HttpResponse(json.dumps(data), content_type=result_type)


def bill_data_add(request):
    user_id = request.session.get('user_dict', '')['user_id']
    bill_request = request.POST
    result = bill_dao.bill_add(bill_request, user_id)
    return HttpResponse(json.dumps(result), content_type=result_type)


def bill_data_delete(request):
    if request.method == 'POST':
        id_array = request.POST.getlist('bills_id')
        result = bill_dao.bill_delete(id_array)
        return HttpResponse(json.dumps(result), content_type=result_type)
