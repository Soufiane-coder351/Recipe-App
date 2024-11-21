from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from recipes.models import Recipe,Avis , Ingredient, Produit, Favorites, Step
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.utils import IntegrityError

def index(request):
    template = loader.get_template("./recipes/index.html")
    liste_recettes = Recipe.objects.all()
    paginator = Paginator(liste_recettes, 3)  # 12 recettes par page
    page_number = request.GET.get('page')  # Numéro de la page actuelle
    recettes = paginator.get_page(page_number)  # Obtenez les recettes pour la page

    return HttpResponse(template.render(request=request,context={"recettes":recettes}))



@login_required
def createrecipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.user
        errors = []

        # Get ingredients from the request
        ingredients = request.POST.get('ingredients')  # Get the comma-separated string
        
        # Get instructions steps dynamically
        steps = []
        step_count = 1
        while f'stepDescription{step_count}' in request.POST:
            step_description = request.POST.get(f'stepDescription{step_count}')
            step_image = request.FILES.get(f'stepImage{step_count}')
            if step_description:
                steps.append({
                    'description': step_description,
                    'image': step_image,
                    'order': step_count,  # Set the step order based on the count
                })
            step_count += 1

        if Recipe.objects.filter(title=title).exists():
            errors.append("Titre de la recette existe déjà")

        if not errors:
            try:
                # Create the recipe
                recipe = Recipe.objects.create(title=title, description=description, user=user, image=image)
                recipe.save()

                # Convert the comma-separated string into a list for ingredients
                ingredient_list = ingredients.split(',') if ingredients else []

                # Create ingredients for the recipe
                for ingredient_name in ingredient_list:
                    if ingredient_name:
                        produit, created = Produit.objects.get_or_create(name=ingredient_name)
                        Ingredient.objects.create(produit=produit, recette=recipe, qtté="")  # Assuming no quantity for now

                # Create steps for the recipe
                for step_data in steps:
                    Step.objects.create(
                        recipe=recipe,
                        description=step_data['description'],
                        image=step_data['image'],
                        order=step_data['order'],
                    )

                return redirect('profile')

            except Exception as e:
                errors.append(str(e))

        return render(request, 'recipes/createrecipe.html', {'errors': errors, 'values': {
            'title': title,
            'description': description,
            'steps': steps,
        }})

    return render(request, "recipes/createrecipe.html")


def recette_info(request, recipe_id):
    try:
        recette=Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return HttpResponse("Recipe not found", status=404)
    is_favorited = Favorites.objects.filter(user=request.user, recette=recette).exists() if request.user.is_authenticated else False
    reviews = Avis.objects.filter(recipe=recette)
    ingredients = Ingredient.objects.filter(recette=recette)
    steps = Step.objects.filter(recipe=recette)
    return render(request, 'recipes/recette_info.html', {'recette': recette, 'is_favorited': is_favorited,'reviews':reviews,'ingredients':ingredients,'steps':steps})


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
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return HttpResponse("Recipe not found", status=404)
    
    # Vérifier si cette recette est déjà dans les favoris de l'utilisateur
    favorite = Favorites.objects.filter(user=request.user, recette=recipe).first()

    if favorite:
        # Si la recette est déjà dans les favoris, on la supprime
        favorite.delete()
        # messages.success(request, f"La recette '{recipe.title}' a été retirée de vos favoris.")
    else:
        # Sinon, on l'ajoute aux favoris
        Favorites.objects.create(user=request.user, recette=recipe)
        # messages.success(request, f"La recette '{recipe.title}' a été ajoutée à vos favoris.")
    
    # Rediriger vers la page des détails de la recette
    return redirect('recette_info', recipe_id=recipe.id)

@login_required
def submit_review(request):
    if request.method == "POST":
        recipe_id= request.POST.get('recipe_id')
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return HttpResponse("Recipe not found", status=404)
        
        try:
            rating = request.POST.get('rating')            
            comment = request.POST.get('comment')  
            # Save the rating and comment to the database
            Avis.objects.create(recipe=recipe, user=request.user, content=comment, rating=rating)
            messages.success(request, "Votre avis est transmis avec succès !")
        except IntegrityError as e:
            messages.error(request,"Vous devez mettre une note")
        
        return redirect('recette_info', recipe_id=recipe.id)  # Redirect to the recipe page
    return HttpResponse("Invalid request method.", status=405)


