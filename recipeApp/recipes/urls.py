import recipes.views
from django.urls import re_path

urlpatterns=[
    re_path(r'^$', recipes.views.showrecipes, name = 'list of recipes'),
]


