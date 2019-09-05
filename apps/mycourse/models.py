# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=64, verbose_name='课程名称')
    description = models.CharField(max_length=255, verbose_name='课程描述')

    class Meta:
        verbose_name = '课程'
        db_table = 'course'


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=64, verbose_name='章节名称')
    description = models.CharField(max_length=255, verbose_name='章节描述')

    class Meta:
        verbose_name = '章节'
        db_table = 'lesson'


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=64, verbose_name='视频名称')
    description = models.CharField(max_length=255, verbose_name='视频描述')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        db_table = 'video'


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=64, verbose_name='课程资源名称')
    description = models.CharField(max_length=255, verbose_name='课程资源描述')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
        db_table = 'course_resource'
