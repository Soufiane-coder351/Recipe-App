from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from recipes import models
# Create your views here.
def index(request):
    template = loader.get_template("./recipes/index.html")
    return HttpResponse(template.render(request=request))

def createrecipe(request):
    template = loader.get_template("./recipes/createrecipe.html")
    return HttpResponse(template.render(request=request))

def search(request):
    query = request.GET.get('q')
    if query:
        results = models.Recipe.objects.filter(title__icontains=query)
    else:
        results = models.Recipe.objects.none()  

    return render(request, 'search.html', {'resultats': results, 'query': query})
    
    
        