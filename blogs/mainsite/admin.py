# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class MysqlAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class RedisAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class Python2Admin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class LinuxAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class MacAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

class ExploitAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
admin.site.register(Post,PostAdmin)

admin.site.register(MysqlContent,MysqlAdmin)

admin.site.register(RedisContent,RedisAdmin)

admin.site.register(Python2Content,Python2Admin)

admin.site.register(LinuxContent,LinuxAdmin)

admin.site.register(MacContent,MacAdmin)

admin.site.register(ExploitContent,ExploitAdmin)
