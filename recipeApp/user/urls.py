import user.views
from django.urls import re_path,path


urlpatterns = [
    re_path(r'^$', user.views.user_info, name = 'user information'),
    path('login/',user.views.login),
    path('signup/',user.views.signup),
    path('user/',user.views.user),

]
