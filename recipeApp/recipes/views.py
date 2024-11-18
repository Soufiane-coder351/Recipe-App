from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    template = loader.get_template("./recipes/index.html")
    return HttpResponse(template.render(request=request))

def createrecipe(request):
    template = loader.get_template("./recipes/createrecipe.html")
    return HttpResponse(template.render(request=request))
