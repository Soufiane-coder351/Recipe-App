from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import RECIPES
# Create your views here.

def index(request):
    message = "Bienvenue dans le site collaboratif de recettes pour les étudiants de Paris Saclay!"
    return HttpResponse(message)

def showrecipes(request):
    message = "<p style='font-size: 100px;'> Recettes du jour.</p> <br>"
    for recipe in RECIPES:
        message += "<b>" + recipe['name'] + "<b>"+ "<br>"
    return HttpResponse(message)

