import user.views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', user.views.user_info, name = 'user information'),
]
