# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', blank=True, null=True)
    birthday = models.DateField(verbose_name=u'生日', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=u'地址', blank=True, null=True)
    age = models.IntegerField(verbose_name=u'年龄', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Female', u'女'), ('Male', '男')), verbose_name=u'性别',
                              default='Male')
    image = models.ImageField(upload_to='images/%Y/%m', verbose_name=u'头像')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=10, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '忘记密码')), max_length=8,
                                 verbose_name=u'类型')
    send_time = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
        db_table = 'email_verify_record'
