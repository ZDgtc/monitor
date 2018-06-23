# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('home_application/index.html')

def select(request):
    s = request.POST.get('value', None)
    if s == 'bk':
        return 'congratulation!'
    else:
        return 'You chose a wrong one.'


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
