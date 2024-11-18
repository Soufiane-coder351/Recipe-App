

from django.db import models

# Create your models here.


from django.db import models

# Modèle pour l'ingrédient
class Produit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modèle pour l'utilisateur (User)
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

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
    rating = models.IntegerField(default=0)  # Note (optionnelle)

    def __str__(self):
        return f'Avis de {self.user.username} sur {self.recipe.title}'
    
class Ingredient(models.Model):
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE)
    recette = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    qté = models.TextField()

""