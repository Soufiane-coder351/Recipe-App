from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from recipes.models import Recipe,Avis
from recipes.models import Favorites
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


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
    

def recette_info(request, title):
    recette = Recipe.objects.get(title=title)
    reviews = Avis.objects.filter(recipe=recette)
    for review in reviews:
        review.filled_stars = [1] * review.rating  # List of 1's for filled stars
        review.empty_stars = [1] * (5 - review.rating)  # List of 1's for empty stars

    return render(request,'recipes/recette_info.html',{'recette': recette, 'reviews':reviews})

@login_required
def afficher_favoris(request):
    favoris = Favorites.objects.filter(user=request.user)
    return render(request,'recipes/favorites.html',{"favoris":favoris})    

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
        avi=Avis.objects.get(recipe=recipe, user=request.user, content=comment, rating=rating)
        messages.success(request, "Your review has been submitted!")
        return redirect('recette_info', title=recipe.title)  # Redirect to the recipe page
    return HttpResponse("Invalid request method.", status=405)


