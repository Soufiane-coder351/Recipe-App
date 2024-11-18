from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template("./recipes/index.html")
    return HttpResponse(template.render(request=request))

def login(request):
    template = loader.get_template("./recipes/login.html")
    return HttpResponse(template.render(request=request))

def signup(request):
    template = loader.get_template("./recipes/signup.html")
    return HttpResponse(template.render(request=request))

def user(request):
    template = loader.get_template("./recipes/user.html")
    return HttpResponse(template.render(request=request))

def createrecipe(request):
    template = loader.get_template("./recipes/createrecipe.html")
    return HttpResponse(template.render(request=request))