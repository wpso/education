# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-11 15:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 23, 19, 37, 102000)),
        ),
    ]
