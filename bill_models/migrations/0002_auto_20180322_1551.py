# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bill',
            name='create_time',
            field=models.IntegerField(),
        ),
    ]