from django.http import HttpResponse
from django.shortcuts import render
from django_web.django_bill import bill_dao


def bill_init(request):
    return render(request, 'page/bill/bill.html')
