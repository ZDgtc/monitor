# -*- coding: utf-8 -*-

from django.db import models

class MultRecord(models.Model):
    multiplier = models.IntegerField(u'乘数')
    multiplicand = models.IntegerField(u'被乘数')
    mult_result = models.IntegerField(u'结果')
