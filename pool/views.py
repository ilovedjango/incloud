# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

from blockchain import wallet
from .models import OrdersServer, Subscription, Question, JobRequest, NumbersRequest, PvaAccount
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def servers(request):
    return render(request, 'servers.html')

def numbers(request):
    return render(request, 'numbers.html')

def pva(request):
    return render(request, 'pva.html')



# Server request
def ServerRequest(request):
    if request.POST:
        location = request.POST.get('location', '')
        time = request.POST.get('time', '')
        skype_id = request.POST.get('skypeid', '')
        email = request.POST.get('email', '')
        instructions = request.POST.get('instructions', '')
        order_type = request.POST.get('ordertype', '')
        tv_machine = request.POST.get('tvmachine', '')
        quantity = request.POST.get('quantity', '')
        payment_method = request.POST.get('payment', '')
        data = {"location": location, "time": time, "skype_id":skype_id, "email":email,
                "instructions":instructions, "order_type":order_type, "tv_machine":tv_machine,
                "quantity":quantity, "payment_method": payment_method
                }
        #return JsonResponse(data)
        order = OrdersServer(location=location, time=time, skype_id=skype_id, email=email, instructions=instructions,
                             order_type=order_type, tv_machine=tv_machine, quantity=quantity, payment_method=payment_method)
        order.save()
        done = "Your request was sent, we will contact you soon."
        context = {'success': done}
        return render(request, "server-request.html", context)
    else:
        return render(request, "server-request.html")


# Forwarded numbers request
def ForwardedNumbersRequest(request):
    if request.POST:
        email = request.POST.get('email')
        skype_id = request.POST.get('skypeid')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        pva = NumbersRequest(email=email, skype_id=skype_id, description=description, quantity=quantity)
        pva.save()
    return render(request, 'numbers-request.html')


# PVA Request
def PvaRequest(request):
    if request.POST:
        email = request.POST.get('email')
        skype_id = request.POST.get('skypeid')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        pva = PvaAccount(email=email, skype_id=skype_id, description=description, quantity=quantity)
        pva.save()
    return render(request, 'pva-request.html')




# Job offers
def Job(request):
    if request.POST:
        name_project = request.POST.get('name_project')
        project_description = request.POST.get('description')
        name = request.POST.get('name')
        email = request.POST.get('email')
        data = {"name_project": name_project, "project_description": project_description, 'name': name,
                'email': email, }
        # return JsonResponse(data)
        req = JobRequest(name_project=name_project, project_description=project_description, name=name, email=email)
        req.save()
        done = "Your request was sent, we will contact you soon."
        context = {'success': done}
        return render(request, "script-request.html", context)
    else:
        return render(request, "script-request.html", )


# Subscription form
def subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        data = {"email": email, "full_name": full_name}
        # return JsonResponse(data)
        subscr = Subscription(name=full_name, email=email)
        subscr.save()
        # Get goes here

# Contact form
def contact(request):
    if request.POST:
        first_name = request.POST.get('firstname', '')
        last_name = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        contactForm = Question(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
        contactForm.save()
        success = 'done'
        context = {'success': success}
        return render(request, 'contact-us.html', context)
    else:
        return render(request, 'contact-us.html')