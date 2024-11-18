import user.views
from django.urls import re_path,path


urlpatterns = [
    path('login/',user.views.login_view, name='login'),
    path('signup/',user.views.signup_view , name='signup'),
    path('profile/',user.views.profile_view, name="profile"),
    path('logout/', user.views.logout_view, name='logout'),

]
