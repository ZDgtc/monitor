# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'home'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
    (r'^multiplication_compute/$', 'multiplication_compute'),
    (r'^get_latest_record', 'get_latest_record')
)
