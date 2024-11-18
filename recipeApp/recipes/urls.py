import recipes.views 
from django.urls import path

urlpatterns=[
    path('',recipes.views.index,name='recipes'),
    path('createrecipe',recipes.views.createrecipe, name="createrecipe"),
]