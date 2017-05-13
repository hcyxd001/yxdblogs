# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from tinymce.models import HTMLField
# Create your models here.
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=200)
    #文章的网址
    
    #文章内容
    body = models.TextField()
    #文章发布时间
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        #设计数据库的表名字
        db_table = 'mainsite'
        #以pub_date对文章进行排序
        ordering = ('-pub_date',)
    
    #使用__unicode__提供此类产生的数据项
    def __udenicode__(self):
        return self.title

class MysqlContent(models.Model):
    title = models.CharField(max_length=100)
    
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=200,default='')

    class Mete:
        db_table = 'mysql_content'

        ordering = ('-pub_date',)

    def __udenicode__(self):
        return self.title

class RedisContent(models.Model):
    title = models.CharField(max_length=100)
    
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=200,default='')

    class Mete:
        db_table = 'redis_content'

        ordering = ('-pub_date',)

    def __udenicode__(self):
        return self.title


class Python2Content(models.Model):
    title = models.CharField(max_length=100)
    
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=200,default='')

    class Mete:
        db_table = 'python2_content'

        ordering = ('-pub_date',)

    def __udenicode__(self):
        return self.title

class LinuxContent(models.Model):
    title = models.CharField(max_length=100)
   
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=200,default='')

    class Mete:
        db_table = 'linux_content'

        ordering = ('-pub_date',)

    def __udenicode__(self):
        return self.title

class MacContent(models.Model):
    title = models.CharField(max_length=100)
    
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=200,default='')

    class Mete:
        db_table = 'mac_content'

        ordering = ('-pub_date',)

    def __udenicode__(self):
        return self.title

class ExploitContent(models.Model):
    title = models.CharField(max_length=100)
    
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    file = models.CharField(max_length=200,default='')

    class Mete:
        db_table = 'Exploit_content'

        ordering = ('-pub_date',)

    def __udenicode__(self):
        return self.title