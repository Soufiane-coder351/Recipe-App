from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from recipes.models import Recipe
from recipes.models import Favorites
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    template = loader.get_template("./recipes/index.html")
    recettes = Recipe.objects.all()
    return HttpResponse(template.render(request=request,context={"recettes":recettes}))

@login_required
def createrecipe(request):
    '''
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    instructions = models.TextField()
    '''
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        instructions = request.POST.get('instructions')
        user = request.user
        
        errors = []
        
        if Recipe.objects.filter(title=title).exists():
            errors.append("Titre de la recette existe déjà")
        
        if not errors:
            try:
                recipe = Recipe.objects.create(title=title,description=description,instructions=instructions,user=user)
                recipe.save()
                return redirect('profile')

            except Exception as e:
                errors.append(str(e))
        
        return render(request,'recipes/createrecipe.html', {'errors':errors, 'values' : {
            'title':title,
            'description':description,
            'instructions': instructions
        }})

    return render(request,"recipes/createrecipe.html")
    

def recette_info(request):
    return render(request,'recipes/recette_info.html')

@login_required
def afficher_favoris(request):
    favoris = Favorites.objects.filter(user=request.user)
    return render(request,'recipes/favorites.html',{"favoris":favoris})    