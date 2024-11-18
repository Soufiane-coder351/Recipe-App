import recipes.views 
from django.urls import path

urlpatterns=[
    path('',recipes.views.index),
    path('createrecipe',recipes.views.createrecipe),
]