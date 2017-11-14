# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import OrdersServer, JobRequest, Subscription, Question, PvaAccount, NumbersRequest


class OrdersServerAdmin(admin.ModelAdmin):
    list_display = ('location', 'time', 'skype_id', 'email', 'instructions', 'order_type', 'tv_machine', 'quantity', 'payment_method')
    list_filter = ('time', 'location', 'quantity', 'payment_method')
admin.site.register(OrdersServer, OrdersServerAdmin)


class JobRequestAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'project_description', 'name', 'email')
admin.site.register(JobRequest, JobRequestAdmin)

class PvaAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'skype_id', 'description', 'quantity')
admin.site.register(PvaAccount, PvaAccountAdmin)

class NumbersRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'skype_id', 'description', 'quantity', 'forward_number', 'how_many_per_day', 'delivery_time', 'quantity')
admin.site.register(NumbersRequest, NumbersRequestAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(Subscription, SubscriptionAdmin)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'message')
admin.site.register(Question, ContactFormAdmin)