from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from recipes.models import Recipe,Avis
from recipes.models import Favorites
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
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
        image = request.FILES.get('image')
        user = request.user
        
        errors = []
        
        if Recipe.objects.filter(title=title).exists():
            errors.append("Titre de la recette existe déjà")
        
        if not errors:
            try:
                recipe = Recipe.objects.create(title=title,description=description,instructions=instructions,user=user,image=image)
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
    



def recette_info(request, title):
    recette = get_object_or_404(Recipe, title=title)
    is_favorited = Favorites.objects.filter(user=request.user, recette=recette).exists() if request.user.is_authenticated else False
    reviews = Avis.objects.filter(recipe=recette)
    return render(request, 'recipes/recette_info.html', {'recette': recette, 'is_favorited': is_favorited,'reviews':reviews})


@login_required
def afficher_favoris(request):
    favoris = Favorites.objects.filter(user=request.user)
    return render(request,'recipes/favorites.html',{"favoris":favoris})    

def chercher_recette(request):
    q = request.GET.get('query', '')  # Obtenir le mot-clé de recherche depuis l'URL
    recherches = Recipe.objects.filter(title__icontains=q)  # Rechercher dans le champ "title"
    return render(request, "recipes/search_result.html", {'recherches': recherches})




def toggle_favorite(request, recipe_id):
    # Récupérer la recette à partir de son ID
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Vérifier si cette recette est déjà dans les favoris de l'utilisateur
    favorite = Favorites.objects.filter(user=request.user, recette=recipe).first()

    if favorite:
        # Si la recette est déjà dans les favoris, on la supprime
        favorite.delete()
        messages.success(request, f"La recette '{recipe.title}' a été retirée de vos favoris.")
    else:
        # Sinon, on l'ajoute aux favoris
        Favorites.objects.create(user=request.user, recette=recipe)
        messages.success(request, f"La recette '{recipe.title}' a été ajoutée à vos favoris.")
    
    # Rediriger vers la page des détails de la recette
    return redirect('recette_info', title=recipe.title)

@login_required
def submit_review(request):
    if request.method == "POST":
        recipe_title= request.POST.get('recipe_title')
        try:
            recipe = Recipe.objects.get(title=recipe_title)
        except Recipe.DoesNotExist:
            return HttpResponse("Recipe not found", status=404)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')  

        if not comment:
            return HttpResponse("Comment field is required!", status=400)
        # Save the rating and comment to the database
        Avis.objects.create(recipe=recipe, user=request.user, content=comment, rating=rating)
        return redirect('recette_info', title=recipe.title)  # Redirect to the recipe page
    return HttpResponse("Invalid request method.", status=405)


