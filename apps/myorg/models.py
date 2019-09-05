# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'组织名称')
    description = models.CharField(verbose_name=u'组织描述', max_length=255)

    class Meta:
        verbose_name = '组织'
        db_table = 'organization'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
