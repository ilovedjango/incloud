# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class OrdersServer(models.Model):
    location = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    skype_id = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    instructions = models.CharField(max_length=300)
    order_type = models.CharField(max_length=30)
    tv_machine = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)

    def __unicode__(self):
        return (self.location)

# PVA Requests
class PvaAccount(models.Model):
    email = models.CharField(max_length=30)
    skype_id = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    quantity = models.CharField(max_length=30)

# Phone numbers
class NumbersRequest(models.Model):
    email = models.CharField(max_length=30)
    skype_id = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    forward_number = models.CharField(max_length=30)
    how_many_per_day = models.CharField(max_length=30)
    delivery_time = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)

class JobRequest(models.Model):
    name_project = models.CharField(max_length=30)
    project_description = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

class Subscription(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Question(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    message = models.CharField(max_length=30)











