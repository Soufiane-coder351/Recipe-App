from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user_info(request):
    message = 'Name <br> Last Name <br> Birth date <br> E-mail adress <br> Date of registration'
    return HttpResponse(message)


