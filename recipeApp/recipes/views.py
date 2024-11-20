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

@login_required
def createrecipe(request):
    return render(request,"recipes/createrecipe.html")
    

def recette_info(request):
    return render(request,'recipes/recette_info.html')

@login_required
def afficher_favoris(request):
    favoris = Favorites.objects.filter(user=request.user)
    return render(request,'recipes/favorites.html',{"favoris":favoris})    