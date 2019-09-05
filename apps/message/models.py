# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=64, verbose_name='消息名称')
    description = models.CharField(max_length=64, verbose_name='消息描述',null=True)

    class Meta:
        verbose_name = '消息'
        verbose_name_plural=verbose_name
        db_table = 'mesaget'
