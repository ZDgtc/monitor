# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^get_biz_list/$', 'get_biz_list'),
    (r'^get_hosts_by_bizId/(\d+)$', 'get_hosts_by_biz_id'),
    (r'^execute_script/$', 'execute_script'),
    (r'^get_script_log_content/$', 'get_script_log_content'),
    (r'^host_state/$', 'host_state'),
    (r'^get_ip_by_biz_id/', 'get_ip_by_biz_id'),
    (r'^get_host_state/', 'get_host_state'),
    (r'^operations/$', 'operations'),
    (r'^get_operations/$', 'get_operations'),
    (r'^add_to_celery/$', 'add_to_celery'),
    (r'^remove_from_celery/$', 'remove_from_celery')
)
