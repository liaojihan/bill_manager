# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    """用户"""
    user_name = models.CharField(max_length=128)
    user_password = models.CharField(max_length=128)
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)

    class Meta:
        db_table = 'user'


class Bill(models.Model):
    """账单"""
    amount = models.IntegerField()
    create_time = models.DateTimeField()
    is_delete = models.BooleanField()
    type = models.ForeignKey('ConsumptionType')
    user = models.ForeignKey('User')

    class Meta:
        db_table = 'bill'


class ConsumptionType(models.Model):
    """消费类型"""
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=128)

    class Meta:
        db_table = 'consumption_type'
