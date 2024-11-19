from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from recipes.models import Recipe
from recipes.models import Favorites
from django.contrib.auth.decorators import login_required


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

@login_required
def afficher_favoris(request):
    template = loader.get_template("./recipes/favorites.html") #j'anticipe mais il ft que j'ai un fichier html pour les favoris solal s'en charge
    favoris = Favorites.objects.filter(user=request.user)
    return HttpResponse(template.render(request=request,context={"favoris":favoris}))
    
    
    
    