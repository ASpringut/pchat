from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile

def index(request):
    template = loader.get_template('chat/index.html')
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template('registration/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user = user, user_type=Profile.OWNER)
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            return HttpResponse(template.render({'user_creation_form':form}, request))
    else:
        form = UserCreationForm()

    return HttpResponse(template.render({'user_creation_form':form}, request))

def vetregister(request):    
    template = loader.get_template('registration/vetregister.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user = user, user_type=Profile.VET)
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            return HttpResponse(template.render({'user_creation_form':form}, request))
    else:
        form = UserCreationForm()

    return HttpResponse(template.render({'user_creation_form':form}, request))

