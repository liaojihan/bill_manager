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
    """获取table数据"""
    user_id = request.session.get('user_dict', '')['user_id']
    page_data = request.GET
    result, result_count = bill_dao.get_bill_data(user_id, page_data)
    data = {
        "recordsTotal": result_count,
        "recordsFiltered": result_count,
        "data": result
    }
    return HttpResponse(json.dumps(data), content_type=result_type)


def bill_data_add(request):
    """记一笔"""
    user_id = request.session.get('user_dict', '')['user_id']
    bill_request = request.POST
    result = bill_dao.bill_add(bill_request, user_id)
    return HttpResponse(json.dumps(result), content_type=result_type)


def bill_data_delete(request):
    """删除/批量删除"""
    if request.method == 'POST':
        id_array = request.POST.getlist('bills_id')
        result = bill_dao.bill_delete(id_array)
        return HttpResponse(json.dumps(result), content_type=result_type)


def get_detailed(request):
    """详情"""
    bill_id = request.GET.get('id', '')
    result = bill_dao.get_detailed_data(bill_id)
    return HttpResponse(json.dumps(result), content_type=result_type)


def edit_bill(request):
    """根据ID获取单个bill对象"""
    bill_id = request.GET.get('id', '')
    result = bill_dao.edit_bill_data(bill_id)
    return HttpResponse(json.dumps(result), content_type=result_type)


def update_bill(request):
    """更新bill"""
    bill_request = request.POST
    result = bill_dao.update_bill_data(bill_request)
    return HttpResponse(json.dumps(result), content_type=result_type)


def search_bill(request):
    """快速查找"""
    bill_form = request.GET
    user_id = request.session.get('user_dict', '')['user_id']
    result, result_count = bill_dao.get_search_bill(bill_form, user_id)
    data = {
        "recordsTotal": result_count,
        "recordsFiltered": result_count,
        "data": result
    }
    return HttpResponse(json.dumps(data), content_type=result_type)
