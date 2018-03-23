# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_password = models.CharField(max_length=128)
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    is_delete = models.BooleanField()

    class Meta:
        db_table = 'user'


class Bill(models.Model):
    bill_type = models.CharField(max_length=128)
    amount = models.IntegerField()
    create_time = models.IntegerField()
    is_delete = models.BooleanField()

    class Meta:
        db_table = 'bill'
