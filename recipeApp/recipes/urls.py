import recipes.views 
from django.urls import path

urlpatterns=[
    path('',recipes.views.index),
    path('login/',recipes.views.login),
    path('signup/',recipes.views.signup),
    path('user/',recipes.views.user),
    path('createrecipe',recipes.views.createrecipe),
]