import recipes.views 
from django.urls import path


urlpatterns=[
    path('',recipes.views.index,name='recipes'),
    path('createrecipe',recipes.views.createrecipe, name="createrecipe"),
    path('recette-info',recipes.views.recette_info, name="recette_info"),
    path('favoris/',recipes.views.afficher_favoris, name="recettes_favorites"),
    path('<str:title>',recipes.views.recette_info, name="recette_info"),
    path('chercher_recette/', recipes.views.chercher_recette, name='chercher_recette'),
]