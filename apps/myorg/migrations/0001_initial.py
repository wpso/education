# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-11 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u7ec4\u7ec7\u540d\u79f0')),
                ('description', models.CharField(max_length=255, verbose_name='\u7ec4\u7ec7\u63cf\u8ff0')),
            ],
            options={
                'db_table': 'organization',
                'verbose_name': '\u7ec4\u7ec7',
                'verbose_name_plural': '\u7ec4\u7ec7',
            },
        ),
    ]