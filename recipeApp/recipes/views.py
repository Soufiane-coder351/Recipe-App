from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    message = "Bienvenue dans le site collaboratif de recettes pour les étudiants de Paris Saclay!"
    return HttpResponse(message)

def showrecipes(request):
    message = 'Tiramisu <br> Crêpes <br> Omelette au fromage'
    return HttpResponse(message)

