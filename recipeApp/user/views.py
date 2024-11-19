from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipes.models import Recipe



# Create your views here.

def user_info(request):
    message = 'Name <br> Last Name <br> Birth date <br> E-mail adress <br> Date of registration'
    return HttpResponse(message)



def login_view(request):
    if request.method == 'POST':
        # Get form data from the POST request
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Initialize an empty list for errors
        errors = []
        print(email)
        # Authenticate the user using the email (instead of username)
        try:
            # Find the user by email
            user = User.objects.get(email=email)
            
            # Authenticate with the password
            if user.check_password(password):
                user = authenticate(request, username=user.username, password=password)
            else:
                user = None
                print("erro , didn't pass 1")
        except User.DoesNotExist:
            user = None
            print("eeror, user does not exist")

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

        if User.objects.filter(email=email).exists():
            errors.append("Email already taken.")
        
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
    recettes_user = Recipe.objects.filter(user=request.user)
    return render(request, 'user/profile.html',{'recettes_user':recettes_user})


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        # Initialize an empty list for errors
        errors = []

        # Check if the old password is correct
        if not request.user.check_password(old_password):
            errors.append("Le mot de passe actuel est incorrect.")

        # Validate that the new passwords match
        if new_password1 != new_password2:
            errors.append("Les nouveaux mots de passe ne correspondent pas.")

        # Validate the length of the new password
        if len(new_password1) < 8:
            errors.append("The new password must be at least 8 characters long.")

        # If there are no errors, update the password
        if not errors:
            try:
                # Save the new password
                request.user.set_password(new_password1)
                request.user.save()

                # Keep the user logged in
                update_session_auth_hash(request, request.user)

                return redirect('profile')  # Redirect to the profile page after success
            except Exception as e:
                errors.append(str(e))

        # If there are errors, render the form again with errors
        return render(request, 'user/change_password.html', {'errors': errors})
    return render(request, 'user/change_password.html')

@login_required
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('recipes') 