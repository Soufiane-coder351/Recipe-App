from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from recipes.models import Recipe

def index(request):
    template = loader.get_template("./recipes/index.html")
    recettes = Recipe.objects.all()
    return HttpResponse(template.render(request=request,context={"recettes":recettes}))

def createrecipe(request):
    template = loader.get_template("./recipes/createrecipe.html")
    return HttpResponse(template.render(request=request))

def recette_info(request):
    return render(request,'recipes/recette_info.html')

def afficher_recettes(request):
    return render(request, 'index.html', {'tortilla' : tortilla})