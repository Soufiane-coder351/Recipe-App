from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def user_info(request):
    message = 'Name <br> Last Name <br> Birth date <br> E-mail adress <br> Date of registration'
    return HttpResponse(message)



def login_view(request):
    if request.method == 'POST':
        # Get form data from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Initialize an empty list for errors
        errors = []

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If authentication fails, display an error
        if user is None:
            errors.append("Invalid username or password.")
        else:
            # If authentication is successful, log the user in
            login(request, user)

            # Redirect to the profile page or home page after successful login
            return redirect('profile')  # Adjust to your target page after login

        # If there are errors, render the login page with the error messages
        return render(request, 'user/login.html', {'errors': errors})

    return render(request, 'user/login.html')
    
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Initialize an empty list for errors
        errors = []

        # Validate the form data manually
        if password != confirm_password:
            errors.append("Passwords do not match.")
        
        if len(password) < 8:  # You can add more validation checks here
            errors.append("Password must be at least 8 characters long.")
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            errors.append("Username already taken.")
        
        # If no errors, create the user
        if not errors:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                # Log the user in
                login(request, user)

                # Redirect to the profile or home page after successful signup
                return redirect('profile')  # Make sure you have a 'profile' page or any other page
            except Exception as e:
                errors.append(str(e))

        # If there are errors, render the signup page with the error messages
        return render(request, 'user/signup.html', {'errors': errors})

    else:
        form = UserCreationForm()

    return render(request, 'user/signup.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'user/profile.html')


def logout_view(request):
    logout(request)  # Log the user out
    return redirect('recipes') 