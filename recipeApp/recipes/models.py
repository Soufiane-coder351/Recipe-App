

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



# Modèle pour l'ingrédient
class Produit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#for user the model, we already use the auth_user provided by django, just use : from django.contrib.auth.models import User

# Modèle pour la recette (Recipe)
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    instructions = models.TextField()

    def __str__(self):
        return self.title

# Relation ManyToMany entre Recipe et User pour les avis
class Avis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.TextField()  # Contenu de l'avis
    rating = models.PositiveIntegerField(default=0)  # Note (optionnelle)

    def __str__(self):
        return f'Avis de {self.user.username} sur {self.recipe.title}'
    
class Ingredient(models.Model):
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE)
    recette = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    qtté = models.TextField()

""