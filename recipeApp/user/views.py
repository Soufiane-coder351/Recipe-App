from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def user_info(request):
    message = 'Name <br> Last Name <br> Birth date <br> E-mail adress <br> Date of registration'
    return HttpResponse(message)



def login(request):
    template = loader.get_template("./user/login.html")
    return HttpResponse(template.render(request=request))

def signup(request):
    template = loader.get_template("./user/signup.html")
    return HttpResponse(template.render(request=request))

def user(request):
    template = loader.get_template("./user/user.html")
    return HttpResponse(template.render(request=request))
