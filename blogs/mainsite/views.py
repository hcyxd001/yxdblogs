# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

from models import *

from datetime import datetime

from django.template.loader import get_template

from django.shortcuts import redirect

# Create your views here.

#def homepage(request):
#    posts = Post.objects.all()
#    post_list = list()
#    for count,post in enumerate(posts):
#        post_list.append("No.{}:".format(str(count)) + str(post) + "<br>")

#    return HttpResponse(post_list)

def homepage(request):

    template = get_template('essay/index.html')

    mysql = MysqlContent.objects.all()

    now = datetime.now()

    html = template.render(locals())

    return HttpResponse(html)

def showpost(request,slug):

    template = get_template('post.html')

    try:
        post = Post.objects.get(slug=slug)
        if post!=None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def mysql_url(request):

    mysqls = MysqlContent.objects.all()

    list1 = []

    for mysql in mysqls:

        list1.append([mysql.id,mysql.title])

    content = {'mysql':list1}

    return JsonResponse(content)

def redis_url(request):

    rediss = RedisContent.objects.all()

    list1 = []

    for redis in rediss:

        list1.append([redis.id,redis.title])

    content = {'redis':list1}

    return JsonResponse(content)

def python2_url(request):

    python2s = Python2Content.objects.all()

    list1 = []

    for python2 in python2s:

        list1.append([python2.id,python2.title])

    content = {'python2':list1}

    return JsonResponse(content)

def linux_url(request):

    linuxs = LinuxContent.objects.all()

    list1 = []

    for linux in linuxs:

        list1.append([linux.id,linux.title])

    content = {'linux':list1}

    return JsonResponse(content)

def mac_url(request):

    macs = MacContent.objects.all()

    list1 = []

    for mac in macs:

        list1.append([mac.id,mac.title])

    content = {'mac':list1}

    return JsonResponse(content)

def exploit_url(request):

    exploits = ExploitContent.objects.all()

    list1 = []

    for exploit in exploits:

        list1.append([exploit.id,exploit.title])

    content = {'exploit':list1}

    return JsonResponse(content)

def mysql_content(request,id):

    mysql = MysqlContent.objects.filter(id=id)

    for i in mysql:
        id = i.id
        
        body = i.body

    content = {'id':id,'body':body}

    return JsonResponse(content)