import user.views
from django.urls import re_path,path


urlpatterns = [
    path('login/',user.views.login, name='login'),
    path('signup/',user.views.signup , name='signup'),
    path('profile/',user.views.profile, name="profile"),
]
